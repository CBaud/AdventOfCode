from collections import deque

class Day15Solution:
    def __init__(self):
        file = open("day15.txt", "r")
        self.items = [int(i) for i in file.read().split(",")]

    def partOne(self) -> int:
        items = deque(self.items)
        items.reverse()
        while len(items) < 2020:
            item = items.popleft()
            next = 0
            if item in items:
                next = items.index(item) + 1
            
            items.appendleft(item)
            items.appendleft(next)

        return items[0]

    def partTwo(self, goal: int = 30000000) -> int:
        seen = {}
        for index in range(0, len(self.items) - 1):
            seen[self.items[index]] = index
        
        index = len(self.items) - 1
        next = self.items[index]
        while index < (goal-1):
            if next in seen.keys():
                pos = seen[next]
                seen[next] = index
                next = index - pos
            else:
                seen[next] = index
                next = 0

            index += 1

        return next

solution = Day15Solution()
print(solution.partOne())
print(solution.partTwo())
