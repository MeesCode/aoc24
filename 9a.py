
file = open("9i.txt").read().strip()

string = ""
space = False
uid = 0
for i in file:

    if not space:
        string += str(uid) * int(i)
        uid += 1
    else:
        string += "." * int(i) 

    space = not space

numbers = [None] * len(string)

# USE ARRAY INSTEAD OF STRING SINCE ID > 9

empty = 0
nonempty = len(string) - 1
loops = 0
while empty < nonempty:

    # find next empty location
    while string[empty] != ".":
        numbers[loops] = int(string[empty])
        empty += 1
        loops += 1

    # find next nonempty location
    while string[nonempty] == ".":
        nonempty -= 1

    if empty >= nonempty:
        break

    # swap
    string = string[:empty] + string[nonempty] + string[empty+1:nonempty] + string[empty] + string[nonempty+1:]
    numbers[loops] = int(string[empty])
    loops += 1
    empty += 1

print(string)
print(numbers)

#get result
result = 0
for index, number in enumerate(numbers):
    if(number == None):
        break
    result += index * number

print(result)