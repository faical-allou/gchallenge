import sys
import random
import string

def read_case():
    n = input()
    N = int(n)
    
    S = []
    E = []
    L = []
    for i in range(N):
        line = input()
        s,e,l = line.rstrip().split(' ')
        S.append(int(s))
        E.append(int(e))
        L.append(int(l))
    return N, S, E, L


def solve(N, S, E, L):
    opportunity = [0]*N
    loss = [0]*N
    eaten = 0
    if N == 1: return E[0]
    for i in range(N):
        for j in range(N):
            others_decay = L.copy()
            others_energy = E.copy()
            del others_decay[j]
            del others_energy[j]
            loss[j] = sum([min(others_energy[k], S[j]*others_decay[k]) for k in range(N-1)]) / ((N-1)*S[j])

        for j in range(N):
            opportunity[j]= E[j]/S[j] - loss[j]
    
        max_ops = max(opportunity)
        max_idx = opportunity.index(max_ops)

        eaten = eaten + E[max_idx]
        E[max_idx] = 0
        for j in range(N):
            E[j] = max(0, E[j]-S[max_idx]*L[j])


    return eaten


def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)

#read number of cases
t = int(input())

for i in range(t):
    ###start solving
    #read input
    N, S, E, L = read_case()

    #solve
    solution = solve(N, S, E, L)
    print(format_output(i, solution))
    sys.stdout.flush()