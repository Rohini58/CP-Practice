# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
    # i=index
    s=abs(digit)//(10**k)
    if(s==0):
        return 0
    else:
        return s%10

