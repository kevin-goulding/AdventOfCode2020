filename = "C:\\Users\\kevin\\Desktop\\2020day5\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

values = [64,32,16,8,4,2,1]
values2 = [1,2,4]
highest = 0
allSeats = []
for entry in inputList:

    firstHalf = []
    secondHalf = []
    for char in entry[0:7]:
        if char == 'B':
            firstHalf.append(1)
        else:
            firstHalf.append(0)
    for char in entry[7:10]:
        if char == "R":
            secondHalf.append(1)
        else:
            secondHalf.append(0)
    totalFirst = 0
    for x in range(7):
        totalFirst += firstHalf[x] * values[x]
    totalSecond = 0
    for x in range(3):
        totalSecond += secondHalf[x] * values2[x]
    total = 8*totalFirst + totalSecond
    allSeats.append(total)
    if total > highest:
        highest = total
print("Part 1:",highest)
allSeats.sort()

oldSeat = 40
for seat in allSeats:
    if seat != oldSeat+1 and seat>40:
        print("Part 2:", seat-1)
    oldSeat = seat