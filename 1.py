def seasons():
    n = int(input("print the number of month: "))
    if n == 1 or n == 2 or n == 12:
        print("winter")
    elif n == 5 or n == 3 or n == 4:
        print("spring")
    elif n == 6 or n == 7 or n == 8:
        print("summer")
    elif n == 9 or n == 10 or n == 11:
        print("autumn")
    else:
        print("sorry, try again")


print(seasons())

#в print после результата выходит ещё строчка с None, я пока не понимаю, откуда она берется..
