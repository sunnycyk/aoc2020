import numpy
import itertools
# 0 .
# 1 L
# -1 #

def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    h = len(inputs) + 2
    w = len(inputs[0]) + 2
    m = numpy.zeros((w, h))
    x = 1
    y = 1
    for input in inputs:
        for p in list(input):
            if p == "L":
                m[y][x] = 1
            y = y + 1
        y = 1
        x = x + 1 
    return m

def adj(x, y, m, target):
    k = len(list(filter(lambda a: a == target, [m[y-1][x-1], m[y-1][x], m[y-1][x+1], m[y][x-1], m[y][x+1], m[y+1][x-1], m[y+1][x], m[y+1][x+1]])))
    return k 

def sol1(m):
    x = 1
    y = 1
    m2 = m.copy()
  
    while True:
        if m[y][x] == 1 and adj(x, y, m, 2) == 0:
            m2[y][x] = 2
        elif m[y][x] == 2 and adj(x, y, m, 2) >= 4:
            m2[y][x] = 1
        x = x + 1
        if x == len(m[0]) - 1:
            x = 1
            y = y + 1
        if y == len(m) - 1:
            compare = numpy.array(m) == numpy.array(m2)
            if compare.all():
                break
            m = m2.copy()
            y = 1
    occupied = list(filter(lambda a: a == 2, list(itertools.chain.from_iterable(m))))
    return len(occupied)

def direction(x, y, incx, incy, m):
    while True:
        x = x + incx
        y = y + incy
        if x == len(m[0]) or x == 0 or y == 0 or y == len(m):
            return 0
        if m[y][x] > 0:
            return m[y][x]

def adj2(x, y, m):
    occupied = 0
    d = []
    if m[y][x] == 1:
        for incx, incy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1) ]:
            d = direction(x, y, incx, incy, m)
            if d == 2:
                return 1
        return 2
    elif m[y][x] == 2:
        count = 0
        for incx, incy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1) ]:
            d = direction(x, y, incx, incy, m)
            if d == 2:
                count = count + 1
                if count == 5:
                    return 1
    return m[y][x]
        

def sol2(m):
    x = 1
    y = 1
    m2 = m.copy()
    while True:
        m2[y][x] = adj2(x, y, m)
        x = x + 1
        if x == len(m[0]) - 1:
            x = 1
            y = y + 1
        if y == len(m) - 1:
            compare = numpy.array(m) == numpy.array(m2)
            if compare.all():
                break
            m = m2.copy()
            y = 1
    occupied = list(filter(lambda a: a == 2, list(itertools.chain.from_iterable(m))))
    return len(occupied)

    
if __name__ == "__main__":
    q = readFileToList("input.txt")
    print(sol1(q))
    print(sol2(q))