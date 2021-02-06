def duplicates(lst):
    st = set(lst)
    if len(lst) == len(st):
        print("good job!")
    else:
        print("there are duplicates...")


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 2, 3, 4]
print(duplicates(list1))
print(duplicates(list2))

#здесь тоже None после результата показывает
