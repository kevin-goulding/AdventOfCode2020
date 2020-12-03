filename = "C:\\Users\\kevin\\Desktop\\2020day2\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

def decodeP1(line):
    minV = int(line[0:line.find('-')])
    maxV = int(line[line.find('-')+1:line.find(' ')])
    char = line[line.find(" ")+1]
    code = line[line.find(":")+2:]
    if code.count(char)>=minV and code.count(char)<=maxV:
        return 1
    else:
        return 0

def decodeP2(line):
    pos1 = int(line[0:line.find('-')])
    pos2 = int(line[line.find('-')+1:line.find(' ')])    
    char = line[line.find(" ")+1]
    code = line[line.find(":")+2:]
    if (code[pos1-1] == char or code[pos2-1]==char) and (code[pos1-1] != code[pos2-1]):
        return 1
    else:
        return 0           

#Part 1
counter = 0
for entry in inputList:
    counter+= decodeP1(entry)
print("Part 1:",counter)

#Part 2
counter = 0
for entry in inputList:
    counter+= decodeP2(entry)
print("Part 2:",counter)

