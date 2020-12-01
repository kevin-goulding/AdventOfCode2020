#My Setup

#I've saved the input data as a txt file on my desktop.
#I'm trying to read directly from the source at https://adventofcode.com/2020/day/1/input but I'm having issues with the https... will update later if I figure it out
#If you run this, you'll need to change this filename to the location of your input data
filename = "C:\\Users\\kevin\\Desktop\\2020Day1\\input.txt" 

#Prep the input data- read it into a list and strip all of the extra whitespace.  After these steps, the input data is neatly in a list called "inputList"
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

#I think that AdventofCode gives each person different goal values, so I added this as a manual entry,
goalValue = int(input("Enter puzzle goal: "))

#There are a ton of ways to do this, and I highly doubt that mine was the best.  My thought was to divide the inputs into two lists: one contains values less than 
#half of the goal number (2020), and the other is more than half.  Rather than inefficiently checking ALL values against each other, we only have to check the
# "lessThanHalf" and "moreThanHalf" added together, as the sum of 2 moreThanHalf values will always be greater than 2020, and 2 lessThanHalf will always be less than 2020
lessThanHalf = []
moreThanHalf = []
for entry in inputList:
    if int(entry) < goalValue/2:
        lessThanHalf.append(int(entry))
    else:
        moreThanHalf.append(int(entry))

#PART 1
#Now I just iterate through each lessThanHalf entry and check it against every moreThanHalf entry until it finds the numbers that add up to 2020.  Multiply them, and
#part 1 is done.

for lowEntry in lessThanHalf:
    for highEntry in moreThanHalf:
        if (lowEntry + highEntry == goalValue):
            print("Part 1:",lowEntry*highEntry)

#PART 2
#For 3 values, we know that the possible candidates will have at least 2 lessThanHalf values. 

#I first check to see if any combination of 3 lessThanHalf sums equals 2020
for entry1 in lessThanHalf:
    for entry2 in lessThanHalf:
        for entry3 in lessThanHalf:
            if (entry1+entry2+entry3 == goalValue):
                print("Part 2:",entry1*entry2*entry3)

#Now I check whether any combination of lessThanHalf, lessThanHalf, moreThanHalf equals 2020
for entry1 in lessThanHalf:
    for entry2 in lessThanHalf:
        for entry3 in moreThanHalf:
            if (entry1+entry2+entry3 == goalValue):
                print("Part 2:",entry1*entry2*entry3)

#This isn't perfect. It prints the answer twice because it double counts lessThanHalf pairs separately as (a,b) and (b,a)