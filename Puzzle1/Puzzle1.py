import re 

#iterate on the txt file
input = open('Puzzle1-Input.txt', 'r')
inputLines = input.readlines()
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
print(total)