# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


def kaprekar(n):
    s=str(n*n)
    for i in range(1,len(s)):s
        t=int(s[:i]) + int(s[i:])
        if t==n:
            return True
            exit()
    return False
def fun_nth_kaprekarnumber(n):
    f = 0
    g = 0
    while(f<=abs(n)):
        g+=1
        if(kaprekar(g)):
            f+=1
    return g
print(fun_nth_kaprekarnumber(5))
    