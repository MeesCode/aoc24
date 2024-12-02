

inp = list(map(lambda x: x.strip(), open("2i.txt").readlines()))

c = 0

for i in inp:
    safe = True
    nums = list(map(int, i.split(" ")))
    print(nums)
    if nums != sorted(nums) and nums != list(reversed(sorted(nums))):
        safe = False
        print("false order")
        continue

    for index, num in enumerate(nums):
        if index == 0:
            continue
        if abs(nums[index] - nums[index - 1]) < 1 or abs(nums[index] - nums[index - 1]) > 3:
            safe = False
            print("false diff")
            break

    if safe:
        c = c + 1

print(c)