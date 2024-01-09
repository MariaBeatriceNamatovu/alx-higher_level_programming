#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    modified_copy = my_list.copy()
    if idx < 0:
        return modified_copy
    elif idx >= len(my_list):
        return modified_copy
    else:
        modified_copy[idx] = element
        return modified_copy
