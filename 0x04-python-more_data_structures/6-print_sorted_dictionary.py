#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Getting the sorted list of keys
    sorted_keys = sorted(a_dictionary.keys())
    # Iterating through the sorted keys and printing the  key-value pairs
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
