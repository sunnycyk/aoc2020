import re
from functools import reduce


def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    return inputs


def sol1(q):
    mem = {}
    mask = ""
    for p in q:
        if p.startswith("mask"):
            g = re.search("^mask = ([X10]{36})?", p)
            mask = g[1]
        else:
            g = re.search("^mem\[(\d+)\] = (\d+)?", p)
            addr = g[1]
            value = list(format(int(g[2]), '036b'))
            for i in range(len(value)):
                if mask[i] == 'X':
                    continue
                else:
                    value[i] = mask[i]
            mem[addr] = int(''.join(value), 2)
    return reduce(lambda  a, b: a + b, mem.values())

def sol2(q):
    mem = []
    mem2 = {}
    mask = ""
    for p in q:
        if p.startswith("mask"):
            g = re.search("^mask = ([X10]{36})?", p)
            mask = g[1]
        else:
            g = re.search("^mem\[(\d+)\] = (\d+)?", p)
            addr = list(format(int(g[1]), '036b'))
            value = int(g[2])
            for i in range(len(addr)):
                if mask[i] != '0':
                    addr[i] = mask[i]
            mem.append((''.join(addr), value))

    for addr, v in mem:
        p = []
        diff = 0
        for i, b in enumerate(reversed(addr)):
            if b == 'X':
                if len(p) == 0:
                    p.append(diff)
                    p.append(2**i + diff)
                    diff = 0
                else:
                    for x in p.copy():
                        p.append(x + (2**i))
            elif b == '1':
                if len(p) == 0:
                    if i == 0:
                        diff = 1
                    else:
                        diff = diff + 2**i
                p = [ x + 2**i for x in p ]
        for a in p:
            mem2[a] = v    
    return reduce(lambda  a, b: a + b, mem2.values(), 0)

if __name__ == "__main__":
    q = readFileToList("input.txt")
    print(sol1(q))
    print(sol2(q))