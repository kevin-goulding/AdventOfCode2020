filename = "C:\\Users\\kevin\\Desktop\\2020day6\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

totalCountP1 = 0
totalCountP2 = 0
length = 0
letterList = []
letterDict = {}

for entry in inputList:
    if entry == '':
        totalCountP1 += len(letterList)
        for letter in letterDict.keys():
            if letterDict[letter]== length:
                totalCountP2 +=1
        letterList.clear()
        letterDict.clear()
        length = 0
    else:
        length +=1
        for char in entry:
            if char not in letterList:
                letterList.append(char)
            if char not in letterDict.keys():
                letterDict[char]=1
            else:
                letterDict[char] = letterDict[char]+1

totalCountP1 += len(letterList)
for letter in letterDict.keys():
    if letterDict[letter]== length:
        totalCountP2 +=1

print("Part 1:",totalCountP1)
print("Part 2:",totalCountP2)


