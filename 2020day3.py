filename = "C:\\Users\\kevin\\Desktop\\2020day3\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

def CountTrees(inputList, xMovement, yMovement):
    treeCount = 0
    yPos = 0
    xPos = 0
    while yPos < len(inputList)-1:
        yPos += yMovement
        xPos += xMovement
        if xPos >= len(inputList[yPos]):
            xPos -= len(inputList[yPos])
        if inputList[yPos][xPos] == "#":
            treeCount +=1
    return(treeCount)

print("Part 1:", CountTrees(inputList,3,1))
print("Part 2:", CountTrees(inputList,1,1)*CountTrees(inputList,3,1)*CountTrees(inputList,5,1)*CountTrees(inputList,7,1)*CountTrees(inputList,1,2))