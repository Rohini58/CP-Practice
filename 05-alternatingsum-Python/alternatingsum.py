# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.





    # l=[]
    # l1=[]
    # for i in a:
    #     if i%2==0:
    #         l.append(i)
    #     else:
    #         l1.append(i)
    # sub=l-l1
    # return sub
            

def readArray():
    a = []
    l = int(input())
    for i in range(l):
        a.append(int(input()))
    return a

def fun_alternatingsum(a): 
    # your code goes here
    flag=True
    res=0
    for i in a:
        if(flag==True):
            res=res+i
            flag=False
        else:
            res=res-i
            flag=True
    return res

            
            
    



# def alternatingSum(L):
#     altSum=0
# for i in range(len(L)):
# if i%2==0:
# altSum+=L[i]
# else:
# altSum-=L[i]
# return altSum