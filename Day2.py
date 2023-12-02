import re

INPUT_FILE = 'Input/Day2_1.txt'

def is_game_valid(line):
    round_list = []
    for s in line.split('; '):
        round_list.append(s.split(', '))
    for r in round_list:
        for take_out in r:
            match = re.match('(.+) (.+)', take_out)
            if match.group(2) == 'blue' and int(match.group(1)) > 14:
                return False
            elif match.group(2) == 'red' and int(match.group(1)) > 12:
                return False
            elif match.group(2) == 'green' and int(match.group(1)) > 13:
                return False
    return True


def get_power_of_cubeset(line):
    round_list = []
    max_blue, max_red, max_green = 0, 0, 0
    for s in line.split('; '):
        round_list.append(s.split(', '))
    for r in round_list:
        for take_out in r:
            match = re.match('(.+) (.+)', take_out)
            if match.group(2) == 'blue':
                max_blue = max(max_blue, int(match.group(1)))
            elif match.group(2) == 'red':
                max_red = max(max_red, int(match.group(1)))
            elif match.group(2) == 'green':
                max_green = max(max_green, int(match.group(1)))
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