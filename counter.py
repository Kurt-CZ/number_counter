# open and load data from file
with open('sequenceTest.txt','r') as file:
    string = file.read()

# set variable for countinng and calculate strinng length
count = 0
length = len(string)

# iterate over every char in string and if same as the previous count it (excluding the first)
for i in range(length):
    if (i < length - 1 and string[i] == string[i + 1]):
        count += int(string[i])

# check if the first and last number are same and if yes count it (strinng should form a cicle)
if string[0] == string[length - 1]:
    count += int(string[0])

# print out the calculated result
print(count)
