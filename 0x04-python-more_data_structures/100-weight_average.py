#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    return (sum([x*b for x, b in my_list]) / sum([b for x, b in my_list]))


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
