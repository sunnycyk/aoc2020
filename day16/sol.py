import numpy as np


def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    fields = {}
    section = 0
    myticket = []
    nearbytickets = []
    for input in inputs:
        if len(input) == 0:
            section += 1
            continue
        if section == 0:
            classname, validRange = input.split(":")
            r1, r2 = validRange.split(" or ")
            a, b = r1.split("-")
            x, y = r2.split("-")
            fields[classname] = [*range(int(a), int(b) + 1)] + [*range(int(x), int(y) + 1)]
        elif section == 1:
            if input == "your ticket:":
                continue
            myticket = list(map(int, input.split(",")))
        else:
            if input == "nearby tickets:":
                continue
            ticket = list(map(int, input.split(",")))
            nearbytickets.append(ticket)

    return fields, myticket, nearbytickets

def removeInvalid(fields, nearby):
    valid = nearby.copy()
    for t in nearby:
        found = False
        for f in t:
            found = False
            for k in fields.keys():
                if f in fields[k]:
                    found = True
                    break
            if found:
                continue
            valid.remove(t)
    return valid

def sol1(fields, myticket, nearby):
    invalid = []
    for t in nearby:
        found = False
        for f in t:
            found = False
            for k in fields.keys():
                if f in fields[k]:
                    found = True
                    break
            if found:
                continue
            invalid.append(f)

    return sum(invalid)

def sol2(fields, myticket, nearby):
    valid = removeInvalid(fields, nearby)
    valid.append(myticket)
    # reconstruct
    
    m = [ [] for x in fields.keys()]
    for i, t in enumerate(valid):
        for j in range(len(m)):
            m[j].append(t[j])
    m = { i: set(x) for i, x in enumerate(m) }
    result = {}
    
    while len(fields) != 0:
        d = { x: [] for x in fields.keys() }
        for k in fields.keys():
            for i, m1 in enumerate(m.keys()):
                s = m[m1] - set(fields[k])
                if len(s) == 0:
                    d[k].append(m1)
        for k in d.keys():
            if k in fields and len(d[k]) == 1:
                del fields[k]
                result[k] = d[k][0]
                del m[result[k]]
    return myticket[result['departure location']] * myticket[result['departure station']] * myticket[result['departure platform']]  * myticket[result['departure track']]  * myticket[result['departure date']] * myticket[result['departure time']]    


if __name__ == "__main__":
    field, myticket, nearby = readFileToList("input.txt")
    print(sol1(field, myticket, nearby))
    print(sol2(field, myticket, nearby))