# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs

# import math
def fun_eggcartons(eggs):
	# your code goes here
	if eggs==0:
		return 0
	if eggs%12==0:
		return eggs//12
	else:
	 	return (int(eggs//12)+1)

# 1..12%12==0
#    		12//12=1
# 2...13
# 	else: 13//12=1     1+1=2

#   return math.ceil(eggs/12)

