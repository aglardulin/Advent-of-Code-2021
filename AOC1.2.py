import csv
with open('Day1 AOCInput.csv', newline = '') as input:
    reader = csv.reader(input)
    puzzle = list(input)

# for element in puzzle: 
#     print(int(element)-1)
counter = 0

for increment in range(2,len(puzzle)-1):
    prevsum=(int(puzzle[increment]) + int(puzzle[increment-1]) + int(puzzle[increment-2]))
    sum=(int(puzzle[increment-1])+ int(puzzle[increment]) +int(puzzle[increment+1]))
    if(sum > prevsum):
        counter+=1
    # print(int(puzzle[increment]))
    # print(change)
#print(puzzle)
#print(len(puzzle))
print(counter)
