import sys
from functools import reduce


def main(args=None):
    file = open('day06/input.txt', 'r')

    lines = file.read().splitlines()

    print(count_collected_answers_reduced_by(lines, lambda a, b: a.union(b)))
    print(count_collected_answers_reduced_by(lines, lambda a, b: a.intersection(b)))

def count_collected_answers_reduced_by(lines, fun) -> int:
    groups = group_by_linebreak(lines)

    gathered_answers = list(map(
        lambda g: reduce(lambda a, b: fun(a, b), g),
        groups
    ))

    return reduce(lambda a, b: a+b,list(map(len, gathered_answers)))

def group_by_linebreak(lines):
    a_list = []
    current_group = []

    for line in lines:
        if line == '':
            a_list.append(current_group)
            current_group = []
        else:
            current_group.append(set(line))

    if current_group != []:
        a_list.append(current_group)

    return a_list

if __name__ == "__main__":
    sys.exit(main())
