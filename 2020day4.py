filename = "C:\\Users\\kevin\\Desktop\\2020day4\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

newStart = True
byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False, False

acceptableHclChars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
counter = 0
for line in inputList:
    if line == '':
        if byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True:
            counter += 1
        byr, iyr, eyr, hgt, hcl, ecl, pid = False, False, False, False, False, False, False
    else:
        if 'byr:' in line:
            byrInt = int(line[line.find('byr:')+4:line.find('byr:')+8])
            if byrInt >= 1920 and byrInt <= 2002:
                byr = True
        if 'iyr:' in line:
            iyrInt = int(line[line.find('iyr:')+4:line.find('iyr:')+8])         
            if iyrInt >=2010 and iyrInt <=2020:   
                iyr = True
        if 'eyr:' in line:
            eyrInt = int(line[line.find('eyr:')+4:line.find('eyr:')+8])         
            if eyrInt >=2020 and eyrInt <=2030:   
                eyr=True
        if 'hgt:' in line:
            splitLines = line.split()
            for subLine in splitLines:
                if 'hgt:' in subLine:
                    heightData = subLine[4:]
                    if heightData[-2:] == 'cm':
                        try:
                            height = int(heightData[0:3])
                            if height >= 150 and height <= 193:
                                hgt = True
                        except:
                            hgt = False
                    elif heightData[-2:] == 'in':
                        try:
                            height = int(heightData[0:2])
                            if height >= 59 and height <= 76:
                                hgt = True
                        except:
                            hgt = False
        if 'hcl:' in line:
            splitLines = line.split()
            for subLine in splitLines:
                if 'hcl:' in subLine:  
                    if len (subLine) == 11:
                        if subLine[4] == '#' and subLine [5] in acceptableHclChars and subLine [6] in acceptableHclChars and subLine[7] in acceptableHclChars and subLine[8] in acceptableHclChars and subLine[9] in acceptableHclChars and subLine[10] in acceptableHclChars:
                            hcl = True
        if 'ecl:' in line:
            splitLines = line.split()
            for subLine in splitLines:
                if 'ecl:' in subLine: 
                    color = subLine[4:] 
                    if color in eyecolors:
                        ecl = True
        if 'pid:' in line:
            splitLines = line.split()
            for subLine in splitLines:
                if 'pid:' in subLine:
                    pidString = subLine[4:] 
                    if len(pidString) == 9:
                        try:
                            pidString = int(pidString)
                            pid = True
                        except:
                            pid= False
if byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True:
    counter += 1
print("Part 2:",counter)