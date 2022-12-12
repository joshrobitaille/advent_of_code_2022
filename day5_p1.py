import re

# stack number will be index + 1
stacks = [['F','C','J','P','H','T','W'],['G','R','V','F','Z','J','B','H'],['H','P','T','R'],['Z','S','N','P','H','T'],['N','V','F','Z','H','J','C','D'],['P','M','G','F','W','D','Z'],['M','V','Z','W','S','J','D','P'],['N','D','S'],['D','Z','S','F','M']]

moves = []
# creates lines list with each entry as a line from input.txt
input = open('reference/Day05/input.txt', 'r')
lines = input.read().splitlines()
# appends each line into the move list using regex to extract only the numbers
for i in lines:
    # creates 2d array, each layer will be [x,x,x]
    # index 0 = move number of crates
    # index 1 = from stack
    # index 2 = to stack
    moves.append(re.findall(r'\b\d+\b', i))

# for each entry in the move list
for j in moves:
    # create counter from number of crates to move
    counter = range(int(j[0]))
    for x in counter:
        # appends last index of the from stack to the to stack
        stacks[int(j[2]) - 1].append(stacks[int(j[1]) - 1][-1])
        # removes last index of the to stack
        stacks[int(j[1]) - 1].pop()

# prints the top crate in each stack
output = ""
for x in stacks:
    output += x[-1]

print(output)