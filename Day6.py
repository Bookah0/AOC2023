
def get_travel_time(speed, time_left, winning_distance):
    return winning_distance+1 <= speed*(time_left)


def parse_input1():
    race_map = {}
    lines = open('Input/Day6.txt', "r").readlines()
    time_line, distance_line = lines[0].split(), lines[1].split()
    for i in range(1, len(time_line)):
        race_map['race'+str(i)] = {'distance': int(distance_line[i]), 'time': int(time_line[i])}
    return race_map


def solve_input(race_map):
    total = 1
    for m in race_map:
        n_record_beats = 0
        time, distance = race_map[m]['time'], race_map[m]['distance']
        for time_held in range(time):
            if get_travel_time(time_held, time-time_held, distance):
                n_record_beats += 1
        total *= n_record_beats
    print(total)


def parse_input2():
    lines = open('Input/Day6.txt', "r").readlines()
    time_line, distance_line = lines[0][9:].replace(' ', ''), lines[1][9:].replace(' ', '')
    return { 'Race1': {'distance': int(distance_line), 'time': int(time_line)}}


if __name__ == '__main__':
    race_map_1 = parse_input1()
    race_map_2 = parse_input2()

    # solve_input1(race_map_1)
    solve_input2(race_map_2)
