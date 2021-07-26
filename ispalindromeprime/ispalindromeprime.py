
# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)

def ispalindromeprime(n):
    
    reverse=int(str(n)[::-1])
    if n==reverse:
        count=0
        # if x>1:
        for i in range(1,n+1):
            if(n%i)==0:
                count = count+1
        if count == 2:
            return True
        else:
            return False
    else:
        return False
print(ispalindromeprime(2))