def checkPacketStart(charOne:str,charTwo:str,charThree:str,charFour:str) -> bool:
    # check if char 1 equals char 2, 3 or 4
    if charOne.__eq__(charTwo) or charOne.__eq__(charThree) or charOne.__eq__(charFour):
        return False
    # check if char 2 equals char 3 or 4
    elif charTwo.__eq__(charThree) or charTwo.__eq__(charFour):
        return False
    # check if char 3 equals char 4
    elif charThree.__eq__(charFour):
        return False
    # if none of the 4 chars are equal then start of packet would be true
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
# start output as 4 since we need at least 4 chars to start
output = 4
while x < len(char):
    # if checkPacketStart returns true than break the while loop
    if checkPacketStart(char[x],char[x + 1],char[x + 2],char[x + 3]):
        break
    # if checkPacketStart returns false add 1 to ouput and the counter (x)
    output += 1
    x += 1

print(output)

file.close()