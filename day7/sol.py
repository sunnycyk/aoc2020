from functools import reduce
import re

def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    bags = {}
    for input in inputs:
        matches = re.search("([\w\s]+) bags contain((( ([\d]) ([\w\s]+) bag[s]?)[,.])+| no other bags.)", input)
        bag_id = matches.group(1)
        bags[bag_id] = []
        contains = matches.group(2).split(",")
        for bag in contains:
            if bag == " no other bags.":
                continue
            bag_match = re.search("([\d]) ([\w\s]+) bag[s]?[.]?", bag)
            bags[bag_id].append((bag_match.group(1), bag_match.group(2)))
    return bags

def find_shiny_bag(q, bags):
    if len(bags) == 0:
        return False
    if 'shiny gold' in bags:
        return True
    else:
        for bag in bags:
            if find_shiny_bag(q, q[bag]):
                return True
        return False

def sol1(q):
    shiny_bag = 0
    # reconstruct
    for x in q.keys():
        bags = list(map(lambda a: a[1], q[x]))
        q[x] = bags
    
    for x in q.keys():
        if find_shiny_bag(q, q[x]):
            shiny_bag = shiny_bag + 1
    return shiny_bag

def find_num_bags(q, n_bag, bag_name):
    if len(q[bag_name]) == 0:
        return n_bag
    bags = q[bag_name]
    total = 0
    for bag in bags:
        n, name = bag
        total = total + n_bag * find_num_bags(q, int(n), name)
    return total + n_bag

def sol2(q):
    return find_num_bags(q, 1, 'shiny gold') - 1

if __name__ == "__main__":
    q = readFileToList("input.txt")
    print(sol1(q))
    q = readFileToList("input.txt")
    print(sol2(q))