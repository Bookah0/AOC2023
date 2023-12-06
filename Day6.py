
def got_first_place(speed, time_left, winning_distance):
    return winning_distance < speed*(time_left)


def parse_input1(race_map={}):
    lines = open('Input/Day6.txt', "r").readlines()
    times, distances = lines[0].split(), lines[1].split()
    return {'race'+str(i): {'distance': int(distances[i]), 'time': int(times[i])} for i in range(1, len(times))}


def solve_input(race_map, total=1):
    for m in race_map:
        tot_time, distance = race_map[m]['time'], race_map[m]['distance']
        total *= sum(1 for time_held in range(tot_time) if got_first_place(time_held, tot_time-time_held, distance))
    print(total)


def parse_input2():
    lines = open('Input/Day6.txt', "r").readlines()
    time_line, distance_line = lines[0][9:].replace(' ', ''), lines[1][9:].replace(' ', '')
    return { 'Race1': {'distance': int(distance_line), 'time': int(time_line)}}


if __name__ == '__main__':
    race_map_1 = parse_input1()
    race_map_2 = parse_input2()

    # solve_input(race_map_1)
    solve_input(race_map_2)
