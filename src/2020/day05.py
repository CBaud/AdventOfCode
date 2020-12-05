from typing import Set

class Day05Solution:
    def __init__(self):
        file = open("day05.txt", "r")
        self.items = file.read().split("\n")
    
    def partOne(self) -> Set[int]:
        ids = set()
        for item in self.items:
            row = 0
            for i in range (6, -1, -1):
                if item[6-i] == "B":
                    row += 2**i
            col = 0
            for i in range(2, -1, -1):
                if item[9-i] == "R":
                    col += 2**i
            ids.add(row * 8 + col)

        return ids

    def partTwo(self) -> int:
        seats = self.partOne()
        seat, = (seat for seat in range(min(seats), max(seats)) if seat not in seats)
        return seat

solution = Day05Solution()
print(max(solution.partOne()))
print(solution.partTwo())
