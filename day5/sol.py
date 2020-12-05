def readFileToList(filename):
    f = open(filename, "r")    
    q = []
    inputs = f.readlines()
    for input in inputs:
        input = input.rstrip()
        row = input[:7]
        seat = input[-3:]
        q.append((row, seat))
    return q

def sol1(q):
    ids = []
    for row, seat in q:
        id = findRow(row,  0, 127) * 8 +  findSeat(seat, 0, 7)
        ids.append(id)
    return ids

def sol2(q):
    ids = sol1(q)
    ids.sort()
    st = ids[0]
    a = ids[0] & 1
    for x in ids:
        if (x & a) != a:
            if (x - 1) not in ids:
                return x - 1
        else:
            a = ~a & 1


def findRow(row,  frm, to):
    if len(row) == 0:
        return frm
    if row[0] == "F":
        return findRow(row[1:], frm, frm + int((to - frm) / 2))
    elif row[0] == "B":
        return findRow(row[1:], frm + int((to - frm)/2) + 1, to)
    
def findSeat(seat,  frm, to):
    if len(seat) == 0:
        return frm
    if seat[0] == "L":
        return findSeat(seat[1:], frm, frm + int((to - frm) / 2))
    elif seat[0] == "R":
        return findSeat(seat[1:], frm + int((to - frm)/2) + 1, to)

if __name__ == "__main__":
    q = readFileToList("input.txt")
    # BFFFBBFRRR: row 70, column 7, seat ID 567.
    # FFFBBBFRRR: row 14, column 7, seat ID 119.
    # BBFFBBFRLL: row 102, column 4, seat ID 820.
    # print(findRow("BFFFBBF",  0, 127) * 8 +  findSeat("RRR", 0, 7))
    # print(findRow("FFFBBBF", 0, 127) *  8 + findSeat("RRR",0, 7))
    # print(findRow("BBFFBBF", 0, 127) * 8 + findSeat("RLL",0, 7))
   
    print(max(sol1(q)))
    print(sol2(q))