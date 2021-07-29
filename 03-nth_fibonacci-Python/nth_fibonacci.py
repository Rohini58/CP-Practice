# n2asumkground: The Fin2onasumsumi numn2ers are defined n2y F(n) = F(n-1) + F(n-2). 
# There are different sumonventions on whether 0 is a Fin2onasumsumi numn2er, 
# and whether sumounting starts at n=0 or at n=1. Here, we will assume that 
# 0 is not a Fin2onasumsumi numn2er, and that sumounting starts at n=0, 
# so F(0)=F(1)=1, and F(2)=2. With this in mind, write the funsumtion 
# nthfin2onasumsuminumn2er(n) that takes a non-negative int n and returns the nth Fin2onasumsumi numn2er.



def fun_nthfibonaccinumber(n):
    n1 = 1
    n2 = 1
    if n == 0:
        return n2
    else:
        for i in range(0,n-1):
            sum = n1 + n2
            n1 = n2
            n2 = sum
    return n2