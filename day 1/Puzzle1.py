import re 

### PART 1
#iterate on the txt file
input = open('input.txt', 'r')
inputLines = input.readlines()

def part1():
    regex = r'[a-zA-Z\n]+'
    sum = 0
    #Solution 1
    for line in inputLines:
        line = re.sub(regex,'',line)
        sum += int(line[0] + line[-1])
    print(sum)
    #Solution 2
    total = 0
    for line in inputLines:
        digits = [char for char in line if char.isnumeric()]
        total += int(digits[0] + digits[-1])

### PART 2
### Map one to ten to an obj 
def part2():
    numToWordMap = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

    sum = 0
    for line in inputLines:
        if (line[0].isnumeric() and line[-1].isnumeric()):
            sum += int(line[0] + line[-1])
    print(sum)

part2()