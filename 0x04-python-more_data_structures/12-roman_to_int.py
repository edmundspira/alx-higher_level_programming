#!/usr/bin/python3
def roman_to_int(roman_string):
    num_arr = []
    total = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0

    for i in range(0, len(roman_string)):
        if roman_string[i] == "I":
            num_arr.append(1)
        if roman_string[i] == "V":
            num_arr.append(5)
        if roman_string[i] == "X":
            num_arr.append(10)
        if roman_string[i] == "L":
            num_arr.append(50)
        if roman_string[i] == "C":
            num_arr.append(100)
        if roman_string[i] == "D":
            num_arr.append(500)
        if roman_string[i] == "M":
            num_arr.append(1000)


    for i in range(0, len(num_arr)):
        if i < len(num_arr) - 1:
            if num_arr[i] < num_arr[i + 1]:
                total -= num_arr[i]
            else:
                total += num_arr[i]
    total += num_arr[i]
    return total



roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
