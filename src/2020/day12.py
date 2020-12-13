from collections import deque
import re

class Instruction:
    def __init__(self, instruction: str):
        m = re.match("(?P<act>[NSEWLRF])(?P<val>\d+)", instruction)
        self.act = m.group("act")
        self.val = int(m.group("val"))

class Day12Solution:
    def __init__(self):
        file = open("day12.txt", "r")
        self.items = [Instruction(line) for line in file.read().split("\n")]
    
    def partOne(self) -> int:
        dir = deque(["E", "S", "W", "N"])
        lat = 0
        lon = 0
        for item in self.items:
            act = item.act
            if act == "F":
                act = dir[0]

            if act == "N":
                lat += item.val
            elif act == "S":
                lat -= item.val
            elif act == "E":
                lon += item.val
            elif act == "W":
                lon -= item.val
            elif act == "R":
                for iteration in range(0, int(item.val / 90)):
                    dir.append(dir.popleft())
            elif act == "L":
                for iteration in range(0, int(item.val / 90)):
                    dir.appendleft(dir.pop())


        return abs(lat) + abs(lon)

    def partTwo(self) -> int:
        lat = 1
        lon = 10
        ship_lat = 0
        ship_lon = 0
        for item in self.items:
            if item.act == "F":
                ship_lat += (item.val * lat)
                ship_lon += (item.val * lon)
            elif item.act == "N":
                lat += item.val
            elif item.act == "S":
                lat -= item.val
            elif item.act == "E":
                lon += item.val
            elif  item.act == "W":
                lon -= item.val
            elif item.act == "R":
                for iteration in range(0, int(item.val / 90)):
                    tmp = lon
                    lon = lat
                    lat = -tmp
            elif item.act == "L":
                for iteration in range(0, int(item.val / 90)):
                    tmp = lat
                    lat = lon
                    lon = -tmp

        return abs(ship_lat) + abs(ship_lon)

solution = Day12Solution()
print(solution.partOne())
print(solution.partTwo())
