
list1 = []
list2 = []

inp = list(map(lambda x: x.strip(), open("1i.txt").readlines()))

for i in inp:
    list1.append(int(i.split("   ")[0]))
    list2.append(int(i.split("   ")[1]))

res = 0

for a in list1:
    c = 0
    for b in list2:
        if a == b:
            c = c + 1
    res = res + a * c

print(res)