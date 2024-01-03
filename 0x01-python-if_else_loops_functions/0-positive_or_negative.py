#!/usr/bin/python3
import random

number = random.rand(-10, 10)
if number > 0:
    print('is positive\n')
elif number == 0:
    print('is zero\n')
else:
    print('is negative\n')
