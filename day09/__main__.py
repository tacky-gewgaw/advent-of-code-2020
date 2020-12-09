import sys


def main(args=None):
    file = open('day09/input.txt', 'r')

    lines = file.read().splitlines()

    numbers = list(map(int, lines))

    answer_1 = find_first_invalid_number(numbers)

    print(answer_1)

    answer_2 = find_encryption_weakness(answer_1, numbers)

    print(answer_2)

def find_first_invalid_number(sequence: [int]) -> int:
    for i in range(25, len(sequence)):
        num = sequence[i]
        
        valid = is_sum_of_two_numbers(num, sequence[i-25:i])
        if not valid:
            return num
    return -1


def is_sum_of_two_numbers(target: int, numbers: [int]) -> bool:
    for i in range(len(numbers) - 1):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False

def find_encryption_weakness(target: int, sequence: [int]):
    for i in range(len(sequence)):
        result = select_sum_to(target, sequence[i:], [])
        if result:
            return max(result) + min(result)

def select_sum_to(target: int, seq: [int], acc = []) -> [int]:
    head, *tail = seq

    remaining = target - head

    acc.append(head)

    if remaining == 0:
        return acc
    
    if remaining < 0 or tail == []:
        return []

    return select_sum_to(remaining, tail, acc)

if __name__ == "__main__":
    sys.exit(main())
