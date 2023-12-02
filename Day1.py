# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def combine_first_and_last_digit(pz_input:str):
    first_digit, last_digit = None, None
    for i in range(len(pz_input)):
        str_number = is_number(pz_input[i:])
        if first_digit is None:
            if str_number is not None:
                first_digit = str_number
                last_digit = str_number
            elif pz_input[i].isdigit():
                first_digit = pz_input[i]
                last_digit = pz_input[i]
        elif pz_input[i].isdigit():
            last_digit = pz_input[i]
        elif str_number is not None:
            last_digit = str_number
    print(f'the input is {pz_input} and the result is {first_digit+last_digit}')
    return first_digit+last_digit


def is_number(letters):
    if letters[0] == 'o':
        if len(letters) > 2 and letters[0:3] == 'one':
            return '1'
    elif letters[0] == 't':
        if len(letters) > 2 and letters[0:3] == 'two':
            return '2'
        elif len(letters) > 4 and letters[0:5] == 'three':
            return '3'
    elif letters[0] == 'f':
        if len(letters) > 3 and letters[0:4] == 'four':
            return '4'
        elif len(letters) > 3 and letters[0:4] == 'five':
            return '5'
    elif letters[0] == 's':
        if len(letters) > 2 and letters[0:3] == 'six':
            return '6'
        elif len(letters) > 4 and letters[0:5] == 'seven':
            return '7'
    elif letters[0] == 'e':
        if len(letters) > 4 and letters[0:5] == 'eight':
            return '8'
    elif letters[0] == 'n':
        if len(letters) > 3 and letters[0:4] == 'nine':
            return '9'
    return None


def solve_input(INPUT_FILE):
    sum = 0
    f = open(INPUT_FILE, "r")
    for input_line in f.readlines():
        sum += int(combine_first_and_last_digit(input_line))
    return sum


if __name__ == '__main__':
    print(solve_input("Input/Day1_2.txt"))

