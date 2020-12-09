import re

class Day08Solution:
    def __init__(self):
        file = open("day08.txt", "r")
        self.items = file.read().split("\n")
    
    def partOne(self) -> int:
        acc = 0
        pos = 0
        vis = set()
        while pos not in vis:
            vis.add(pos)

            m = re.match("(?P<ins>\w{3})\s(?P<sign>\D)(?P<val>\d+)", self.items[pos])
            ins = m.group("ins")
            isNegative = bool(m.group("sign") == "-")
            val = int(m.group("val"))

            if ins == "acc":
                pos += 1
                if isNegative:
                    acc -= val
                else:
                    acc += val

            if ins == "jmp":
                if isNegative:
                    pos -= val
                else:
                    pos += val

            if ins == "nop":
                pos += 1

        return acc

    def partTwo(self) -> int:
        acc = 0
        swp = set()
        while True:
            acc = 0
            pos = 0
            vis = set()
            canSwap = True
            while pos not in vis and pos < len(self.items):
                vis.add(pos)

                m = re.match("(?P<ins>\w{3})\s(?P<sign>\D)(?P<val>\d+)", self.items[pos])
                ins = m.group("ins")
                isNegative = bool(m.group("sign") == "-")
                val = int(m.group("val"))

                if ins == "acc":
                    pos += 1
                    if isNegative:
                        acc -= val
                    else:
                        acc += val

                if ins == "jmp":
                    if pos not in swp and canSwap:
                        canSwap = False
                        swp.add(pos)
                        
                        # simulate nop
                        pos += 1
                        continue

                    if isNegative:
                        pos -= val
                    else:
                        pos += val

                if ins == "nop":
                    if pos not in swp and canSwap:
                        canSwap = False
                        swp.add(pos)

                        #simulate jmp
                        if isNegative:
                            pos -= val
                        else:
                            pos += val
                        continue

                    pos += 1

            if pos == len(self.items):
                break
        return acc

solution = Day08Solution()
print(solution.partOne())
print(solution.partTwo())
