import re


def parse_input():
    lines = open('Input/Day8.txt', "r").readlines()
    instructions = []
    directions = {}
    for i in range(len(lines)):
        if i == 0:
            instructions = [instruction for instruction in lines[i][:-1]]
        elif i >= 2:
            start, left, right = re.match(r'(.+) = \((.+), (.+)\)', lines[i]).groups()
            directions[start] = {'L': left, 'R': right}

    return instructions, directions

def solve_input():
    instructions, directions = parse_input()
    cur_elem = 'AAA'
    count = 0
    while True:
        for instruction in instructions:
            cur_elem = directions[cur_elem][instruction]
            count += 1
            if cur_elem == 'ZZZ':
                return count


def parse_input2():
    lines = open('Input/Day8.txt', "r").readlines()
    instructions,  = [], []
    directions, starts = {}, {'L': [], 'R': []}
    for i in range(len(lines)):
        if i == 0:
            instructions = [instruction for instruction in lines[i][:-1]]
        elif i >= 2:
            start, left, right = re.match(r'(.+) = \((.+), (.+)\)', lines[i]).groups()
            if start[2] == 'A':
                starts['L'].append(left)
                starts['R'].append()
            if left[2] == 'A' or left[2] == 'Z':
                left = left[2]
            if right[2] == 'A' or right[2] == 'Z':
                right = right[2]
        if start not in directions:

    print(directions, instructions)
    return instructions, directions


def solve_input2():
    instructions, directions = parse_input2()
    cur_elems = ['A']
    new_elems = []
    count = 0
    while count < 7:
        for instruction in instructions:
            for elem in cur_elems:
                new_elems.extend(directions[elem][instruction])
            cur_elems = list(set(new_elems))
            new_elems = []
            count += 1
            print(f'Count is {count}, instruction is {instruction} and elems are {cur_elems}')
            if cur_elems[0] == 'Z':
                if len(set(cur_elems)) == 1:
                    return count

if __name__ == '__main__':
    print(solve_input2())
