def sol1(q):
    turn = len(q)
    rounds = q.copy()
    while True:
        if turn == 2020:
            break
        if rounds[turn - 1] not in rounds[:-1]:
            rounds.append(0)
        else:
            last_idx = max(i for i, item in enumerate(rounds[:-1]) if item == rounds[turn - 1])
            rounds.append(turn - last_idx - 1)

        turn = turn + 1
    return rounds[-1]

def sol2(q):
    turn = len(q)
    last_spoke = {}
    last_round = q[-1]
    for i, x in enumerate(q):
        last_spoke[x] = (-1, i)
    while True:
        if turn == 30000000:
            break
        l, c = last_spoke[last_round]
        if l == -1: #first time
            l0, c0 = last_spoke[0]
            last_spoke[0] = (c0, turn)
            last_round = 0
        else:
            diff = c - l
            try:
                ldiff, cdiff = last_spoke[diff]
                if ldiff == -1:
                    last_round = diff
                    last_spoke[last_round] = (cdiff, turn)
                else:
                    last_round = diff
                    last_spoke[last_round] = (cdiff, turn)
            except:
                last_spoke[diff] = (-1, turn)
                last_round = diff
        turn = turn + 1
    return last_round

if __name__ == "__main__":
    input = [9,3,1,0,8,4]
    testcase = [0, 3, 6]
    print(sol1(testcase))
    print(sol1(input))
    print(sol2(testcase))
    print(sol2(input))
