#Arithmetic -> +, -, *, /, //, %, **
# print(15/3) # division operator returns a float 5.0
# print(10/3) # division operator returns a float 3.3333333333333335
# print(15.6/3) # division operator returns a float 5.2

# print(10//3) # floor division operator returns an integer 3 when both operands are integers
# print(10.0//3) # floor division operator returns a float 3.0 when at least one operand is a float
# print(15.6//3) # floor division operator returns a float 5.0 when at least one operand is a float

# / and // for signed numbers

#floor division rounds towards negative infinity, while true division rounds towards zero. This means that for negative numbers, floor division will round down to the next lowest integer, while true division will round up towards zero.

# print(-10/3) # true division returns -3.3333333333333335
# print(-10//3) # floor division returns -4

# % modulus operator returns the remainder of the division of the left operand by the right operand

# one of the properties of the modulus operator is that it always returns a result with the same sign as the divisor (the right operand). This means that if the divisor is positive, the result will be positive or zero, and if the divisor is negative, the result will be negative or zero.

#when both inputs are of different signs -> a%b = b - (a%b)
print(16%3)
print(16%-3)
print(-16%-3)
print(-16%3)

#Find Results

print(14.3//4) 

print(3.7/2)

print(15.75//-4)  #-4.0

print(19%-4) # -4-(19%-4) = -4-(-3) = -1

print(-23%7)  # 7-(-23%7) = 7-2 =5

print(-43%-6) #-1

print(63%19) #6