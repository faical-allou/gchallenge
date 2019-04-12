import sys

def read_case():
    size = int(input())
    wall = list(map(int, list(input())))

    return size, wall

def solve(size, wall):
    half_size = int((size+1)/2)
    beauty_max = 0
    for l in range(size - half_size+1):
        beauty = sum([wall[k] for k in range(l, l+half_size)])
        if beauty >= beauty_max: beauty_max = beauty
    return beauty_max

def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)

#read number of cases
n = int(input())

for i in range(n):
    ###start solving
    #read input
    size, wall = read_case()

    #solve
    solution = solve(size, wall)
    print(format_output(i, solution))
    sys.stdout.flush()