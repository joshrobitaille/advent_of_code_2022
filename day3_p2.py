from string import ascii_letters

priorities = []

# create key value pairs with ascii (a-z and A-Z) with number asignments starting with 1
priorityValues = {key: value for value, key in enumerate(ascii_letters, start=1)}

# create lines list with each entry as a line from input.txt
input = open('reference/Day03/input.txt', 'r')
lines = input.read().splitlines()

# for each entry in lines append the line to priorities
for i in lines:
    priorities.append(i)

total = 0
# create a counter
x = 0

# while x is less than the length of the priorities list
# find the intersection of 3 entries in priorities for the itemType
# add 3 to x as the counter (since we are looking at indicies x, x+1, x+2 : ex- 0,1,2)
# add the value assigned to the itemType to total
while x < len(priorities):
    itemType = list(set(priorities[x]) & set(priorities[x + 1]) & set(priorities[x + 2]))
    x += 3
    total += priorityValues.get(itemType[0])

print(total)