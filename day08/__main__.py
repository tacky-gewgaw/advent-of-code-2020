import sys
import re


R = r'^([a-z]{3})\s([-+][0-9]+)$'

def main(args=None):
    file = open('day08/input.txt', 'r')

    lines = file.read().splitlines()

    instructions = []

    for line in lines:
        instructions.append(parse_line(line))

    result_1 = calc_acc(instructions)

    print(result_1)

    alts = generate_alternatives(instructions)

    for a in alts:
        result = calc_alc_if_terminated(a)

        if result != None:
            print(result)
            break

def parse_line(i: str) -> (str, int):
    match = re.match(R, i)

    instr = match[1]
    val = int(match[2])

    return instr, val

def calc_acc(instructions: [(str, int)]) -> int:
    acc = 0
    i = 0
    visited = set()

    while i not in visited and i < len(instructions):
        visited.add(i)
        
        instr, value = instructions[i]

        if instr == 'nop':
            i += 1
        elif instr == 'acc':
            acc += value
            i += 1
        elif instr == 'jmp':
            i += value
        else:
            print(f'Unknown instruction: {instr}')
            break

    return acc

def calc_alc_if_terminated(instructions: [(str, int)]):
    acc = 0
    i = 0
    visited = set()

    while i < len(instructions):
        if i in visited:
            return None

        visited.add(i)
        
        instr, value = instructions[i]

        if instr == 'nop':
            i += 1
        elif instr == 'acc':
            acc += value
            i += 1
        elif instr == 'jmp':
            i += value
        else:
            print(f'Unknown instruction: {instr}')
            break

        if i == len(instructions)-1:
            return acc
    
    return None

def generate_alternatives(instructions: [(str, int)]) -> [(str, int)]:
    result = []

    for i in range(len(instructions)):
        instr, v = instructions[i]

        if instr == 'jmp':
            # Copy instr with altered position into result
            copy = instructions.copy()
            copy[i] = ('nop', v)
            result.append(copy)
        elif instr == 'nop':
            # Copy instr with altered position into result
            copy = instructions.copy()
            copy[i] = ('jmp', v)
            result.append(copy)

    return result

if __name__ == "__main__":
    sys.exit(main())
