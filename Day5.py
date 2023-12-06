import re
import time
map_dict = {
    'seed_map': {'next': 'soil_map', 'seeds': [], 'data': []},
    'soil_map': {'next': 'fertilizer_map', 'seeds': [], 'data': []},
    'fertilizer_map': {'next': 'water_map', 'seeds': [], 'data': []},
    'water_map': {'next': 'light_map', 'seeds': [], 'data': []},
    'light_map': {'next': 'temperature_map', 'seeds': [], 'data': []},
    'temperature_map': {'next': 'humidity_map', 'seeds': [], 'data': []},
    'humidity_map': {'next': 'location_map', 'seeds': [], 'data': []},
    'location_map': {'next': None, 'seeds': [], 'data': []},
}

def parse_input1():
    with open('Input/Day5.txt', "r") as f:
        cur_map = None
        for line in f.readlines():
            if line[:5] == 'seeds':
                map_dict['seed_map']['seeds'].extend(map(int, line.split()[1:]))
            elif line[0].isalpha():
                _, cur_map_name = re.match('(.+)-to-(.+) map:', line).groups()
                cur_map = map_dict[cur_map_name + '_map']
            elif line[0].isdigit() and cur_map is not None:
                d_range, s_range, range_len = re.match(r'(.+) (.+) (.+)', line).groups()
                cur_map['data'].append((int(d_range), int(s_range), int(range_len)))


def solve_input1():
    parse_input2()
    for map in map_dict:
        seeds, next = map_dict[map]['seeds'], map_dict[map]['next']
        if next is None:
            seeds.sort()
            return seeds[0]
        next_seeds = map_dict[next]['seeds']
        for i in range(len(seeds)):
            for data in map_dict[next]['data']:
                d_range, s_range, range_len = data[0], data[1], data[2]
                if s_range <= seeds[i] < (s_range + range_len):
                    next_seeds.append(seeds[i] + d_range - s_range)
            if len(next_seeds) != i + 1:
                next_seeds.append(seeds[i])


def parse_input2():
    with open('Input/Day5.txt', "r") as f:
        cur_map = None

        for line in f.readlines():
            if line[:5] == 'seeds':
                line = line.split()[1:]
                map_dict['seed_map']['seeds'] = [(int(line[i]), int(line[i + 1]) + int(line[i])) for i in
                                                 range(0, len(line), 2) if i < len(line)]
            elif line[0].isalpha():
                _, cur_map_name = re.match('(.+)-to-(.+) map:', line).groups()
                cur_map = map_dict[cur_map_name + '_map']
            elif line[0].isdigit():
                d_range, s_range, range_len = re.match(r'(.+) (.+) (.+)', line).groups()
                cur_map['data'].append((int(s_range), int(s_range) + int(range_len), int(d_range) - int(s_range)))
    print(map_dict)


def solve_input2():
    for map in map_dict:
        seeds, next = map_dict[map]['seeds'], map_dict[map]['next']
        if next is None:
            return get_min(seeds)

        for i in range(len(seeds)):
            seed_start, seed_end = seeds[i][0], seeds[i][1]
            found_range = False

            for data in map_dict[next]['data']:
                source_start, source_end, diff = data[0], data[1], data[2]
                new_seed_range = get_intersection_of_range((seed_start, seed_end), (source_start, source_end), diff)

                if new_seed_range is not None:
                    found_range = True
                    map_dict[next]['seeds'].append(new_seed_range)

            if found_range is False:
                map_dict[next]['seeds'].append(seeds[i])


def get_intersection_of_range(range1, range2, diff):
    start1, end1 = range1
    start2, end2 = range2

    if start1 < end2 and end1 > start2:
        return max(start1, start2) + diff, min(end1, end2) + diff
    else:
        return None


def get_min(seeds):
    min_location = float('inf')
    for seed in seeds:
        min_location = min(min_location, seed[0])
    return min_location


if __name__ == '__main__':
    start = time.time()
    parse_input2()
    print(solve_input2())
    end = time.time()
    print(end - start)
