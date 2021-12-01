import csv
with open('Day1 AOCInput.csv', newline = '') as input:
    reader = csv.reader(input)
    puzzle = list(input)

# for element in puzzle: 
#     print(int(element)-1)
counter = 0

for increment in range(1,len(puzzle)):
    change=(int(puzzle[increment]) - int(puzzle[increment-1]))
    if(change > 0):
        counter+=1
    # print(int(puzzle[increment]))
    # print(change)
#print(puzzle)
#print(len(puzzle))
print(counter)
