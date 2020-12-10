
def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    q = []
    for input in inputs:
        q.append(int(input))
    q.sort()
    return q

def sol1(q):
    oneDiff = []
    threeDiff = []
    currX = 0
    for i, x in enumerate(q):
        testX = min(filter(lambda a: a <= currX + 3, q[i:]))
        diff = testX - currX
        if diff == 1:
            oneDiff.append(testX)
        elif diff == 3:
            threeDiff.append(testX)
        currX = testX
    # return len(oneDiff) * (len(threeDiff) + 1)
    return (oneDiff, threeDiff)


def sol2(one, three):
    f = 0
    last = max([max(one), max(three)]) + 3
    i = 0
    order = 1
    while True:
        if i == len(three):
            e = last
        else:
            e = three[i]
        l = 0
        for x in one:
            if x < e and x > f:
                l = l + 1
        if l == 4:
            order = order * 7
        elif l == 3:
            order = order * 4
        elif l == 2:
            order = order * 2

        i = i + 1
        f = e
        if f == last:
            break
        
        


    return order

if __name__ == "__main__":
    q = readFileToList("input.txt")
    one, three = sol1(q)
    print(len(one) * (len(three) + 1))
    print(sol2(one, three))
