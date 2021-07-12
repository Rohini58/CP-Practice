# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
    firstdigit= hand // 100
    seconddigit=(hand%100) // 10
    thirddigit=(hand%10) 
    return firstdigit,seconddigit,thirddigit

#  1.231// 100 = 2
#  2.100)231(2
#      200
#      ----
#      31
#      31//10=3
# 3.10)231(23
#      20
#      ----
#      31
#     we have to divide only once
     
	
# def handTodice(hand):
# 	x=str(hand)
# 	return tuple(int(i) for i in x)
	
     
 
 


