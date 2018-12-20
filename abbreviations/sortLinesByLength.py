import re

inputFile = input("Enter filename here: ")
outputFile = 'sortedByLength_' + inputFile

list = []

# open file
f = open(inputFile,'r')
for line in f:
	list.append(line)
f.close()

list.sort()
list.sort(key=len, reverse=True)

newData = ""
for line in list:
	newData += line

# close file
f = open(outputFile,'w')
f.write(newData)
f.close()
