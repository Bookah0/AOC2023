import re

INPUT_FILE = 'Input/Day3.txt'


def get_adjacent_numbers(gear_ind, line:str):
    numbers = {}
    adjacent_numbers = []
    cur_num = ''
    for i in range(len(line)):
        if line[i].isdigit():
            cur_num += line[i]
        if cur_num != '' and not line[i].isdigit():
            for j in range(len(cur_num)):
                numbers[i-j-1] = cur_num
            cur_num = ''
    print(numbers)
    if gear_ind-1 in numbers:
        adjacent_numbers.append(numbers[gear_ind-1])
    if gear_ind + 1 in numbers and numbers[gear_ind+1] not in adjacent_numbers:
        adjacent_numbers.append(numbers[gear_ind + 1])
    if gear_ind in numbers and numbers[gear_ind] not in adjacent_numbers:
        adjacent_numbers.append(numbers[gear_ind])
    return adjacent_numbers


def solve_input2():
    f = open(INPUT_FILE, "r")
    lines = f.readlines()
    sum = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                line_under, line_over = None, None
                if i != 0:
                    line_over = lines[i - 1]
                if i != len(lines)-1:
                    line_under = lines[i + 1]
                adjacent_numbers = get_adjacent_numbers(j, lines[i])
                adjacent_numbers.extend(get_adjacent_numbers(j, line_over))
                adjacent_numbers.extend(get_adjacent_numbers(j, line_under))
                if len(adjacent_numbers) == 2:
                    sum += int(adjacent_numbers[0]) * int(adjacent_numbers[1])
    return sum


def solve_input1():
    f = open(INPUT_FILE, "r")
    lines = f.readlines()
    sum = 0

    for i in range(len(lines)):
        start_ind, end_ind = None, None
        for j in range(len(lines[i])):
            if start_ind is None:
                start_ind = get_num_start_ind(i, j, lines)
            if start_ind is not None:
                end_ind = get_num_end_ind(i, j, lines)
            if end_ind is not None:
                line_under, line_over = None, None
                if i != 0:
                    line_over = lines[i - 1]
                if i != len(lines)-1:
                    line_under = lines[i + 1]
                if is_adjacent(start_ind, end_ind, lines[i], line_over, line_under):
                    sum += int(lines[i][start_ind:end_ind + 1])
                    print(f'{lines[i][start_ind:end_ind + 1]} is adjacent')
                start_ind, end_ind = None, None
    return sum


def is_adjacent(start_ind, end_ind, line, line_over, line_under):
    if start_ind > 0:
        start_ind -= 1
    if end_ind < len(line) - 1:
        end_ind += 1

    lines = [line[start_ind], line[end_ind]]

    if line_over is not None:
        lines.extend(line_over[start_ind:end_ind + 1])

    if line_under is not None:
        lines.extend(line_under[start_ind:end_ind + 1])

    lines = [l for l in lines if l != '\n']

    for c in lines:
        if c != '.':
            if not c.isdigit():
                return True
    return False

def get_num_start_ind(i, j, lines):
    if j == 0:
        if lines[i][j].isdigit():
            return j
    elif j > 0:
        if not lines[i][j - 1].isdigit() and lines[i][j].isdigit():
            return j


def get_num_end_ind(i, j, lines):
    if j < len(lines[i]) - 1:
        if not lines[i][j + 1].isdigit() and lines[i][j].isdigit():
            return j
    elif j == len(lines[i]) - 1:
        if lines[i][j].isdigit():
            return j
    return None


if __name__ == '__main__':
    print(solve_input2())
