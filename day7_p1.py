class Command:
    def __init__(self, commandInput, commandOutput):
        self.commandInput = commandInput
        self.commandOutput = commandOutput
        
class Directory:
    def __init__(self, ParentDir, childDir, size):
        self.parentDir = parentDir
        self.childDir = childDir
        self.size = size

with open('input.txt','r') as f:
    input = [l.strip() for l in f]

x = 1    
for c in input:
    if c.__contains__('$'):
        f'command{x}' = Command()

print(commands)

f.close()
