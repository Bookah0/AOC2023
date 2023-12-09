

def solve_input1():
    histories = [[[int(n) for n in line.strip().split()]] for line in open('Input/Day9.txt', "r").readlines()]

    for history_list in histories:
        cur_list = history_list[0]

        while True:
            cur_list = [cur_list[i+1] - cur_list[i] for i in range(len(cur_list) - 1)]
            history_list.append(cur_list)

            if cur_list[0] == 0 and len(set(cur_list)) == 1:
                history_list[-1].insert(0, 0)
                for i in range(len(history_list) - 1, 0, -1):
                    history_list[i-1].insert(0, history_list[i-1][0]-history_list[i][0])
                break

    before = sum([history_list[0][0] for history_list in histories])
    after = sum([l[-1] for history_list in histories for l in history_list])
    return before, after


if __name__ == '__main__':
    print(solve_input1())
