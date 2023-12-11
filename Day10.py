class Pipe:
    type = ''
    pos = (0, 0)
    connecting_pipes = []
    steps = 0
    on_loop = False
    in_loop = None


    def __init__(self, type, i, j):
        self.type = type
        self.pos = (i, j)

    def set_connecting_pipes(self, pipe_list):
        self.connecting_pipes = []
        if self.type == '.':
            return
        i, j = self.pos[0], self.pos[1]
        if 'east' in self.get_connections() and j != len(pipe_list[i])-1:
            if 'west' in pipe_list[i][j+1].get_connections():
                self.connecting_pipes.append(pipe_list[i][j+1])
        if 'north' in self.get_connections() and i != 0:
            if 'south' in pipe_list[i-1][j].get_connections():
                self.connecting_pipes.append(pipe_list[i-1][j])
        if 'west' in self.get_connections() and j != 0:
            if 'east' in pipe_list[i][j-1].get_connections():
                self.connecting_pipes.append(pipe_list[i][j-1])
        if 'south' in self.get_connections() and i != len(pipe_list)-1:
            if 'north' in pipe_list[i+1][j].get_connections():
                self.connecting_pipes.append(pipe_list[i+1][j])

    def get_connections(self):
        return pipe_map[self.type]
    
    def print_connections(self):
        connecting_pipe_types = [pipe.type for pipe in self.connecting_pipes]
        print(f'Connections for {self.type} at position {self.pos} are {connecting_pipe_types}')

    def get_adjacents(self, pipe_list):
        adjs = []
        i, j = self.pos[0], self.pos[1]
        if i != 0:
            adjs.extend(pipe_list[i-1][max(0, j-1):min(len(pipe_list[i])-1, j+1)])
        if i != len(pipe_list) - 1:
            adjs.extend(pipe_list[i+1][max(0, j-1):min(len(pipe_list[i])-1, j+1)])
        if j != 0:
            adjs.append(pipe_list[i][j-1])
        if j != len(pipe_list[i])-1:
            adjs.append(pipe_list[i][j+1])

        return adjs


pipe_map = {
    '|': ['north', 'south'],
    '-': ['east', 'west'],
    'L': ['north', 'east'],
    'J': ['north', 'west'],
    '7': ['south', 'west'],
    'F': ['south', 'east'],
    '.': [],
    'S': ['south', 'east', 'north', 'west']
    }


def parse_input():
    lines = [line.strip() for line in open('Input/Day10.txt', "r").readlines()]
    start, end, s_pos = None, None, None
    pipe_list = [[Pipe(lines[i][j], i, j) for j in range(len(lines[i]))] for i in range(len(lines))]

    for row in pipe_list:
        for pipe in row:
            pipe.set_connecting_pipes(pipe_list)
            if pipe.type == 'S':
                start = pipe
    return lines, pipe_list, start


def solve_input():
    lines, pipe_list, start = parse_input()
    q = [start]
    visited = set(start.pos)
    cur_pipe = None

    while q:
        cur_pipe = q.pop(0)
        cur_pipe.on_loop = True
        for con_pipe in cur_pipe.connecting_pipes:
            if con_pipe.pos not in visited:
                con_pipe.steps += cur_pipe.steps + 1
                visited.add(cur_pipe.pos)
                q.append(con_pipe)

    print(cur_pipe.steps / 2)

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if cur_pipe.on_loop is False and cur_pipe.in_loop is None:
                if is_enclosed():
                    cur_pipe.in_loop = True
                else:
                    cur_pipe.in_loop = False


def is_enclosed():
    pass # :(((


if __name__ == '__main__':
    solve_input()