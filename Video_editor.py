
menu = open("menu.txt", "r").read()
exit = False

while exit == False:
    option = int(input(menu))
    if option == 0:
        exit = True
