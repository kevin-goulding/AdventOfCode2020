filename = "C:\\Users\\kevin\\Desktop\\2020day8\\input.txt" 
with open(filename) as f:
    inputList = f.readlines()
inputList = [x.strip() for x in inputList] 

counter = 0
pointer =0
beenThereList = []
go = True

while go == True:
        instruction = inputList[pointer].split()
        beenThereList.append(pointer)
        if instruction[0]== 'nop':
            pointer+=1
        elif instruction[0] == 'acc':
            counter += int(instruction[1])
            pointer+= 1
        elif instruction[0] == 'jmp':
            pointer += int(instruction[1])

        if pointer in beenThereList:
            print("Part 1:",counter)
            go = False


oldInputList = inputList.copy()
counter = 0
pointer =0
beenThereList = []
go = True
changePointer = 0

while go == True:
        instruction = inputList[pointer].split()
        beenThereList.append(pointer)
        if instruction[0]== 'nop':
            pointer+=1
        elif instruction[0] == 'acc':
            counter += int(instruction[1])
            pointer+= 1
        elif instruction[0] == 'jmp':
            pointer += int(instruction[1])

        if pointer in beenThereList:
            inputList = oldInputList.copy()
            changeInstruction = inputList[changePointer].split()
            if changeInstruction[0] == 'nop':
                inputList[changePointer] = 'jmp '+changeInstruction[1]
            elif changeInstruction[0] == 'jmp':
                inputList[changePointer] = 'nop '+changeInstruction[1]
            changePointer +=1
            beenThereList = []
            counter = 0
            pointer = 0

        if pointer >= len(inputList):
            print("Part 2:",counter)
            go = False

