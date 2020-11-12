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
        start = input("\nSelect start time in format: hh:mm:ss \n")
        time = int(input("\nHow many seconds? \n"))

        os.system("ffmpeg -ss {} -i {} -t {} -c copy {}".format(start, filename, time, 'cut' + filename))

    if option == 2:

        os.system('ffmpeg -i {} -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" {}'.format( filename, 'hist' + filename))
