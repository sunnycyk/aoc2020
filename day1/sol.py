from functools import reduce
from time import process_time

def readFileToList(filename):
    f = open(filename, "r")    
    q = []
    lines = f.readlines()
    for line in lines:
        q.append(int(line))
    return q

def sol1(x, q): 
    if len(q) == 0: 
        return
    y = 2020 - x
    if y in q:
        print(x * y)
    else:
        sol1(q[1:][0], q[1:])

def sol2(x, q):
    if len(q) == 0:
        return
    for y in q:
        z = 2020 - x - y
        if z in q:
            print(x * y * z)
            return
    sol2(q[0], q[1:])

if __name__ == "__main__":
    q = readFileToList("input.txt")
    t1_start = process_time()
    sol1(q[0], q[1:])
    t1_stop = process_time()
    print(t1_stop - t1_start)

    t1_start = process_time()
    sol2(q[0], q[1:])
    t1_stop = process_time()
    print(t1_stop - t1_start)
    
    t1_start = process_time()
    print(reduce(lambda a, b: a * b, filter(lambda y: y in q, map(lambda x: 2020 - x, q))))  
    t1_stop = process_time()
    print(t1_stop - t1_start)