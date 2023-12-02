def combine_first_and_last_digit2(input: str):
    first_digit, last_digit = None, None

    for i in range(len(input)):
        str_number = str_to_number(input[i:])

        if input[i].isdigit():
            if first_digit is None:
                first_digit = input[i]
            last_digit = input[i]
        elif str_number is not None:
            if first_digit is None:
                first_digit = str_number
            last_digit = str_number

    return first_digit + last_digit


def combine_first_and_last_digit1(input: str):
    first_digit, last_digit = None, None

    for i in range(len(input)):
        if input[i].isdigit():
            if first_digit is None:
                first_digit = input[i]
            last_digit = input[i]

    return first_digit + last_digit


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

    for number in number_dict:
        if letters[:len(number)-1] == number:
            return number_dict[number]
    return None



def solve_input(INPUT_FILE):
    sum = 0
    f = open(INPUT_FILE, "r")
    for input_line in f.readlines():
        sum += int(combine_first_and_last_digit2(input_line))
    return sum


if __name__ == '__main__':
    print(solve_input("Input/Day1_2.txt"))
