import re
import string

class Day04Solution:
    def __init__(self):
        file = open("day04.txt", "r")
        self.items = file.read().split("\n")

    def partOne(self, slide=3, drop=1) -> int:
        def hasLabels(passport: str) -> bool:
            return (re.match(".*byr:.+", passport)
                and re.match(".*ecl:.+", passport)
                and re.match(".*eyr:.+", passport)
                and re.match(".*hcl:.+", passport)
                and re.match(".*hgt:.+", passport)
                and re.match(".*iyr:.+", passport)
                and re.match(".*pid:.+", passport))

        passports = [""]
        for line in self.items:
            if not line:
                passports.append("")
                continue
            passports[-1] += " " + line
        
        return len([passport for passport in passports if (hasLabels(passport))])

    def partTwo(self) -> int:
        def hasLabels(passport: str) -> bool:
            m = re.match(".*byr:(?P<value>\d{4}).*", passport)
            if not m or int(m.group("value")) < 1920 or int(m.group("value")) > 2002:
                return False

            m = re.match(".*ecl:(?P<value>\w{3}).*", passport)
            if not m or m.group("value") not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                return False
            
            m = re.match(".*eyr:(?P<value>\d{4}).*", passport)
            if not m or int(m.group("value")) < 2020 or int(m.group("value")) > 2030:
                return False
            
            m = re.match(".*hcl:#(?P<value>\w+).*", passport)
            if not m or bool([char for char in m.group("value") if char not in string.hexdigits]):
                return False

            m1 = re.match(".*hgt:(?P<value>\d{3})cm.*", passport)
            m2 = re.match(".*hgt:(?P<value>\d{2})in.*", passport)
            if ((not m1 or int(m1.group("value")) < 150 or int(m1.group("value")) > 193) and
                (not m2 or int(m2.group("value")) < 59 or int(m2.group("value")) > 76)):
                return False
                
            m = re.match(".*iyr:(?P<value>\d{4}).*", passport)
            if not m or int(m.group("value")) < 2010 or int(m.group("value")) > 2020:
                return False
            
            m = re.match(".*pid:(?P<value>\d+).*", passport)
            if not m or len(m.group("value")) != 9:
                return False

            return True

        passports = [""]
        for line in self.items:
            if not line:
                passports.append("")
                continue
            passports[-1] += " " + line
        
        return len([passport for passport in passports if (hasLabels(passport))])

solution = Day04Solution()
print(solution.partOne())
print(solution.partTwo())
