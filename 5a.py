
rules = [(int(i.split("|")[0]), int(i.split("|")[1])) for i in open("5i.txt").read().split("\n\n")[0].split("\n")]
updates = [[int(j) for j in i.split(",")] for i in open("5i.txt").read().split("\n\n")[1].split("\n")]
count = 0

for update in updates:
    print("\nchecking", update)
    correct = True
    for number in range(len(update)-1):

        for after in range(number+1, len(update)):
            if (update[after], update[number]) in rules:
                # rule broken
                print(f"Rule broken: {update[after]} after {update[number]}")
                correct = False
                break
            if not correct:
                break
        if not correct:
            break

    if correct:
        count += update[len(update)//2]

print(count)

