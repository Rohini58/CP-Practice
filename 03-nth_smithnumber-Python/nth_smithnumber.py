# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def isprime(x):
    count=0
    if x>1:
        for i in range(1,x+1):
            if(x%i)==0:
                count = count+1
        if count == 2:
            return True
        else:
            return False
  
def sum_of_digits(x):
    if x <= 10:
        return x
    
    sum = 0
    
    while(x != 0):
        sum += x % 10
        x = x // 10
    return sum

def factorsofnumber(x):
    if x <= 1:
        return False
    
    primefactors = list()
    sumfactors = 0
    d = 2
    
    while(d <= x):
        if isprime(d) and x % d != 0:
            primefactors.append(d)
            x = x // d
        else:
            d += 1

    for i in primefactors:
        sumfactors += sum_of_digits(i)

    return (sumfactors )


def solve (n):
    
    if factorsofnumber(n) == sum_of_digits(n):
        return  1
    else:
        return 0

  

def fun_nth_smithnumber(x):
    found=1
    guess=1
    while(found<=x):
        guess+=1
        if(solve(guess)):
            found+=1
    return guess

   

   
