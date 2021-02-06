def seasons():
    n = int(input("print the number of month: "))
    if n in {1, 2, 12}:
        print("winter")
    elif n in {3, 4, 5}:
        print("spring")
    elif n in {6, 7, 8}:
        print("summer")
    elif n in {9, 10, 11}:
        print("autumn")
    else:
        print("sorry, try again")


seasons()
