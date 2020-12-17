import re

class Day13Solution:
    def __init__(self):
        file = open("day13.txt", "r")
        self.start = int(file.readline())
        line = file.readline()
        self.buses = [int(i) for i in re.findall("(?P<num>\d+)", line)]
        self.items = line.split(",")
    
    def partOne(self) -> int:
        wait = self.start
        result = 0
        for bus in self.buses:
            next = bus - (self.start % bus)
            if next < wait:
                wait = next
                result = wait * bus
        return result

    def partTwo(self) -> int:
        items = {}
        for index in range(0,len(self.items)):
            if self.items[index] == "x":
                continue
            items[index] = int(self.items[index])

        x = 118889450154
        result = 0
        while not result:
            x += 161028941683
            for index in items:
                if (x + index) % items[index] != 0:
                    break
                if index == len(self.items)-1:
                    result = x

        return result

solution = Day13Solution()
print(solution.partOne())
print(solution.partTwo())
