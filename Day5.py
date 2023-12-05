import re
soil_map, fertilizer_map, water_map, light_map, temperature_map, humidity_map, location_map = {}, {}, {}, {}, {}, {}, {}
seeds = []

def parse_input():
    with open('Input/Day5.txt', "r") as f:
        cur_map = None
        for line in f.readlines():
            if line[:5] == 'seeds':
                seeds.extend(map(int, line.split()[1:]))
            elif line[0].isalpha():
                _, cur_map_name = re.match('(.+)-to-(.+) map:', line).groups()
                cur_map = globals().get(cur_map_name + '_map')
            elif line[0].isdigit() and cur_map is not None:
                d_range, s_range, range_len = re.match(r'(.+) (.+) (.+)', line).groups()
                d = range(int(s_range), int(s_range)+int(range_len))
                s = range(int(d_range), int(d_range)+int(range_len))
                for i in range(len(s)):
                    cur_map[d[i]] = s[i]


def solve_input1():
    parse_input()
    locations = []
    for seed in seeds:
        soil = get_default(soil_map, seed)
        fert = get_default(fertilizer_map, soil)
        water = get_default(water_map, fert)
        light = get_default(light_map, water)
        temp = get_default(temperature_map, light)
        hum = get_default(humidity_map, temp)
        locations.append(get_default(location_map, hum))
    locations.sort()
    print(locations[0])


def get_default(map, get):
    val = map.get(get)
    if val is None:
        return get
    return val


if __name__ == '__main__':
    solve_input1()