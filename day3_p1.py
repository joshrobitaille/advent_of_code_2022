from string import ascii_letters

priorities = []

# create key value pairs with ascii (a-z and A-Z) with number asignments starting with 1
priorityValues = {key: value for value, key in enumerate(ascii_letters, start=1)}

# create lines list with each entry as a line from input.txt
input = open('reference/Day03/input.txt', 'r')
lines = input.read().splitlines()

# for each entry in lines create a list of 2, the first half of the line as 1 and the second half as 2
for i in lines:
    one = i[:len(i)//2]
    two = i[len(i)//2:]
    # append the 2 halves as a list to priorities
    priorities.append([one, two])

total = 0

# for each priority entry find the intersection of the 2 for itemType
# add the number value associated to the itemType to the total
for x in priorities:
    itemType = list(set(x[0]).intersection(set(x[1])))
    total += priorityValues.get(itemType[0])

print(total)