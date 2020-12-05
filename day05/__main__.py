import sys


def main(args=None):
    file = open('day05/input.txt', 'r')

    lines = file.read().splitlines()

    taken_seats = list(map(get_seat_position, lines))

    taken_seat_ids = [ get_seat_id(r, c) for r, c in taken_seats ]

    print(max(taken_seat_ids))

    for row in range(128):
        for column in range(8):
            id = get_seat_id(row, column)
            if id not in taken_seat_ids:
                if id + 1 in taken_seat_ids and id - 1 in taken_seat_ids:
                    print(id)
                    return
    

def get_seat_position(line) -> (int, int):
    row_indicators = list(line[:7])

    row = find_spot(row_indicators, range(128), 'F', 'B')

    column_indicators = list(line[7:])

    column = find_spot(column_indicators, range(8), 'L', 'R')

    return row, column

def get_seat_id(row: int, column: int) -> int:
    return (row * 8) + column

def find_spot(indicators, space, low_c, up_c) -> int:
    if space == []:
        print("ERROR: space is empty")
        return -1

    if indicators == [] and len(space) == 1:
        return space[0]
    
    i, *tail = indicators
    new_space = []
    split_index = int(len(space)/2)
    if i == low_c:
        new_space = space[:split_index]
    elif i == up_c:
        new_space = space[split_index:]
    else:
        print("ERROR: invalid character")
        
    return find_spot(tail, new_space, low_c, up_c)

if __name__ == "__main__":
    sys.exit(main())
