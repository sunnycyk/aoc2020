from functools import reduce

def readFileToList(filename):
    f = open(filename, "r")    
    q = []
    inputs = f.read().split("\n\n")
    for input in inputs:
        grp = set(input.replace("\n", " ").replace(" ", ""))
        q.append(grp)
    return q
        
def readFileforSol2(filename):
    f = open(filename, "r")    
    q = []
    inputs = f.read().split("\n\n")
    for input in inputs:
        q.append(input.split("\n"))
    return q
    
        

def sol1(q):
    return reduce(lambda a, b: a + b, map(lambda a: len(a), q))

def sol2(q):
    yesgrp = []
    for grp in q:
        yes = set(grp[0])
        for ind in grp[1:]:
            yes = yes.intersection(set(ind))
        yesgrp.append(yes)
    return reduce(lambda a, b: a + b, map(len, yesgrp))

if __name__ == "__main__":
    q = readFileToList("input.txt")
    print(sol1(q))
    q = readFileforSol2("input.txt")
    print(sol2(q))