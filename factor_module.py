import math
def fact(n):
    f=[ ]
    for i in range(1,n+1):
        if n%i==0:
            f.append(i)
    return f
def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def prime_factor(n):
    pf=[ ]
    for i in range(1,n+1):
        if n%i==0 and isPrime(i):
            pf.append(i)
    return pf
