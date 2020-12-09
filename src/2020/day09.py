from collections import deque

class Day09Solution:
    def __init__(self):
        file = open("day09.txt", "r")
        self.items = [int(line) for line in file.read().split("\n")]
    
    def partOne(self) -> int:
        q = deque()
        for i in range(0, 25):
            q.append(self.items[i])
        for i in range(25,len(self.items)):
            next = self.items[i]
            subs = [val for val in q if next - val in q]
            q.popleft()
            q.append(next)

            if subs:
                continue

            return next

    def partTwo(self) -> int:
        q = deque()
        x = self.partOne()
        for i in range(0, len(self.items)):
            while sum(q) + self.items[i] > x:
                q.popleft()

            q.append(self.items[i])
            if sum(q) == x:
                break
        return min(q) + max(q)

solution = Day09Solution()
print(solution.partOne())
print(solution.partTwo())
