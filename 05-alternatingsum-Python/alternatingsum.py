# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.



def fun_alternatingsum(a):
    altSum=0
    for i in range(len(a)):
        if i%2==0:  #i  takes index not a value 
            altSum+=a[i]
        else:
            altSum-=a[i]
    return altSum  

# def readArray():
#     a = []
#     l = int(input())
#     for i in range(l):
#         a.append(int(input()))
#     return a

# def fun_alternatingsum(a): 
#     # your code goes here
#     # flag=True
#     # res=0
#     # for i in a:
#     #     if(flag==True):
#     #         res=res+i
#     #         flag=False
#     #     else:
#     #         res=res-i
#     #         flag=True
#     # return res

            
            
    



# def alternatingSum(L):
    # altSum=0
    # for i in range(len(a)):
    #     if i%2==0:  #i  takes index not a value 
    #         altSum+=a[i]
    #     else:
    #         altSum-=a[i]
    # return altSum