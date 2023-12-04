import re

INPUT_FILE = 'Input/Day2_1.txt'

def is_game_valid(line):
    round_list = [s.split(', ') for s in line.split('; ')]
    for r in round_list:
        for take_out in r:
            num, color = re.match('(.+) (.+)', take_out).groups()
            if color == 'blue' and int(num) > 14:
                return False
            elif color == 'red' and int(num) > 12:
                return False
            elif color == 'green' and int(num) > 13:
                return False
    return True


def get_power_of_cubeset(line):
    round_list = [s.split(', ') for s in line.split('; ')]
    max_blue, max_red, max_green = 0, 0, 0
    for r in round_list:
        for take_out in r:
            num, color = re.match('(.+) (.+)', take_out).groups()
            if color == 'blue':
                max_blue = max(max_blue, int(num))
            elif color == 'red':
                max_red = max(max_red, int(num))
            elif color == 'green':
                max_green = max(max_green, int(num))
    return max_blue*max_red*max_green


def solve_input():
    sum = 0
    f = open(INPUT_FILE, "r")
    for input_line in f.readlines():
        match = re.match("Game (.+): (.+)", input_line)
        if is_game_valid(match.group(2)):
            print(match.group(1))
            sum += int(match.group(1))
    return sum


def solve_input2():
    sum = 0
    f = open(INPUT_FILE, "r")
    for input_line in f.readlines():
        match = re.match("Game (.+): (.+)", input_line)
        sum += get_power_of_cubeset(match.group(2))
    return sum


if __name__ == '__main__':
    print(solve_input2())