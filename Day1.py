
def combine_first_and_last_digit2(input, first=None, last=None):
    for i in range(len(input)):
        cur_digit = str_to_number(input[i:])
        if input[i].isdigit():
            cur_digit = input[i]

        if cur_digit is not None:
            if first is None:
                first = cur_digit
            last = cur_digit

    return first + last


def combine_first_and_last_digit1(input, first=None, last=None):
    for i in range(len(input)):
        if input[i].isdigit():
            if first is None:
                first = input[i]
            last = input[i]

    return first + last


def str_to_number(letters):
    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    return number_dict.get(letters[:len(letters) - 1], None)



def solve_input(INPUT_FILE, sum = 0):
    for input_line in open(INPUT_FILE, "r").readlines():
        sum += int(combine_first_and_last_digit2(input_line))
    return sum


if __name__ == '__main__':
    print(solve_input("Input/Day1_2.txt"))
