import os

menu = open("menu.txt", "r").read()
exit = False
change_vid = True

while not exit:

    if change_vid:
        filename = input("\nQuin video vols editar?\n")

    option = int(input(menu))

    if option == 0:
        exit = True
        continue

    if option == 1:
        start = input("\nEspecifica l'inici en el format: hh:mm:ss \n")
        time = input("\nQuants segons vols? \n")
        out = "cut_{}seconds_{}".format(time, filename)
        os.system("ffmpeg -i {} -ss {} -t {} -c copy {}".format(filename, start, time, out))


    if option == 2:
        out = 'hist_' + filename
        os.system('ffmpeg -i {} -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" {}'.format( filename, out))


    if option == 3:
        out = "resized_" + filename
        sizes = ["1280:720", "720:480", "360:240", "160:120"]
        idx = int(input("\nA quina resolució el vols canviar?\n 1: 720p\n 2: 480p\n 3: 360x240\n 4: 160x120 \n")) - 1
        os.system("ffmpeg -i {} -vf scale={},setsar=1:1 {}".format(filename, sizes[idx], out))


    if option == 4:
        out = "monoAAC_" + filename
        os.system("ffmpeg -i {} -c:v copy -ac 1 -c:a aac {}".format(filename, out))

    print("\nGuardat com a " + out)
