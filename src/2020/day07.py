from collections import deque
from collections import namedtuple
import re

class Day07Solution:
    def __init__(self):
        Color = namedtuple("Color", ["colors", "counts"])
        file = open("day07.txt", "r")
        self.items = {re.match("(?P<key>.+) bags contain ", line).group("key"): Color(re.findall("\d+ (?P<value>\D+) bag\D+", line), [int(quantity) for quantity in re.findall("\d+", line) if quantity]) for line in file.read().split("\n")}
    
    def partOne(self, color="shiny gold") -> int:
        bags = set()
        inspect = deque([color])
        while inspect:
            bag = inspect.popleft()
            for key in self.items:
                if bag in self.items[key].colors and key not in bags:
                    bags.add(key)
                    inspect.append(key)

        return len(bags)

    def partTwo(self, color="shiny gold") -> int:
        def getCount(key: str) -> int:
            count = 0
            for index in range(0, len(self.items[key].colors)):
                count += self.items[key].counts[index]
                count += (self.items[key].counts[index] * getCount(self.items[key].colors[index]))
                
            return count

        return getCount(color)

solution = Day07Solution()
print(solution.partOne())
print(solution.partTwo())
