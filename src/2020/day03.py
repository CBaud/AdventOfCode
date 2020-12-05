class Day03Solution:
    def __init__(self):
        file = open("day03.txt", "r")
        self.items = file.read().split("\n")

    def partOne(self, slide=3, drop=1) -> int:
        count = 0
        col = 0
        for row in range(0, len(self.items), drop):
            if col >= len(self.items[row]):
                col %= len(self.items[row])
            
            if self.items[row][col] == "#":
                count += 1
            
            col += slide

        return count

    def partTwo(self) -> int:
        count = self.partOne(1, 2)
        for slide in range(1, 8, 2):
            count *= self.partOne(slide)

        return count

solution = Day03Solution()
print(solution.partOne())
print(solution.partTwo())
