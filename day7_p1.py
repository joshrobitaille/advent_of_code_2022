class commands(self, parentDir, childDir, size, commandInput, commandOutput):
    def __init__(self):
        self.parentDir = parentDir
        self.childDir = childDir
        self.size = size
        self.commandInput = commandInput
        self.commandOutput = commandOutput

with open('input.txt','r') as f:
    input = [l.strip() for l in f]
    
# for c in commands:
#     if c.__contains__('$'):
#         commands[f'{key}'] = value
#         key = ''
#         value.clear()
#         key += c.strip()
#         x += 1
#     else:
#         value.append(c.strip())

print(commands)

f.close()
