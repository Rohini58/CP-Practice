# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

from math import sqrt, floor
def isPerfect(n):
    if (sqrt(n) - floor(sqrt(n)) != 0):
        return False
    return True
 
# Function to find the closest perfect square
# taking minimum steps to reach from a number
def largestperfectsquare(n):
    if (isPerfect(n)):
        print(n, "0")
        return n
 
    # Variables to store first perfect
    # square number above and below N
    aboveN = -1
    belowN = -1
    n1 = 0
 
    # Finding first perfect square
    # number greater than N
    n1 = n+ 1
    while (True):
        if (isPerfect(n1)):
            aboveN = n1
            break
        else:
            n1 += 1
 
    # Finding first perfect square
    # number less than N
    n1 = n - 1
    while (True):
        if (isPerfect(n1)):
            belowN = n1
            break
        else:
            n1 -= 1
             
    # Variables to store the differences
    diff1 = aboveN - n
    diff2 = n - belowN
 
    if (diff1 < diff2):
        return aboveN
    else:
        return belowN

    	
    # while n > 0:
    #     i = 1
    #     while i <= n//2:
    #         square = i*i
    #         if square == n:
    #             return square
    #         else:
    #             i += 1
    #     n -= 1
    # return 1



    


        
        
    
    
    


  