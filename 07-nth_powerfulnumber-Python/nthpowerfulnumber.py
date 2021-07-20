# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


# def get_primefactor(n):
#     count=0
#     if n>1:
#         for i in range(1,n+1):
#             if(n%i)==0:
#                 count=count+1
#         if count==2:
#             return True
#         else:
#             return False

# def nthpowerfulnumber(n):
#     primefactor=get_primefactor
#     # filter to get unique prime factors
#     unique_primefactors = tuple(dict.fromkeys(primefactors))
#     for p in unique_primefactors:
#         if n % p != 0 or n % (p*p) != 0:
#             return False
#     return True

# if nthpowerfulnumber(n):
#     print('%d is powerful' %(n))
# else:
#     print('%d is Not Powerful' %(n))
    


def get_prime_factors(n):
    i = 2
    prime_factors = []
    while i*i <= n:
        if n%i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    if n>1:
        prime_factors.append(n)
    
    return prime_factors

def nthpowerfulnumber(n):
    # get prime factors
    prime_factors = get_prime_factors(n)
    
    # filter to get unique prime factors
    unique_prime_factors = tuple(dict.fromkeys(prime_factors))
    for p in unique_prime_factors:
        if n % p != 0 or n % (p*p) != 0:
            return False
    return True

# Read number from user
# number = int(input('Enter number: '))

# Function call & making decision
if nthpowerfulnumber(number):
    print('%d is powerful' %(number))
else:
    print('%d is Not Powerful' %(number))