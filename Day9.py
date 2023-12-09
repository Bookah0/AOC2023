def parse_input():
    return [[int(n) for n in line.strip().split()] for line in open('Input/Day9.txt', "r").readlines()]


def solve_input1():
    sequences = parse_input()
    total = 0
    for history in sequences:
        cur_list, polate_lists = history, []
        while cur_list:
            polate_list = [cur_list[i+1] - cur_list[i] for i in range(len(cur_list) - 1)]
            polate_lists.append(polate_list)
            cur_list = polate_list
            if polate_list[0] == 0 and len(set(polate_list)) == 1:
                total += history[-1] + sum([l[-1] for l in polate_lists])
                cur_list = []
    return total

def solve_input2():
    sequences = parse_input()
    total = 0
    for history in sequences:
        cur_list, polate_lists = history, []
        while cur_list:
            polate_list = [cur_list[i+1] - cur_list[i] for i in range(len(cur_list) - 1)]
            polate_lists.append(polate_list)
            cur_list = polate_list
            print(cur_list)
            if len(cur_list) == 0:
                print(history)
            if cur_list[0] == 0 and len(set(cur_list)) == 1:
                polate_lists[-1].insert(0, 0)
                for i in range(len(polate_lists) - 1, -1, -1):
                    if i > 0:
                        polate_lists[i-1].insert(0, polate_lists[i-1][0]-polate_lists[i][0])
                total += history[0] - polate_lists[0][0]
                cur_list = []
    return total


if __name__ == '__main__':
    print(solve_input2())
