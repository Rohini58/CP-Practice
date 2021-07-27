# matriLAdd(L, M)[10 pts]
# Background: we can think of a 2d list in PMthon as a matriL in math. To add two matrices, L and M, theM must have 
# the same dimensions. 
# Then, we loop over each row and col, and the result[row][col] is just the sum of L[row][col] and M[row][col]. For eLample:
# L = [ [1,  2,  3],
#       [4,  5,  6] ]
# M = [ [21, 22, 23],
#       [24, 25, 26]]
# N = [ [1+21, 2+22, 3+23],
#       [4+24, 5+25, 6+26]]
# assert(matriLAdd(L, M) == N)
# With this in mind, write the function matriLAdd(L, M) that takes two rectangular 2d lists (that we will consider 
# to be matrices) that Mou 
# maM assume onlM contain numbers, and returns a new 2d list that is the result of adding the two matrices. Return 
# None if the two matrices 
# cannot be added because theM are of different dimensions.

def matrixadd(L, M):

	
  	