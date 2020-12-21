import regex as re
def readFileToList(filename):
    f = open(filename, "r")    
    inputs = f.read().split("\n")
    rules = {}
    msg = []
    checkRule = True
    for input in inputs:
        if len(input) == 0:
            checkRule = False
            continue
        if checkRule:
            x = input.split(": ")
            rules[x[0]] = x[1]
        else:
            msg.append(input)
    return rules, msg


class Rules(object):
    def __init__(self, rules):
        self.rules = rules
        self.d = {}

    def getRule(self, n):
        r = self.rules[n]
        s = ''
        if r == '"a"':
            return 'a'
        if r == '"b"':
            return 'b'
        s += '('
        for cond in r.split(" "):
            if cond.isdigit():
                s += self.getRule(cond)
            elif cond == "|":
                s += '|'
        s += ')'
        return s

    def getRule2(self, n):
        r = self.rules[n]
        s = ''
        if r == '"a"':
            return 'a'
        if r == '"b"':
            return 'b'
        if n == '8':
            return "(" + self.getRule2('42') + ")+" 
        if n == '11':
            return "(?P<X>" + self.getRule2('42') + "(?&X)?" + self.getRule2('31') + ")"
        s += '('
        for cond in r.split(" "):
            if cond.isdigit():
                s += self.getRule2(cond)
            elif cond == "|":
                s += '|'
        s += ')'
        return s

def f1(rules):
    return Rules(rules)
        

def sol1(rules, msg):
    r = f1(rules)
    total = 0
    regex = re.compile("^{}$".format(r.getRule('0')))
    for m in msg:
        if regex.match(m) != None:
            total += 1
    return total

def sol2(rules, msg):
    r = f1(rules)
    total = 0
    regex = re.compile("^{}$".format(r.getRule2('0')))
    for m in msg:
        if regex.match(m) != None:
            total += 1
    return total

if __name__ == "__main__":
    rules, msg = readFileToList("input.txt")
    print(sol1(rules, msg))
    print(sol2(rules, msg))
