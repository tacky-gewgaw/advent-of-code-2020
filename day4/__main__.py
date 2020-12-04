import sys
import re


def main(args=None):
    file = open('day4/input.txt', 'r')

    lines = file.read().splitlines()

    regex = r'^([a-z]+):([a-z0-9#]+)$'

    passports = []
    currentpp = {}

    for line in lines:
        if line == '':
            passports.append(currentpp)
            currentpp = {}
        else:
            fields = line.split()
            for field in fields:
                match = re.split(regex, field)
                key = match[1]
                value = match[2]
                currentpp[key] = value
    
    if currentpp is not {}:
        passports.append(currentpp)

    valids = [ pp for pp in passports if valid(pp) ]

    print(len(valids))

    corrects = [ pp for pp in valids if correct(pp) ]

    print(len(corrects))
            
def valid(pp: dict) -> bool:
    return set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) <= set(pp.keys())

def correct(pp: dict) -> bool:
    byr = int(pp['byr'])
    
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(pp['iyr'])

    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(pp['eyr'])

    if eyr < 2020 or eyr > 2030:
        return False

    hgt = pp['hgt']
    dh = re.split(r'^([0-9]+)([a-z]{2})$', hgt)
    try:
        num = int(dh[1])
        units = dh[2]
    except IndexError:
        return False

    if units not in ['in','cm']:
        return False
    if units == 'cm':
        if num < 150 or num > 193:
            return False
    if units == 'in':
        if num < 59 or num > 76:
            return False

    hcl = pp['hcl']

    if re.match(r'^#[a-z0-9]{6}$', hcl) is None:
        return False
    
    ecl = pp['ecl']

    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    pid = pp['pid']

    if len(pid) != 9:
        return False

    try:
        int(pid)
    except ValueError:
        return False

    return True

if __name__ == "__main__":
    sys.exit(main())
