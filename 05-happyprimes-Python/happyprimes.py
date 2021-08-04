# # Happy Primes [20 pts]
# # Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# # some thought, we see that no matter what number we start with, when we keep replacing 
# # the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# # unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# # (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# # right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# # And that's top-down design! Here we go.... 
# # Note: the autograder will grade each of the following functions, so they are required. 
# # However, they also are here specifically because they are just the right helper 
# # functions to make nthHappyNumber(n) easier to write!

def ishappynumber(n):
    	# your code goes here
	if n<1:
		return False
	sum = 0
	while(n>0):
		sum+= (n % 10) * (n % 10)
		n = n//10
	if sum == 1:
		return True 
	elif sum == 4:
		return False
	else:
		return ishappynumber(sum)

def isprime(x):
    count=0
    if x>1:
        for i in range(1,x+1):
            if(x%i)==0:
                count = count+1
        if count == 2:
            return True
        else:
            return False

def ishappyprimenumber(n):
    # Your code goes here
    if(ishappynumber(n) and isprime(n)):
        return True
    else:
        return False
