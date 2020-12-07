import sys
import re
from functools import reduce


BAG_AMOUNT_MATCHER = r'^\s*([0-9]+)\s([a-z]+\s[a-z]+)\sbags?\W*$'

def main(args=None):
    file = open('day07/input.txt', 'r')

    lines = file.read().splitlines()

    rules = {}

    rules_inverted = {}

    for line in lines:
        sline = line.split('contain')
        
        container = sline[0]
        cc = parse_color(container)

        containees = sline[1].split(',')
        if containees == [' no other bags.']:
            rules_inverted[cc] = {}
            continue

        if cc not in rules_inverted:
            rules_inverted[cc] = {}

        for containee in containees:
            color, amount = parse_bags(containee)
            if color in rules.keys():
                rules[color].append((cc, amount))
            else:
                rules[color] = [(cc, amount)]
            
            rules_inverted[cc][color] = int(amount)

    shiny_gold_containers = set(['shiny gold'])

    result_size = len(shiny_gold_containers)
    search = True

    while search:
        result = reduce(lambda a, b: a.union(b), list(map(lambda c: find_containers(c, rules), shiny_gold_containers)))
        shiny_gold_containers = shiny_gold_containers.union(result)
        search = len(shiny_gold_containers) > result_size
        result_size = len(shiny_gold_containers)
    
    
    print(result_size - 1)

    print(graph_traversal_total_bags('shiny gold', rules_inverted))

def parse_bags(string: str) -> (str, int):
    try:
        match = re.fullmatch(BAG_AMOUNT_MATCHER, string)

        amount = match.group(1)
        color = match.group(2)

        return color, amount
    except AttributeError:
        print(f'AttributeError: failed on {string}')

def parse_color(string: str) -> str:
    try: 
        match = re.fullmatch(r'^[^a-z]*([a-z]+\s[a-z]+)\sbags\W*$', string)

        color = match.group(1)

        return color
    except AttributeError:
        print(f'AttributeError: failed on {string}')

def find_containers(color, graph):
    if color not in graph.keys():
        return set()

    containers = graph[color]

    return set([ color for color, amount in containers ])

def graph_traversal_total_bags(color, graph) -> int:
    known_bags = {}

    empty_bags = [ c for c in graph.keys() if graph[c] == {} ]
    for bag in empty_bags:
        known_bags[bag] = 1

    while color not in known_bags:
        for c in graph.keys():
            if set(graph[c].keys()) <= set(known_bags.keys()) and c not in known_bags:
                total = 1

                for c1 in graph[c]:
                    value = graph[c][c1] * known_bags[c1]
                    
                    total += value
                    
                known_bags[c] = total

    return known_bags[color] - 1

if __name__ == "__main__":
    sys.exit(main())
