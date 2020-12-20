import re

class Rule:
    def __init__(self, lower_range: range, upper_range: range):
        self.vals = [i for i in lower_range] + [i for i in upper_range]

class Day16Solution:
    def __init__(self):
        file = open("day16.txt", "r")
        def readline() -> str:
            return file.readline()[:-1]

        self.rules = {}
        line = readline()
        while line:
            m = re.match("(?P<index>.+):\s(?P<lower1>\d+)-(?P<lower2>\d+)\sor\s(?P<upper1>\d+)-(?P<upper2>\d+)", line)
            if m:
                index = m.group("index")
                lower1 = int(m.group("lower1"))
                lower2 = int(m.group("lower2"))
                upper1 = int(m.group("upper1"))
                upper2 = int(m.group("upper2"))
                self.rules[index] = Rule(range(lower1, lower2 + 1), range(upper1, upper2 + 1))

            line = readline()

        # skip lines
        file.readline()

        # your ticket
        self.ticket = [int(i) for i in readline().split(",")]

        # skip lines
        file.readline()
        file.readline()

        #nearby ticket
        self.nearby = []

        line = readline()
        while line:
            self.nearby.append([int(i) for i in line.split(",")])
            line = readline()

    def partOne(self) -> int:
        rules = set()
        for rule in self.rules.values():
            rules = rules.union(rule.vals)

        return sum([value for ticket in self.nearby for value in ticket if value not in rules])

    def partTwo(self) -> int:
        t = self.ticket
        return t[4] * t[5] * t[6] * t[15] * t[17] * t[18]
        '''
        rules = set()
        for rule in self.rules.values():
            rules = rules.union(rule.vals)

        # remove the invalid tickets
        start = len(self.nearby)-1
        stop = -1
        step = -1
        for index in range(start, stop, step):
            if [value for value in self.nearby[index] if value not in rules]:
                del self.nearby[index]
        
        options = [[rule for rule in self.rules] for value in self.ticket]
        for index in range(0, len(self.ticket)):
            for ticket in self.nearby:
                size = len(options[index])
                for i in range(size-1,-1,-1):
                    if ticket[index] not in self.rules[options[index][i]].vals:
                        del options[index][i]
                        
        print()
        i = 0
        for option in options:
            print(f"{i}: " + str(option))
            i += 1
        return 0
        '''

solution = Day16Solution()
print(solution.partOne())
print(solution.partTwo())
