import re
def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    r = {}
    allgen = set()
    all = []
    for input in inputs:
        ing, allg = input.split("(contains")
        allg = set(allg.replace(")", "").replace(" ", "").split(","))
        ing = set(ing.rstrip().split(" "))
        for name in allg:
            if name in r.keys():
                r[name] = r[name].intersection(ing)
            else:
                r[name] = ing
            allgen.add(name)
        all.append(ing)
    
    return r, allgen, all      

from functools import reduce
def sol1(r, allgen, all):
    while True:
        if (len([v for k, v in r.items() if len(v) != 1 ]) == 0):
            break
        found = [v for k, v in r.items() if len(v) == 1]
        for k, v in r.items():
            for f in found:
                if v == f:
                    continue
                r[k] = r[k] - f
    alg = reduce(lambda a, b: a.union(b), r.values(), set())
    print(alg)
    total = 0
    for i in all:
        total += len(i - alg)
    return total



def sol2(r, allgen, all):
    while True:
        if (len([v for k, v in r.items() if len(v) != 1 ]) == 0):
            break
        found = [v for k, v in r.items() if len(v) == 1]
        for k, v in r.items():
            for f in found:
                if v == f:
                    continue
                r[k] = r[k] - f
    al = [n for n in r.keys()]
    al = sorted(al)


    return reduce(lambda a,b: a + "," + list(r[b])[0], al[1:], list(r[al[0]])[0])


if __name__ == "__main__":
    r, allgen, all = readFileToList("input.txt")
    print(sol1(r, allgen, all))
    print(sol2(r, allgen, all))