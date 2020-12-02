def readFileToList(filename):
    f = open(filename, "r")    
    q = []
    lines = f.readlines()
    for line in lines:
        occur, target, password = line.rstrip().split(" ")
        frm, to = map(int, occur.split("-"))
        q.append((frm, to, target[:-1], list(password)))
    return q

def sol1(input):
    valid = 0
    for frm, to, target, password in input:
        n = password.count(target)
        if n >= frm and n <= to:
            valid = valid + 1
    print(valid)

def sol2(input):
    valid = 0
    for frm, to, target, p in input:
        if p[frm - 1] != p[to - 1] and (p[frm - 1] == target or p[to - 1] == target):
            valid = valid + 1
    print(valid)

if __name__ == "__main__":
    a = readFileToList("input.txt")
    
    sol1(a)
    sol2(a)
