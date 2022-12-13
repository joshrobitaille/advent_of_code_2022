class Command:
    def __init__(self, pwd, contents):
        self.pwd = pwd
        self.contents = contents
        
    def __info__(self):
        print(f'Dir: {self.pwd}\nContents: {contents}')
        
class Directory:
    def __init__(self, ParentDir, childDir, size):
        self.parentDir = parentDir
        self.childDir = childDir
        self.size = size

    
with open('input.txt','r') as f:
    input = [l.strip() for l in f]

obj = list()
contents = list()
pwd = ''
firstSet = True

for i in input:
    if i.__contains__('cd') and firstSet:
        firstSet = False
        pwd = i
    elif i.__contains__('cd'):
        obj.append(Command(pwd,contents))
        contents.clear()
        pwd = i
    elif i.__contains__('ls'):
        continue
    else:
        contents.append(i)

print(input)
   
for o in obj:
    o.__info__()

f.close()
