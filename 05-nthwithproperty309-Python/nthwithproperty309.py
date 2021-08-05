# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
def property309(n):
    n=pow(n,5)
    m=[]
    while(n):
        rem=n%10
        m.append(rem)
        n=n//10
    x=[0,1,2,3,4,5,6,7,8,9]
    for i in x:
        if(i not in m):
            return False
    return True

def nthwithproperty309(n):
    # Your code goes here
    if(n == 0):
        return 309
    x = 0
    y = 308
    while(x<=n):
        y+=1
        if(property309(y)):
            x+=1
    return y

    # Your code goes here
