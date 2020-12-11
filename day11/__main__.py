import sys
import functools


def main(args=None):
    file = open('day11/input.txt', 'r')

    lines = file.read().splitlines()

    cells = list(map(list, lines))

    final_state_1 = run_until_stable(cells, update_state)

    print(sum(list(map(lambda row: row.count('#'), final_state_1))))

    final_state_2 = run_until_stable(cells, update_state_2)

    print(sum(list(map(lambda row: row.count('#'), final_state_2))))


def run_until_stable(cells: [[str]], func) -> [[str]]:
    
    run = True
    mem = cells

    while run:
        run = False
        copy = []

        for y in range(len(mem)):
            row = []
            for x in range(len(mem[y])):
                changed, state = func(x, y, mem)
                run = run or changed
                row.append(state)
            copy.append(row)
                
        mem = copy

    return mem
        

def update_state(x: int, y: int, cells: [[str]]) -> (bool, str):
    this_cell = cells[y][x]
    if this_cell == '.':
        return False, this_cell

    neighbours = [
        (x-1, y-1), (x, y-1), (x+1, y-1),
        (x-1, y), (x+1, y),
        (x-1, y+1), (x, y+1), (x+1, y+1),
    ]
    
    max_y = len(cells)-1
    max_x = len(cells[0])-1
    
    valid_neighbours = [ (x, y) for (x,y) in neighbours if 0 <= x <= max_x and 0 <= y <= max_y ]
    v_n = [ cells[y][x] for (x,y) in valid_neighbours ]
    occupied = len([ s for s in v_n if s == '#' ])

    if this_cell == 'L':
        if occupied == 0:
            return (True, '#')
    elif this_cell == '#':
        if occupied >= 4:
            return (True, 'L')

    return (False, this_cell)

def print_cells(c: [[str]]):
    for row in c:
        print(''.join(row))

def count_visible_occupied_seats(x: int, y: int, cells: [[str]]) -> int:
    directions = [
        (-1,-1), (0, -1), (1, -1),
        (-1, 0),          (1,  0),
        (-1, 1), (0,  1), (1,  1)
    ]

    return sum([ find_seat(x, y, dx, dy, cells) for dx, dy in directions ])

def find_seat(x, y, dx, dy, cells: [[str]]) -> int:
    x1 = x + dx
    y1 = y + dy

    if not (0 <= x1 < len(cells[0]) and 0 <= y1 < len(cells)):
        return 0

    this_cell = cells[y1][x1]
    if this_cell == '#':
        return 1
    elif this_cell == 'L':
        return 0
    elif this_cell == '.':
        return find_seat(x1, y1, dx, dy, cells)

def update_state_2(x: int, y: int, cells: [[str]]) -> (bool, str):
    this_cell = cells[y][x]
    if this_cell == '.':
        return False, this_cell

    occupied = count_visible_occupied_seats(x, y, cells)

    if this_cell == 'L':
        if occupied == 0:
            return (True, '#')
    elif this_cell == '#':
        if occupied >= 5:
            return (True, 'L')

    return (False, this_cell)

if __name__ == "__main__":
    sys.exit(main())
