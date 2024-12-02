

inp = list(map(lambda x: x.strip(), open("2i.txt").readlines()))

c = 0

for i in inp:
    nums = list(map(int, i.split(" ")))
    print(nums)

    for rem in range(len(nums)):
        safe = True
        newnums = nums.copy()
        newnums.pop(rem)

        if newnums != sorted(newnums) and newnums != list(reversed(sorted(newnums))):
            safe = False
            print("false order")
            continue

        for index, num in enumerate(newnums):
            if index == 0:
                continue
            if abs(newnums[index] - newnums[index - 1]) < 1 or abs(newnums[index] - newnums[index - 1]) > 3:
                safe = False
                print("false diff")
                break

        if safe:
            c = c + 1
            break

print(c)