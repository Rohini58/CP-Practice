# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

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
def numSquareSum(n):
    squareSum = 0;
    while(n>0):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum

# method return true if
# n is Happy number
def ishappyprimenumber(n):
    # initialize slow
    # and fast by n
    slow = n;
    fast = n;
    while(True):

        # move slow number
        # by one iteration
        slow = numSquareSum(slow);
        # move fast number
        # by two iteration
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;

    # if both number meet at 1,
    # then return true
    if (slow == 1):
        return True
    else:
        return False

    	