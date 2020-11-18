import os

# Initialization
with open("menu.txt", "r") as file:
    menu = file.read()
exit = False

# Start infinite loop
while not exit:

    # Show files in dir and ask user to enter which wants to use
    files = os.listdir()
    count = 0
    videos = []
    print("\nWhich video do you want to edit?\nEnter the number besides the option:")

    for file in files:
        if file.endswith('.mp4'):
            print("{} - {}".format(count,file))
            videos.append(file)
            count += 1

    filename = videos[int(input())]

    # get the option
    option = int(input(menu))
    all_options = False

    # this activates the autoincremental option value to run all the above options
    if option == 5:
        all_options = True
        option = 1

    # exit option
    if option == 0:
        exit = True
        continue

# At each option run the correspondent ffmpeg command asking the user some input if is necessary

    if option == 1:
        start = input("\nSpecify the start in the format: hh:mm:ss \n")
        time = input("\nHow many seconds?\n")
        out = "cut_{}seconds_{}".format(time, filename)
        os.system("ffmpeg -i {} -ss {} -t {} -c copy {}".format(filename, start, time, out))
        if all_options:
            option += 1

    if option == 2:
        out = 'hist_' + filename
        os.system('ffmpeg -i {} -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" {}'.format( filename, out))
        if all_options:
            option += 1

    if option == 3:
        out = "resized_" + filename
        sizes = ["1280:720", "720:480", "360:240", "160:120"]
        idx = int(input("\nWhich resize do you want to apply?\n 1: 720p\n 2: 480p\n 3: 360x240\n 4: 160x120 \n")) - 1
        os.system("ffmpeg -i {} -vf scale={},setsar=1:1 {}".format(filename, sizes[idx], out))
        if all_options:
            option += 1


    if option == 4:
        out = "monoAAC_" + filename
        os.system("ffmpeg -i {} -c:v copy -ac 1 -c:a aac {}".format(filename, out))

# Final print before asking for a new video
    if all_options:
        print("All options executed")
    else:
        print("\nSaved as " + out)
