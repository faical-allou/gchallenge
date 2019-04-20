import sys
import random

def read_case():
    size = int(input())
    wall = list(map(int, list(input())))

    return size, wall

def initialize(size, wall):
    init = random.randint(0,size)
    return init

def solve(init, size, wall):
    first_painted = init
    last_painted = init
    for j in range(int((size+1)/2)):
        if first_painted>0:
            if last_painted < size-1:
                if wall[first_painted -1] > wall[last_painted +1]:
                    first_painted = first_painted -1
                else:
                    last_painted = last_painted +1
            else:
                first_painted = first_painted -1
        else: 
            last_painted = last_painted +1

    beauty = sum(wall[k] for k in range(first_painted, last_painted))
    
    return beauty

def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)


#read number of cases
n = int(input())

for i in range(n):
    ###start solving
    #read input
    size, wall = read_case()

    #solve
    start = initialize(size, wall)
    solution = solve(start, size, wall)
    print(format_output(i, solution))