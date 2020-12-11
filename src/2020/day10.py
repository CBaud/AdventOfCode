from typing import List

class Day10Solution:
    def __init__(self):
        file = open("day10.txt", "r")
        self.items = [0] + [int(i) for i in file.read().split("\n")]
        self.items += [max(self.items) + 3]
    
    def partOne(self) -> int:
        one = 0
        three = 0
        items = [i for i in set(self.items)]
        for i in range(0, len(items) - 1):
            diff = items[i+1] - items[i]
            if diff == 1:
                one += 1
            elif diff == 3:
                three += 1

        return one * three

    def partTwo(self) -> int:
        count = 0
        items = [i for i in set(self.items)]
        for i in range(0, len(items)):
            if i == len(items)-1:
                items[i] = 1
                continue

            for j in range(i+3, i, -1):
                if j >= len(items):
                    continue
                if items[j]-items[i] <= 3:
                    items[i] = j-i
                    break
        
        paths = 1
        stack = []
        for item in items:
            if item > 1:
                stack.append(item)
                continue

            if stack and len(stack) == 1:
                paths *= sum(stack)
                stack = []
            elif stack:
                paths *= (sum(stack)-1)
                stack = []
        
        return paths

solution = Day10Solution()
print(solution.partOne())
print(solution.partTwo())
