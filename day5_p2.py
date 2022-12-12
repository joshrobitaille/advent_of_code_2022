import re

# stack number will be index + 1 
# reversed: stack index will be stack number - 1
stacks = [['F','C','J','P','H','T','W'],['G','R','V','F','Z','J','B','H'],['H','P','T','R'],['Z','S','N','P','H','T'],['N','V','F','Z','H','J','C','D'],['P','M','G','F','W','D','Z'],['M','V','Z','W','S','J','D','P'],['N','D','S'],['D','Z','S','F','M']]

with open('reference/Day05/input.txt') as file:
    # lines[0] = number of crates to move
    # lines[1] = stack to move crates from
    # lines[2] = stack to move crates to
    lines = []
    for line in file:
        lines.append(re.findall(r'\d+', line))

for i in lines:
    # stack to move from will be line at index 1 (-1 to match the index)
    fromStack = int(i[1]) - 1
    # stack to move to will be line at index 2 (-1 to match the index)
    toStack = int(i[2]) - 1
    # number of crates to move (+1 to work with indicies)
    crateAmount = int(i[0]) + 1
    # extend the to stack with entires (equal to crates to move) in the from stack
    stacks[toStack].extend(stacks[fromStack][len(i[1]) - crateAmount::])
    # removes the entries (added to the to stacj) from the from stack
    del stacks[fromStack][len(i[1]) - crateAmount:]

# prints the top crate in each stack
output = ""
for j in stacks:
    output += j[-1]

print(output)