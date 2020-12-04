class Day01Solution:
    def __init__(self):
        file = open("day01.txt", "r")
        self.items = [int(line) for line in set(file.read().split("\n"))]

    def partOne(self, total=2020) -> int:
        for item in self.items:
            if total - item in self.items:
                return item * (total - item)
        
        return None

    def partTwo(self) -> int:
        for item in self.items:
            result = self.partOne(2020 - item)
            if result:
                return item * result
        
        return None
            

solution = Day01Solution()
print(solution.partOne())
print(solution.partTwo())