import re

class Instruction:
    def __init__(self, string: str):
        m = re.match("mask\s+=\s+(?P<value>\w+)", string)
        self.mask = str()
        if m:
            self.mask = m.group("value")
        
        m = re.match("mem\[(?P<index>\d+)\]\s+=\s+(?P<value>\d+)", string)
        if m:
            self.index = int(m.group("index"))
            self.value = int(m.group("value"))

class Day14Solution:
    def __init__(self):
        file = open("day14.txt", "r")
        self.instructions = [Instruction(line) for line in file.read().split("\n")]
    
    def partOne(self) -> int:
        mem = {}
        mask = str()
        for ins in self.instructions:
            if ins.mask:
                mask = ins.mask
            else:
                value = ins.value | int(mask.replace("X", "0"), 2)
                value = value & int(mask.replace("X", "1"), 2)
                mem[ins.index] = value

        return sum(mem.values())

    def partTwo(self) -> int:
        mem = {}
        mask = str()
        for ins in self.instructions:
            if ins.mask:
                mask = ins.mask
            else:
                x = [index for index in range(0, len(mask)) if mask[index] == "X"]
                masks = []
                for val in range(0,2**len(x)):
                    flt = format(val, f'0{len(x)}b')
                    floating_mask = format(ins.index | int(mask.replace("X", "0"), 2), f'0{len(mask)}b')
                    for i in range(0, len(x)):
                        floating_mask = floating_mask[0:x[i]] + flt[i] + floating_mask[x[i]+1:]
                    masks.append(floating_mask)
                for index in masks:
                    mem[index] = ins.value

        return sum(mem.values())

solution = Day14Solution()
print(solution.partOne())
print(solution.partTwo())
