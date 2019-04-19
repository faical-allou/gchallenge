import sys
import random

def read_case():
    line = input()
    N = list(map(int, list(line)))
    return N

def format_output(i, solu1, solu2):
    return 'Case #'+str(i+1)+': '+str(solu1)+" "+str(solu2)

def solve(N):
    check_4 = [str(int(digit == 4)) for digit in N ] 
    sub_4 = []
    for i in range(len(N)):
        sub_4.append(str(N[i] - int(check_4[i])))
    a_int = ''.join(sub_4)
    b_int = ''.join(check_4)
    return a_int, b_int

#read number of cases
t = int(input())

for i in range(t):
    ###start solving
    #read input
    N = read_case()

    #solve
    sol1, sol2 = solve(N)
    print(format_output(i, sol1, sol2))
    sys.stdout.flush()