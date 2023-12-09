import math
import re


def parse_input():
    lines = open('Input/Day8.txt', "r").readlines()
    instructions, starts = [], []
    directions = {}

    for i in range(len(lines)):
        if i == 0:
            instructions = [instruction for instruction in lines[i][:-1]]
        elif i >= 2:
            start, left, right = re.match(r'(.+) = \((.+), (.+)\)', lines[i]).groups()
            if start[2] == 'A':
                starts.append(start)
            directions[start] = {'L': left, 'R': right}

    return instructions, directions, starts

def solve_input():
    instructions, directions, starts = parse_input()
    results = []

    for start in starts:
        cur_elem = start
        found = False
        count = 0
        while not found:
            for instruction in instructions:
                cur_elem = directions[cur_elem][instruction]
                count += 1
                if cur_elem[2] == 'Z':
                    results.append(count)
                    found = True

    return math.lcm(*results)


if __name__ == '__main__':
    print(solve_input())