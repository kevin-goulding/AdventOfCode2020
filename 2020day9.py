filename = "C:\\Users\\kevin\\Desktop\\2020day9\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

def checkData(listof25, checkNum):
    for entry in listof25:
        target = int(checkNum) - int(entry)
        if str(target) in listof25:
            return(True)
    return(False)

def findContiguous(inputList, checkNum):
    startPoint = 0
    for x in range(len(inputList)):
        index = startPoint
        added = 0
        while added < int(checkNum):
            added += int(inputList[index])
            if added == int(checkNum):
                return(inputList[startPoint:index])
            index+=1
        startPoint+=1


pointer = 25
finalNum = 0
while pointer < len(inputList):
    preamble = inputList[pointer-25:pointer]
    checkNum = inputList[pointer]
    if checkData(preamble,checkNum)== False:
        print("Part 1:",inputList[pointer])
        finalNum = inputList[pointer]
    pointer+=1

finalList = (findContiguous(inputList, finalNum))
print(int(max(finalList))+int(min(finalList)))