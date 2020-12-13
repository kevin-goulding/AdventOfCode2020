filename = "C:\\Users\\kevin\\Desktop\\2020day10\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [int(x.strip()) for x in inputList] 

inputList.sort()

count1 = 1
count3 = 1

for x in range(len(inputList)-1):
    diff = inputList[x+1]-inputList[x]
    if diff == 1:
        count1+=1
    elif diff == 3:
        count3+= 1

print("Part 1:",count1*count3)

adapters = {}
adaptList = inputList.copy()
adaptList.reverse()
adaptList.append(0)

for x in adaptList:
    adapters[x] = 0

adapters[167] = 1

for adapter in adaptList:
    totalVal = 0

    if (adapter+3) in adaptList:
        totalVal += (adapters[adapter+3]) 

    if (adapter+2) in adaptList:
        totalVal += (adapters[adapter+2])

    if (adapter+1) in adaptList:
        totalVal += (adapters[adapter+1])

    if adapter != 167:
        adapters[adapter] = totalVal

print("Part 2:",adapters[0])
