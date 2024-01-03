#!/usr/bin/python3

def uppercase(str):
    result = 'i'
    for i in str:
        if i >= 'a' and i <= 'z':
            result += chr(ord(i)-32)
        else:
            result += i
    return result


str = "best"
upper = uppercase(str)
print(upper)
