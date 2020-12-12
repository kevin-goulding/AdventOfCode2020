filename = "C:\\Users\\kevin\\Desktop\\2020day7\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

def parseLine(line):
    key = line[:line.find("bag")-1]
    values = line[line.find('contain')+8:].split(',')
    values = [x.strip() for x in values] 

    value = {}
    for words in values:
        thisWord = (words[2:words.find("bag")-1])
        try:
            number = int(words[0:1])
        except:
            pass
        if thisWord != ' other':
            value[(words[2:words.find("bag")-1])]=number
    return key,value

def findParents(bagDict, starter):
    returnList = []
    for key in bagDict.keys():
        if starter in bagDict[key]:
            returnList.append(key)
            returnList.extend(findParents(bagDict, key))
    return(returnList)

def countKids(bagDict, starter):
    count = 1
    for key in bagDict[starter].keys():

        count += bagDict[starter][key] * countKids(bagDict, key)

    return(count)
            

instructDict = {}
for line in inputList:
    key, value = parseLine(line)
    instructDict[key] = value



tempList = (findParents(instructDict, "shiny gold"))
newList = []
for item in tempList:
    if item not in newList:
        newList.append(item)
print("Part 1:", len(newList))

print("Part 2:", countKids(instructDict, "shiny gold")-1)
