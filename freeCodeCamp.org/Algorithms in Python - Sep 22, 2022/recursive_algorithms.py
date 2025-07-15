# Recursion, which originates from the Latin verb, “recurrere” means to “run back”... 
# and this is what the program we’re going to write together is going to do- run back to itself, over and over, 
# as many times as it needs to until the program terminates. 


# ____________________________________________________EXAMPLES__________________________________________________________

# FACTORIALS

def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
#print(iterative_factorial(5))

def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        return temp * n
# print(recur_factorial(5))

# Two-line recursive program to calculate factorial
def recur_factorial(n):
    if n == 1: return n
    else: return n * recur_factorial(n-1)
# print(recur_factorial(5))

# _______________________________________________________________


# PERMUTATIONS

# ITERATIVE PROGRAM FOR PERMUTATIONS

from math import factorial

def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp
s = 'abc'
s = list(s)
permutations(s)


# RECURSIVE PROGRAM FOR PERMUTATIONS

def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range((len(string))):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
# print(permute("ABC", ""))

# _______________________________________________________________


# NO PROGRAM WAS DISCUSSED FOR N-QUEENS PROBLEM