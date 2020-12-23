import re

class Day18Solution:
    def __init__(self):
        file = open("day18.txt", "r")
        self.items = file.read().split("\n")

    def evaluate(self, expression: str) -> int:
        exp = expression.split()
        val = int(exp[0])
        for index in range(1, len(exp), 2):
            if exp[index] == "+":
                val += int(exp[index+1])
            elif exp[index] == "*":
                val *= int(exp[index+1])
        return val

    def evaluate_advanced(self, expression: str) -> int:
        exp = expression.split()
        for index in range(len(exp)-2, 0, -2):
            if exp[index] == "+":
                exp[index - 1] = str(int(exp[index - 1]) + int(exp[index + 1]))
                del exp[index + 1]
                del exp[index]
        
        val = int(exp[0])
        for index in range(1, len(exp), 2):
            if exp[index] == "+":
                val += int(exp[index+1])
            elif exp[index] == "*":
                val *= int(exp[index+1])
        return val

    def partOne(self) -> int:
        total = 0
        for expression in self.items:
            parenthesis = re.findall("(?P<x>\([^\(\)]+\))", expression)
            while parenthesis:
                for subexpression in parenthesis:
                    result = self.evaluate(subexpression[1:-1])
                    expression = expression.replace(subexpression, str(result))
                parenthesis = re.findall("(?P<x>\([^\(\)]+\))", expression)
            total += self.evaluate(expression)

        return total

    def partTwo(self) -> int:
        total = 0
        for expression in self.items:
            parenthesis = re.findall("(?P<x>\([^\(\)]+\))", expression)
            while parenthesis:
                for subexpression in parenthesis:
                    result = self.evaluate_advanced(subexpression[1:-1])
                    expression = expression.replace(subexpression, str(result))
                parenthesis = re.findall("(?P<x>\([^\(\)]+\))", expression)
            total += self.evaluate_advanced(expression)
        return total

solution = Day18Solution()
print(solution.partOne())
print(solution.partTwo())
