#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list


my_list = [1, 2, 3, 4, 5]
element = 9
idx = 3
new_list = replace_in_list(my_list, idx, element)
print(new_list)
print(my_list)
