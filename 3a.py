import re

inp = open("3i.txt").read()

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", inp)

total = 0

for match in matches:
    print(match)
    product = int(match[0]) * int(match[1])
    total = total + product

print(total)
