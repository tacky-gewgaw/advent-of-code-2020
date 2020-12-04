import sys


def main(args=None):
    file = open('day01/input.txt', 'r')

    lines = file.readlines()

    numbers = list(map(int, lines))

    product = find_product_of_2(numbers)

    print(product)

    product3 = find_product_of_3(numbers)

    print(product3)


def find_product_of_2(numbers):
    sumdict = {}

    for number in numbers:

        if (number > 1010):
            counterpart = 2020 - number
            
            if (counterpart in sumdict.keys()):
                return sumdict[counterpart] * number
            else:
                sumdict[counterpart] = number
        else:
            if (number in sumdict.keys()):
                return sumdict[number] * number
            else:
                sumdict[number] = number
    

def find_product_of_3(numbers):
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == 2020:
                    return a * b * c
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
