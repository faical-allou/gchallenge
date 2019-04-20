import sys
import random

def read_case():
    line = input()
    size = int(line)
    line = input()
    P = list(list(line))
    return size, P

def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)

def solve(size, path):
    solu = []
    for i in range(2*size - 2):
        if path[i] == 'E':
            solu.append('S')
        else:
            solu.append('E')
    
    return ''.join(solu)

#read number of cases
t = int(input())

for i in range(t):
    ###start solving
    #read input
    size, P = read_case()

    #solve
    solution = solve(size, P)
    print(format_output(i, solution))
    sys.stdout.flush()