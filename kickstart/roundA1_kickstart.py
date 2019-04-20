import sys
import random

def read_case():
    line = input()
    n, p = line.rstrip().split(' ')
    line = input()
    s = list(map(int, list(line.rstrip().split(' '))))

    return int(t),int(n),int(p),s

def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)

def solve(n,p,s):
    s.sort()
    sum_s = [0]*(n-p+1)
    max_s = [0]*(n-p+1)
    work_s = [0]*(n-p+1)
    for i in range(n-p+1):
        sum_s[i]= sum(s[i+j] for j in range(0,p))
        max_s[i]= s[i+p-1]
        work_s[i] = max_s[i]*p - sum_s[i]
    return min(work_s)

#read number of cases
t = int(input())

for i in range(t):
    ###start solving
    #read input
    t,n,p,s = read_case()

    #solve
    solution = solve(n,p,s)
    print(format_output(i, solution))