class Day17Solution:
    def __init__(self):
        file = open("day17.txt", "r")
        self.items = [[char for char in line] for line in file.read().split("\n")]

    def partOne(self) -> int:
        factor = 2
        height = len(self.items)
        width = len(self.items[0])
        state = []
        for slice in range(-width * factor, width * factor):
            if slice:
                state += [[[False for col in range(-width * factor, width * factor)] for row in range(-height * factor, height * factor)]]
            else:
                state += [[[bool(col >= 0 and col < width and row >= 0 and row < height and self.items[row][col] == "#") for col in range(-width * factor,width * factor)] for row in range(-height * factor, height * factor)]]

        size = len(state)
        for cycle in range(6):
            print(f"Cycle {cycle}")
            curr = [[state[slice][row].copy() for row in range(0, size)] for slice in range(0, size)]
            for slice in range(1, size-1):
                for row in range(1, size-1):
                    for col in range(1, size-1):
                        adjacent = sum([1 for s in range(slice-1,slice+2) for r in range(row-1, row+2) for c in range(col-1,col+2) if (curr[s][r][c] and not (s == slice and r == row and c == col))])
                        state[slice][row][col] = bool(adjacent == 3 or (curr[slice][row][col] and adjacent == 2))

        return sum([row.count(True) for slice in state for row in slice])

    def partTwo(self) -> int:
        factor = 3
        height = len(self.items)
        width = len(self.items[0])
        state = []
        for cube in range(-width * factor, width * factor):
            hypercube = []
            for slice in range(-width * factor, width * factor):
                if cube or slice:
                    hypercube += [[[False for col in range(-width * factor, width * factor)] for row in range(-height * factor, height * factor)]]
                else:
                    hypercube += [[[bool(col >= 0 and col < width and row >= 0 and row < height and self.items[row][col] == "#") for col in range(-width * factor,width * factor)] for row in range(-height * factor, height * factor)]]
            state.append(hypercube)

        changed = []
        size = len(state)
        for cycle in range(6):
            print(f"Cycle {cycle}")
            if changed:
                for h,s,r,c in changed:
                    curr[h][s][r][c] = state[h][s][r][c]
            else:
                curr = [[[state[cube][slice][row].copy() for row in range(0, size)] for slice in range(0, size)] for cube in range(0, size)]

            for cube in range(1, size-1):
                for slice in range(1, size-1):
                    for row in range(1, size-1):
                        for col in range(1, size-1):
                            adjacent = sum([1 for h in range(cube-1,cube+2) for s in range(slice-1,slice+2) for r in range(row-1, row+2) for c in range(col-1,col+2) if (curr[h][s][r][c] and not (h == cube and s == slice and r == row and c == col))])
                            state[cube][slice][row][col] = bool(adjacent == 3 or (curr[cube][slice][row][col] and adjacent == 2))

                            if curr[cube][slice][row][col] != state[cube][slice][row][col]:
                                changed.append((cube,slice,row,col))

        return sum([row.count(True) for cube in state for slice in cube for row in slice])

solution = Day17Solution()
print(solution.partOne())
print(solution.partTwo())
