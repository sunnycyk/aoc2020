import re
def readFileToList(filename):
    f = open(filename, "r")    
    q = []
    inputs = f.read().split("\n\n")
    p = {}
    for input in inputs:
        attrs = input.replace("\n", " ").split(" ")
        for attr in attrs: 
            k, v = attr.split(":")
            p[k] = v
        q.append(p)
        p = {}

    return q

def sol1(q):
    valid = []
    validFields = set(("byr","iyr","eyr","hgt","hcl","ecl", "pid"))
    for p in q:
        entry = set(p.keys())
        y = validFields - entry
        if len(y) == 0:
            valid.append(p)
    return valid


def sol2(q):
    vp = sol1(q)
    valid = filter(lambda p: validPid(p["pid"]) and validEcl(p["ecl"]) and validHcl(p["hcl"]) and validHgt(p["hgt"]) and validEyr(int(p["eyr"])) and validByr(int(p["byr"])) and validIyr(int(p["iyr"])), vp)
    return list(valid)

def validHgt(input):
    u = input[-2:]
    if u == "cm":
        h = int(input.replace(u, ""))
        return h >= 150 and h <= 193
    elif u == "in":
        h = int(input.replace(u, ""))
        return h >= 59 and h <= 76
    return False

def validPid(input):
    return re.search("^\d{9}$", input) != None

def validEcl(input):
    return input in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validHcl(input):
    return re.search("^#[0-9a-f]{6}$", input) != None

def validByr(input):
    return input >= 1920 and input <= 2002

def validIyr(input):
    return input >= 2010 and input <= 2020

def validEyr(input):
    return input >= 2020 and input <= 2030

if __name__ == "__main__":
    q = readFileToList("input.txt")
    print(len(sol1(q)))
    print(len(sol2(q)))
