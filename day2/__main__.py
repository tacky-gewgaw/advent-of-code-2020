import sys
import re


def main(args=None):
    file = open('day2/input.txt', 'r')

    lines = file.read().splitlines()
    
    regex = r'^([0-9]+)-([0-9]+)\s([a-z]):\s([a-z]+)$'

    valid_pws1 = 0
    valid_pws2 = 0

    for line in lines:
        match = re.split(regex, line)

        low = int(match[1])
        high = int(match[2])
        char = match[3]
        pw = match[4]

        valid_pws1 += is_valid1(low, high, char, pw)
        
        valid_pws2 += is_valid2(low, high, char, pw)

    print(f"Valid passwords by option 1: {valid_pws1}")
    print(f"Valid passwords by option 2: {valid_pws2}")

def is_valid1(low, high, char, pw) -> int:
    occ = 0
    for c in pw:
        if c==char:
            occ = occ + 1
            if occ > high:
                return 0
    
    if occ < low:
        return 0

    return 1

def is_valid2(index1, index2, char, pw) -> int:
    if (pw[index1-1] == char) ^ (pw[index2-1] == char):
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
