def parse_input():
    universe = [list(line.strip()) for line in open('Input/Day11.txt', "r").readlines()]
    inds_vert = [i for (i, col) in enumerate(zip(*universe)) if len(set(col)) == 1]
    inds_hor = [i for i in range(len(universe)) if len(set(universe[i])) == 1]
    galaxy_positions = [(j, i) for i in range(len(universe)) for j in range(len(universe[i])) if universe[i][j] == '#']

    return inds_hor, inds_vert, universe, galaxy_positions

def solve_input():
    inds_hor, inds_vert, universe, galaxy_positions = parse_input()
    expansions_traversed, tot = 0, 0
    while galaxy_positions:
        source = galaxy_positions.pop(0)
        for target in galaxy_positions:
            expansions_traversed += sum(1 for ind in inds_hor if source[1] < ind < target[1])
            expansions_traversed += sum(1 for ind in inds_vert if target[0] < ind < source[0] or target[0] > ind > source[0])
            tot += abs(target[1] - source[1]) + abs(target[0] - source[0])
    print(tot+expansions_traversed, tot+(expansions_traversed*9999))


if __name__ == '__main__':
    solve_input()