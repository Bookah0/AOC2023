def parse_input1(race_map={}):
    lines = open('Input/Day6.txt', "r").readlines()
    times, distances = lines[0].split(), lines[1].split()
    return {str(i): {'distance': int(distances[i]), 'time': int(times[i])} for i in range(1, len(times))}

def parse_input2():
    lines = open('Input/Day6.txt', "r").readlines()
    time_line, distance_line = lines[0][9:].replace(' ', ''), lines[1][9:].replace(' ', '')
    return { '1': {'distance': int(distance_line), 'time': int(time_line)}}


def solve_input(race_map, total=1):
    for m in race_map:
        tot_time, distance = race_map[m]['time'], race_map[m]['distance']
        total *= sum(1 for time_held in range(tot_time) if distance < time_held * (tot_time-time_held))
    print(total)


if __name__ == '__main__':
    # solve_input(parse_input1())
    solve_input(parse_input2())
