
list1 = []
list2 = []

input = list(map(lambda x: x.strip(), open("1i.txt").readlines()))

for i in input:
    list1.append(int(i.split("   ")[0]))
    list2.append(int(i.split("   ")[1]))

list1.sort()
list2.sort()

res = 0

for i in range(len(list1)):
    res = res + abs(list1[i] - list2[i])

print(res)