import sys
import random

def read_case():
    line = input()
    r, c = line.rstrip().split(' ')
    r = int(r)
    c = int(c)
    s = [[]*c for x in range(r)]
    list_centers = []
    for i in range(r):
        s[i] = list(map(int, list(input())))
        for j in range(c):
            if s[i][j] == 1 : list_centers.append([i,j])
    return int(t),r,c,s, list_centers

def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)

def solve(r,c,s,list_centers):
    hm1, mc1, mh1 = heatmap(r,c,s,list_centers,0)
    current_maxheat = mh1
    ncenters = len(mc1) 
    centroid = [int(sum(mc1[i][0] for i in range(ncenters))/ncenters), int(sum(mc1[i][1] for i in range(ncenters))/ncenters)]
    mc1.append(centroid)
    for i in range(r):
        for j in range(c):
            list_centers.append([i,j])
            hm2, mc2, mh2 = heatmap(r,c,s,list_centers,0)
            list_centers.pop()
            current_maxheat = min(current_maxheat, mh2)
    return current_maxheat

def manhattan(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

def heatmap(r,c,s,list_centers,maxoffset):
    heatmap = [[0]*c for x in range(r)]
    maxheat = 0
    maxcoord = []
    for i in range(r):
        for j in range(c):
            heatmap[i][j] = min(manhattan(i,j,l[0],l[1]) for l in list_centers)
        maxheat = max(maxheat, max(heatmap[i][k] for k in range(c) ))
    
    maxrow = [x for x in heatmap if maxheat-maxoffset in x]
    for maxr in maxrow:
        maxcol = [i for i, x in enumerate(maxr) if x == maxheat-maxoffset]
    maxcoord = list([heatmap.index(maxrow[i]), maxcol[j]] for j in range(len(maxcol)) for i in range(len(maxrow)))
    #print(heatmap, maxcoord, maxheat )
    return heatmap, maxcoord, maxheat 

#read number of cases
t = int(input())

for i in range(t):
    ###start solving
    #read input
    t,r,c,s,list_centers = read_case()

    #solve
    solution = solve(r,c,s,list_centers)
    print(format_output(i, solution))
    sys.stdout.flush()