import sys

a = 0
b = 0
t = 0

def read_case():
    line = input()
    min_a, max_b = line.rstrip().split(' ')
    t_tries = input()
    return int(min_a)+1,int(max_b),int(t_tries)

def solve(a,b,t):
    min_int = a
    max_int = b
    response = 'INIT'
    iteration = 0
    
    while response in ('INIT', 'TOO_BIG','TOO_SMALL') and iteration <t:       
        iteration = iteration+1
        guess = int((max_int-min_int)/2)+min_int
        print(guess)
        sys.stdout.flush()
        response = input()
        if response == 'TOO_BIG': 
            max_int = guess -1
        else: 
            min_int = guess + 1
    return response
       
#read number of cases
n = int(input())

for i in range(n):
    ###start solving
    #read input
    a_in,b_in,t_in = read_case()
    #solve
    response = solve(a_in, b_in, t_in)
    if response != 'CORRECT': break