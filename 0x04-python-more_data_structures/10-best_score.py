#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        # Finding the key with the maximum value using max and dictionary.get
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None
