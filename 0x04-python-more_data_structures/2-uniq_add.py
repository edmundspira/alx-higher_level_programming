#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    num = set(my_list)
    for i in num:
        total += i
    return total


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
