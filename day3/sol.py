from functools import reduce

def readFileToList(filename):
    f = open(filename, "r")    
    q = []
    lines = f.readlines()
    y = 0
    l = 0
    for line in lines:
        l = len(line)
        for i, x in enumerate(line):
            if x == "#":
                q.append((i, y))
        y = y + 1
    return q, y, l

def sol1(q, bottom, l, dx, dy): 
    x = 0 
    y = 0
    tree = 0
    while y <= bottom:
        y = y + dy
        x = x + dx
        if x >= l:
            x = x - l
        if (x, y) in q:
            tree = tree + 1
    return tree

def sol2(q, bottom, l):
    m = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return reduce(lambda a, b: a * b, map(lambda x: sol1(q, bottom, l, x[0], x[1]), m))

if __name__ == "__main__":
    q, bottom, l = readFileToList("input.txt")
    print(sol1(q, bottom, l, 3, 1))
    print(sol2(q, bottom, l))
