# function to check if there are any duplicates in the list
# compare the length of the list (possibly containing dups) to the length of the list as a set (no dups allowed)
def checkDuplicates(l:list[str]) -> bool:
    if len(l).__eq__(len(set(l))):
        return False
    else:
        return True

# read input file one char at a time
# append the char to the char list
with open('reference/Day06/input.txt', 'r') as file:
    char = []
    while True:
        c = file.read(1)
        char.append(c)
        if not c:
            # end of file
            break

# create counter 
x = 0
# start output as 14 since we need at least 14 chars to start
output = 14
while x < len(char):
    # create a list of 14 chars starting with the index of x
    charL = [char[y] for y in range(x, x + 14)]
    # if checkDuplicates returns false (meaning no duplicate chars) break the loop
    if not checkDuplicates(charL):
        break
    # if checkMessageStart returns false add 1 to ouput and the counter (x)
    output += 1
    x += 1

print(output)

file.close()