#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string) - 1):
        current_char = roman_string[i]
        next_char = roman_string[i + 1]

        current_value = roman_numerals.get(current_char, 0)
        next_value = roman_numerals.get(next_char, 0)

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result + roman_numerals.get(roman_string[-1], 0)
