# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
# def checkproperty309(n):
#     n=pow(n,5)
#     m=[]
#     while(n):
#         rem=n%10
#         m.append(rem)
#         n=n//10
#     x=[0,1,2,3,4,5,6,7,8,9]
#     for i in x:
#         if(i not in m):
#             return False
#     return True
import math
def checkproperty309(n):
    #flag=True
    x=int(math.pow(n,5))
    #print(x)
    y=str(x)
    list=["0","1","2","3","4","5","6","7","8","9"]
    for i in list:
        #print(i)
        if i not in y:
            return False
    return True
def nthwithproperty309(n):
    count=0
    i=1
    res=0
    while(count<=n):
        if(checkproperty309(i)):
            count+=1
            res=i
        i+=1
    return res

    # Your code goes here
