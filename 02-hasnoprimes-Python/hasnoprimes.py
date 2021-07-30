# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def isPrime(n):
    if len(n)==1:
        return False
    if (n>1):
        
        for i in range(1,n+1):
            if (n % 2 == 0):
                return False
        return True

def fun_hasnoprimes(l):
    # your code goes here
    for i in (l):
        for j in (i):
            if(isPrime(j)==True):
                return False
        return True



