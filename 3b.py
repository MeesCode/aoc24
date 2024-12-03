import re

inp = open("3i.txt").read()
inp = inp.replace("\n", "")

chunks = re.findall(r"(?:^|do\(\))(.*?)(?:$|don't\(\))", inp)

total = 0

for chunk in chunks:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", chunk)

    for match in matches:
        product = int(match[0]) * int(match[1])
        total = total + product

print(total)
