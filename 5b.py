rules = [(int(i.split("|")[0]), int(i.split("|")[1])) for i in open("5i.txt").read().split("\n\n")[0].split("\n")]
updates = [[int(j) for j in i.split(",")] for i in open("5i.txt").read().split("\n\n")[1].split("\n")]
count = 0

for update in updates:
    print("checking", update)
    correct = True
    for number in range(len(update)-1):

        for after in range(number+1, len(update)):
            a = update[after]
            b = update[number]

            if (a, b) in rules:

                # rule broken
                print(f"Rule broken: {a} after {b}")
                correct = False
                break

            if not correct:
                break
        if not correct:
            break

    if not correct:
        # sort according to the rules
        for x in range(len(update)):
            for i in range(len(update) - 1):
                for j in range(i+1, len(update)):
                    if (update[j], update[i]) in rules:
                        update[i], update[j] = update[j], update[i]
                        break

        print("sorted update", update)
        count += update[len(update)//2]

print(count)