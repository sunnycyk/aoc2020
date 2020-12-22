import re
def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    p1 = Player()
    p2 = Player()
    player = 1
    for input in inputs:
        if input == "Player 1:":
            player = 1
            continue
        if input == "Player 2:":
            player = 2
            continue
        if input == "":
            continue
        if player == 1:
            p1.addCard(int(input))
        else:
            p2.addCard(int(input))
    return (p1, p2)

class Player(object):
    def __init__(self):
        self.cards = []

    def nextRound(self): 
        card = self.cards[0]
        self.cards = self.cards[1:]
        return card

    def addCard(self, card):
        self.cards.append(card)

    def __str__(self):
        return self.cards.__str__()

    def gameOver(self):
        return len(self.cards) == 0

    def hash(self):
        s = ','.join(map(str, self.cards))
        return s
            

def sol1(p1, p2):
    while not p1.gameOver() and not p2.gameOver():
        c1 = p1.nextRound()
        c2 = p2.nextRound()
        if c1 > c2:
            print("p1 win")
            p1.addCard(c1)
            p1.addCard(c2)
        else:
            print("p2 win")
            p2.addCard(c2)
            p2.addCard(c1)
    winner = []
    if p1.gameOver():
        winner = p2.cards.copy()
    else:
        winner = p1.cards.copy()
    winner.reverse()
    k = sum([x * (i + 1) for i, x in enumerate(winner)])
    return k

class RecusiveComabt(object):
    def __init__(self, p1, p2, subgame = False):
        self.p1 = p1
        self.p2 = p2
        self.history = []
        self.subgame = False

    def inHistory(self):
        s = self.p1.hash() + " " + self.p2.hash()
        if s in self.history:
            return True
        return False

    def addHistory(self):
        s = self.p1.hash() + " " + self.p2.hash()
        self.history.append(s)
 

    def play(self):
        round = 0
        while not self.p1.gameOver() and not self.p2.gameOver():
            # print("round" + str(round))
            # print(self.p1.cards, self.p2.cards)
            if self.inHistory():
                #
                return 1
            else:
                self.addHistory()
            c1 = self.p1.nextRound()
            c2 = self.p2.nextRound()
            # print(c1, self.p1.cards, c2, self.p2.cards)
            if (c1 <= len(self.p1.cards) and c2 <= len(self.p2.cards)):
                p1 = Player()
                p2 = Player()
                p1.cards = self.p1.cards[0:c1]
                p2.cards = self.p2.cards[0:c2]
                subgame = RecusiveComabt(p1, p2, True)
                # print("enter subgame")
                result = subgame.play()
                    
                if result == 1:
                    # print("p1 win")
                    self.p1.addCard(c1)
                    self.p1.addCard(c2)
                elif result == 2:
                    # print("p2 win")
                    self.p2.addCard(c2)
                    self.p2.addCard(c1)
            elif c1 > c2:
                # print("p1 win")
                self.p1.addCard(c1)
                self.p1.addCard(c2)
            else:
                # print("p2 win")
                self.p2.addCard(c2)
                self.p2.addCard(c1)
            round += 1
        if self.p1.gameOver():
            # print("p2 win")
            return 2
        else:
            # print("p1 win")
            return 1

def sol2(p1, p2):
    game = RecusiveComabt(p1, p2)
    winner = []
    result = game.play()
    if result == 1:
        winner = p1.cards.copy()
    else:
        winner = p2.cards.copy()
    # print(winner)
    winner.reverse()
    k = sum([x * (i + 1) for i, x in enumerate(winner)])
    return k

if __name__ == "__main__":
    p1, p2 = readFileToList("input.txt")
    # print(sol1(p1, p2))
    p1, p2 = readFileToList("input.txt")
    print(sol2(p1, p2))
    # p1, p2 = readFileToList("testcase2.txt")
    # print(play2(p1.cards, p2.cards))


    