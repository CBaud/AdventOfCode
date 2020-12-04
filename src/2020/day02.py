import re

class Day02Solution:
    def __init__(self):
        file = open("day02.txt", "r")
        self.items = [re.match("(?P<min>\d+)-(?P<max>\d+)\s+(?P<pattern>\w):\s+(?P<password>.+)", line) for line in file.read().split("\n")]
    
    def partOne(self) -> int:
        valid = 0
        for item in self.items:
            min = int(item.group("min"))
            max = int(item.group("max"))
            occurrences = item.group("password").count(item.group("pattern"))
            if min <= occurrences and occurrences <= max:
                valid += 1

        return valid

    def partTwo(self) -> int:
        valid = 0
        for item in self.items:
            min = int(item.group("min")) - 1
            max = int(item.group("max")) - 1
            pattern = item.group("pattern")
            password = item.group("password")
            if (min < len(password) and password[min] == pattern) ^ (max < len(password) and password[max] == pattern):
                valid += 1

        return valid

solution = Day02Solution()
print(solution.partOne())
print(solution.partTwo())
