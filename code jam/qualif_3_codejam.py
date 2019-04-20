import sys
import random

def read_case():
    line = input()
    s = list(map(int, list(line.rstrip().split(' '))))
    maxn = s[0]
    length = s[1]
    line = input()
    crypto = list(map(int, list(line.rstrip().split(' '))))
    return maxn, length, crypto

def format_output(i, solution):
    return 'Case #'+str(i+1)+': '+str(solution)

def solve(maxn, length, crypto):
    
    a_ , b_ = prime_prod(crypto[0], maxn)

    try:
        decrypt_initial = [min(a_ , b_), max(a_, b_)]
        return decryption(crypto, maxn, length, decrypt_initial)

    except:
        print('rollback')
        decrypt_initial = [max(a_ , b_), min(a_, b_)]
        return decryption(crypto, maxn, length, decrypt_initial)

def decryption(crypto, maxn, length, decrypt_int):
    for i in range(length-1):
        decrypt_int.append(int(crypto[i+1]/decrypt_int[i+1]))
    
    alphabet_prime = list(set(decrypt_int))
    alphabet_prime.sort()
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    dictonnary = [0]*(maxn+1)
    for i in range(26):
        dictonnary[alphabet_prime[i]] = alphabet[i]

    word = []
    for i in range(length+1):
        word.append(dictonnary[decrypt_int[i]]) 
    return ''.join(word)

def prime_prod(prime_factor, maxn):
    if int(prime_factor) % 2 == 0: 
        a_ = 2
        b_ = int(prime_factor/2)
        return a_ , b_
    for i in range(3,maxn+1,2):
        if int(prime_factor) % i == 0: 
            a_ = i
            b_ = int(prime_factor/i)
            break 
    return a_ , b_

#read number of cases
t = int(input())

for i in range(t):
    ###start solving
    #read input
    maxn, length, crypto = read_case()
    #solve
    solution = solve(maxn, length, crypto)
    print(format_output(i, solution))
    sys.stdout.flush()