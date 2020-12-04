import sys


def main(args=None):
    file = open('day03/input.txt', 'r')

    lines = file.read().splitlines()

    trees_b = count_trees(lines, 3, 1)

    print(f"No. trees in problem one: {trees_b}")

    trees_a = count_trees(lines, 1, 1)
    trees_c = count_trees(lines, 5, 1)
    trees_d = count_trees(lines, 7, 1)
    trees_e = count_trees(lines, 1, 2)

    print(f"Product of trees in all slopes: {trees_a * trees_b * trees_c * trees_d * trees_e}")


def count_trees(input, dx, dy) -> int:
    width = len(input[0])
    height = len(input)

    trees = 0

    x = 0

    for y in range(0,height,dy):
        line = input[y]
        if line[x] == '#':
            trees += 1
        x = (x + dx) % width

    return trees


if __name__ == "__main__":
    sys.exit(main())
