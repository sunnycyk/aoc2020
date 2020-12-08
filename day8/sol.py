
OPS = {
    'nop' : 0,
    'jmp' : 1,
    'acc' : 2
}


def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    instrs = []
    for input in inputs:
        op, arg = input.split(" ")
        incdec = arg[0]
        value = int(arg[1:])
        instrs.append([OPS[op], incdec, value])
    return instrs

class Console(object):
    def __init__(self, instrs=None):
        self.ptr = 0
        self.accumulator = 0
        self.mem = []
        if instrs == None:
            instrs = []
        self.instrs = instrs

    def play(self):
        while self.ptr < len(self.instrs):
            if self.ptr in self.mem: # infintite loop detection
                break
            self.mem.append(self.ptr)
            instr, op, v = self.instrs[self.ptr]
            if instr == 0:
                self.nop(op, v)
            elif instr == 1:
                self.jmp(op, v)
            elif instr == 2:
                self.acc(op, v)

    def playWithFix(self):
        testInstr = []
        lastFixPtr = -1
        while self.ptr < len(self.instrs):
            if self.ptr in self.mem:
                self.ptr = 0
                self.accumulator = 0
                lastFixPtr = -1
                self.mem = []
                continue
            self.mem.append(self.ptr)
            instr, op, v = self.instrs[self.ptr]
            if instr == 0:
                if lastFixPtr == -1 and self.ptr not in testInstr:
                    testInstr.append(self.ptr)
                    lastFixPtr = self.ptr
                    self.jmp(op, v)
                else:
                    self.nop(op, v)
            elif instr == 1:
                if lastFixPtr == -1 and self.ptr not in testInstr:
                    testInstr.append(self.ptr)
                    lastFixPtr = self.ptr
                    self.nop(op, v)
                else:
                    self.jmp(op, v)
            elif instr == 2:
                self.acc(op, v)

    def nop(self, op, v):
        self.ptr = self.ptr + 1

    def jmp(self, op, v):
        if op == "+":
            self.ptr = self.ptr + v
        else:
            self.ptr = self.ptr - v

    def acc(self, op, v):
        if op == "+":
            self.accumulator = self.accumulator + v
        else:
            self.accumulator = self.accumulator - v
        self.ptr = self.ptr + 1


def clearmem(q):
    for instr in q:
        instr[2] = []               

def sol1(q):
    console = Console(q)
    console.play()
    return console.accumulator
    

def sol2(q):
    console = Console(q)
    console.playWithFix()
    return console.accumulator

if __name__ == "__main__":
    q = readFileToList("input.txt")
    print(sol1(q))
    print(sol2(q))

    