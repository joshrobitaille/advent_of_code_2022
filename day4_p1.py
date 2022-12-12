ranges = []
# creates lines list with each entry as a line from input.txt
input = open('reference/Day04/input.txt', 'r')
lines = input.read().splitlines()

# appends each entry from line list to move list
for i in lines:
    ranges.append(i)

# function to check if the task 1 or 2 are subsets of each other
def checkRanges (assignments) -> bool:
    taskOne = assignments.split(",")[0].split("-")
    taskTwo = assignments.split(",")[1].split("-")

    x = range(int(taskOne[0]), int(taskOne[1]) + 1)
    y = range(int(taskTwo[0]), int(taskTwo[1]) + 1)

    # print(f"task one: {x} task two: {y} || {set(x).issubset(y) or set(y).issubset(x)}")

    return set(x).issubset(y) or set(y).issubset(x)

# for each entry in range adds 1 to the total if checkRanges comes back true, then print the total
total = 0
for j in ranges:
    if checkRanges(j):
        total += 1

print(total)