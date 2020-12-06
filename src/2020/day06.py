class Day06Solution:
    def __init__(self):
        file = open("day06.txt", "r")
        self.items = file.read().split("\n")
    
    def partOne(self) -> int:
        answers = [set()]
        for item in self.items:
            if not item:
                answers.append(set())
                continue
            answers[-1] = answers[-1].union([char for char in item])
        return sum([len(group) for group in answers])

    def partTwo(self) -> int:
        answers = [None]
        for item in self.items:
            if not item:
                answers.append(None)
                continue

            answer = [char for char in item]
            if answers[-1] is None:
                answers[-1] = set(answer)
            else:
                answers[-1] = answers[-1].intersection(answer)
        return sum([len(group) for group in answers])

solution = Day06Solution()
print(solution.partOne())
print(solution.partTwo())
