import re 

#iterate on the txt file
input = open('Puzzle1-Input.txt', 'r')
inputLines = input.readlines()
regex = r'[a-zA-Z\n]+'
sum = 0
for line in inputLines:
    line = re.sub(regex,'',line)
    sum += int(line[0] + line[-1])
print(sum)