# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.


    # Your code goes here
def isrotation(x, y):
    s=str(x)
    r=str(y)
    rev=r[::-1]
    if s==r:
        return True
    else:
        
        if len(s)==len(r):
            res=s[len(s)-2:]+s[0:len(s)-2]
            
            if res==r:
                return True
            elif s==rev:
                return True
            else:
                return False      
        else:
            return False

    # your code goes here
    # if len(x)==len(y):
    #     res=x[2:]+x[0:2]
    #     return (res==y)
    # if x==y:
    #     return True
    

