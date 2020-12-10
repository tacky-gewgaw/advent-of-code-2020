import sys


def main(args=None):
    file = open('day10/input.txt', 'r')

    lines = file.read().splitlines()

    joltages = list(map(int, lines))

    outlet = 0
    device = max(joltages) + 3

    joltages.append(outlet)
    joltages.append(device)
    
    answer_1 = calc_diff_of_adapters(joltages)
    
    print(answer_1)

    answer_2 = calc_arrangements(joltages)

    print(answer_2)

def calc_diff_of_adapters(joltages: [int]) -> int:
    js = sorted(joltages)
    ones = 0
    threes = 0

    for i in range(len(js)-1):
        diff = js[i+1] - js[i]
        if diff == 1:
            ones += 1
        if diff == 3:
            threes +=1
    
    return ones * threes

store = {}

# Dynamic programming, baby!
def calc_arrangements(joltages: [int]) -> int:
    for j in sorted(joltages, reverse=True):
        connections = get_connections(j, joltages)

        if connections == []:
            store[j] = 1
        else:
            store[j] = sum([ store[c] for c in connections ])
    
    return store[min(joltages)]

def get_connections(joltage: int, all: [int]) -> [int]:
    candidates = { joltage+1, joltage+2, joltage+3 }
    return list(candidates.intersection(set(all)))

if __name__ == "__main__":
    sys.exit(main())
