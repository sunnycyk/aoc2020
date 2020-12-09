import itertools

def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    q = []
    for input in inputs:
        q.append(int(input))
    return q

def calwindow(q, pl):
    w = []
    for i, x in enumerate(q[:pl]):
        sum = []
        for y in q[:i]:
            sum.append(x + y)
        w.append(sum)
    return w

def fn(q, pl):
    w = calwindow(q, pl)
    for i, x in enumerate(q[pl:]):
        a = list(itertools.chain.from_iterable(w))
        if x in a:
            w = calwindow(q[i + 1:], pl)
        else:
            return x

def fn2(q, pl, invalid):
    i = 0
    j = 1
    s = q[0]
    while True:
        s = s + q[j]
        while s > invalid:
            s = s - q[i]
            i = i + 1
        if s == invalid:
            return q[i:j]
        j = j + 1



def sol1(q):
    return fn(q, 25)

def sol2(q, pl, invalid):
    result = fn2(q, pl, invalid)
    return max(result) + min(result)

if __name__ == "__main__":
    q = readFileToList("input.txt")
    invalid = sol1(q)
    print(invalid)
    print(sol2(q, 25, invalid))