from typing import List

class Day11Solution:
    def __init__(self):
        file = open("day11.txt", "r")
        self.items = [[char for char in "." + line + "."] for line in file.read().split("\n")]
        self.items = [["." for char in self.items[0]]] + self.items + [["." for char in self.items[0]]]
        self.rows = len(self.items)-1
        self.cols = len(self.items[0])-1
    
    def partOne(self) -> int:
        count = -1
        pass2 = [[col for col in row] for row in self.items]
        while count != sum([row.count("#") for row in pass2]):
            count = sum([row.count("#") for row in pass2])
            pass1 = [[col for col in row] for row in pass2]
            for row in range(1, self.rows):
                for col in range(1, self.cols):
                    if pass2[row][col] == "." or pass2[row][col] == "#":
                        continue

                    hashes = 0
                    hashes += pass2[row-1][col-1:col+2].count("#")
                    hashes += pass2[row][col-1:col].count("#")
                    hashes += pass2[row][col+1:col+2].count("#")
                    hashes += pass2[row+1][col-1:col+2].count("#")
                    if hashes == 0:
                        pass1[row][col] = "#"
            pass2 = [[col for col in row] for row in pass1]
            for row in range(1, self.rows):
                for col in range(1, self.cols):
                    if pass1[row][col] == "." or pass1[row][col] == "L":
                        continue

                    hashes = 0
                    hashes += pass1[row-1][col-1:col+2].count("#")
                    hashes += pass1[row][col-1:col].count("#")
                    hashes += pass1[row][col+1:col+2].count("#")
                    hashes += pass1[row+1][col-1:col+2].count("#")
                    if hashes >= 4:
                        pass2[row][col] = "L"

        return count

    def partTwo(self) -> int:
        count = -1
        pass2 = [[col for col in row] for row in self.items]
        while count != sum([row.count("#") for row in pass2]):
            count = sum([row.count("#") for row in pass2])
            pass1 = [[col for col in row] for row in pass2]
            for row in range(1, self.rows):
                for col in range(1, self.cols):
                    if pass2[row][col] == "." or pass2[row][col] == "#":
                        continue

                    hashes = ["." for dot in range(0,8)]
                    for delta in range(1, max(self.rows, self.cols)):
                        # northwest
                        if hashes[0] == "." and row - delta > 0 and col - delta > 0 and pass2[row-delta][col-delta] != ".":
                            hashes[0] = pass2[row-delta][col-delta]

                        # north
                        if hashes[1] == "." and row - delta > 0 and pass2[row-delta][col] != ".":
                            hashes[1] = pass2[row-delta][col]
                        
                        # northeast
                        if hashes[2] == "." and row - delta > 0 and col + delta < self.cols and pass2[row-delta][col+delta] != ".":
                            hashes[2] = pass2[row-delta][col+delta]
                        
                        # east
                        if hashes[3] == "." and col + delta < self.cols and pass2[row][col+delta] != ".":
                            hashes[3] = pass2[row][col+delta]
                        
                        # southeast
                        if hashes[4] == "." and row + delta < self.rows and col + delta < self.cols and pass2[row+delta][col+delta] != ".":
                            hashes[4] = pass2[row+delta][col+delta]

                        # south
                        if hashes[5] == "." and row + delta < self.rows and pass2[row+delta][col] != ".":
                            hashes[5] = pass2[row+delta][col]

                        # southwest
                        if hashes[6] == "." and row + delta < self.rows and col - delta > 0 and pass2[row+delta][col-delta] != ".":
                            hashes[6] = pass2[row+delta][col-delta]

                        # west
                        if hashes[7] == "." and col - delta > 0 and pass2[row][col-delta] != ".":
                            hashes[7] = pass2[row][col-delta]
                    
                    if hashes.count("#") == 0:
                        pass1[row][col] = "#"

            pass2 = [[col for col in row] for row in pass1]
            for row in range(1, self.rows):
                for col in range(1, self.cols):
                    if pass1[row][col] == "." or pass1[row][col] == "L":
                        continue

                    hashes = ["." for dot in range(0,8)]
                    for delta in range(1, max(self.rows, self.cols)):
                        # northwest
                        if hashes[0] == "." and row - delta > 0 and col - delta > 0 and pass1[row-delta][col-delta] != ".":
                            hashes[0] = pass1[row-delta][col-delta]

                        # north
                        if hashes[1] == "." and row - delta > 0 and pass1[row-delta][col] != ".":
                            hashes[1] = pass1[row-delta][col]
                        
                        # northeast
                        if hashes[2] == "." and row - delta > 0 and col + delta < self.cols and pass1[row-delta][col+delta] != ".":
                            hashes[2] = pass1[row-delta][col+delta]
                        
                        # east
                        if hashes[3] == "." and col + delta < self.cols and pass1[row][col+delta] != ".":
                            hashes[3] = pass1[row][col+delta]
                        
                        # southeast
                        if hashes[4] == "." and row + delta < self.rows and col + delta < self.cols and pass1[row+delta][col+delta] != ".":
                            hashes[4] = pass1[row+delta][col+delta]

                        # south
                        if hashes[5] == "." and row + delta < self.rows and pass1[row+delta][col] != ".":
                            hashes[5] = pass1[row+delta][col]

                        # southwest
                        if hashes[6] == "." and row + delta < self.rows and col - delta > 0 and pass1[row+delta][col-delta] != ".":
                            hashes[6] = pass1[row+delta][col-delta]

                        # west
                        if hashes[7] == "." and col - delta > 0 and pass1[row][col-delta] != ".":
                            hashes[7] = pass1[row][col-delta]
                    
                    if hashes.count("#") >= 5:
                        pass2[row][col] = "L"

        return count

solution = Day11Solution()
print(solution.partOne())
print(solution.partTwo())
