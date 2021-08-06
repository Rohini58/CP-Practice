# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
# import math
# def isPrime(n):
#     if n==2 or n==3:
#         return True
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return False
#     return True
# def sumDigits(n):
#     s=0
#     while(n>0):
#         s=s+n%10
#         n=n//10
#     return s
        
        
# def factorSum(n,d):
#     pfs=0
#     while(n%d==0):
#         pfs=pfs+d
#         n=n//d
#     return pfs,n            

# def isSmith(n):
#     sd=sumDigits(sumDigits(n))
#     nit=n//2+1
#     pfs,n=factorSum(n,2)
    
#     for i in range(3,nit,2):
#         p,n = factorSum(n,i)
#         pfs=pfs+p
#     ps=sumDigits(sumDigits(pfs))
#     return sd==ps
 
def fun_nth_smithnumber(n):
    i=1
    m=0
    while(i<n):
        if (isSmith(m)):
            i=i+1
        m=m+1
    return m        
print(fun_nth_smithnumber(1))

import math
def fun_nth_smithnumber(n):
   count=0
   x=1
   y = 0
   while(n+1!=count):
       if(isSmith(x)):
           count+=1
           y = x
       x+=1
   return y
 
def isPrime(n):
    if n==2 or n==3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
 
def isSmith(n):
   if(isPrime(n)!=True):
       k = n
       factors = []
       sumoffactors=0
       sumofnumbers=0
       rem=0
       srem = 0
       stotal = 0
       x =0
       z =0
       ve = 0
       ro = 0
       if n==1:
           return False
       for i in range(2,(n//2) + 1):
           if(isPrime(i)==True) and (n%i==0):
               factors.append(i)
          
       for an in str(n):
           ro+=int(an)
      
       li=[]
       for i in factors:
           while (k%i==0 and k!=0):
               li.append(i)   
               sumoffactors+=i
               k=k//i
      
       e = 0       
       for j in li:
           if(j>9):
               for d in str(j):
                   e+=int(d)
           else:
               e+=j
      
       if(ro==e):
           return True
       else:
           return False
