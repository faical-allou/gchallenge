import sys
import random
import string

def read_case():
    line = input()
    n, q = line.rstrip().split(' ')
    N = int(n)
    Q = int(q)
    blocks = list(input())
    L = []
    R = []
    for i in range(Q):
        line = input()
        l, r = line.rstrip().split(' ')
        L.append(int(l))
        R.append(int(r))
    return N, Q, L, R, blocks


def solve(N, Q, L, R, blocks):
    count_possible = 0
    for i in range(Q):
        d = dict.fromkeys(string.ascii_uppercase, 0)
        for j in range(L[i]-1, R[i]):
            d[blocks[j]] += 1
       
        count_odd = 0
       
        for key, value in d.items():
            if value % 2 != 0: count_odd += 1
        
        if count_odd <= 1: 
            count_possible += 1

    return count_possible


def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)

#read number of cases
t = int(input())

for i in range(t):
    ###start solving
    #read input
    N, Q, L, R, blocks = read_case()

    #solve
    solution = solve(N, Q, L, R, blocks)
    print(format_output(i, solution))
    sys.stdout.flush()