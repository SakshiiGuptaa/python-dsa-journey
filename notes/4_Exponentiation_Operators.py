#exponentiation operator
#right to left associativity
print(2**3) # 8
print(2**3**2) # 512 (2**(3**2))

#Logical Operators
#and(&), or(|), not(~), xor(^)

#short curcuiting

print(False and True) # False (Here, right side true is not evaluated because the left side is already false, so the overall result will be false regardless of the right side. This is known as short-circuit evaluation, where the second operand is not evaluated if the first operand already determines the result.)

print(True or False) # True (Here, right side false is not evaluated because the left side is already true, so the overall result will be true regardless of the right side. This is another example of short-circuit evaluation.)

#Examples

a=1.2
b=0
# x = a & b #(True & False) = False
# x = 1.2 & 0 #= 0 #(because 1.2 is treated as True and 0 is treated as False, so the result of the bitwise AND operation is False, which is represented as 0 in Python.)

# y = a | b #(True | False) = True
# y = 1.2 | 0 = 1.2 #(because 1.2 is treated as True and 0 is treated as False, so the result of the bitwise OR operation is True, which is represented as 1 in Python.)

#Here, no need to check the value of b, because a is true and we have or operation, so the overall result will be true regardless of the value of b. This is an example of short-circuit evaluation, where the second operand is not evaluated if the first operand already determines the result.

#XOR (^) -> Both inputs are different -> 1, else 0
print(True ^ False) # True (Here, the result is True because the two operands are different. The XOR operator returns True if the operands are different and False if they are the same.)

#Shift Operators

#Performs operation on the binary digits(1|0)
#<< left shift -> shifts bits to the left and fills the rightmost bits with 0
#>> right shift -> shifts bits to the right and fills the leftmost bits with 0



#value << count => value * (2**count)
#value >> count => value // (2**count)



#Formula is aplicable only for non-negative decimal numbers, for negative numbers we have to convert them into their binary representation and then perform the shift operation.

#For Right Shift (>>), no need to check for the sign manitude or no need to add bits of 0's in the left, because we have to fill the leftmost bits with 0's after shifting the bits to the right, so the sign of the number will not affect the result of the right shift operation.

#Example
print(5<<1) # 10 (5 * 2^1) , convert 5 into binary and convert it into sign magnitude form(into 8 bits add 0's in the left of the binary value we get), then shift the bits to the left by 1 position and fill the rightmost bit with 0, which gives us 10 in decimal.

# 5 -> 00000101 (binary representation of 5 in 8 bits)
# if we have 1 in the Left most bit then it is negative number and if we have 0 in the left most bit then it is positive number, this is called sign magnitude form.
# We have to add 8 more bits of 0's in the left, if we have 1 as the LMB of the binary representation of the number -> This number will become of 16 bits, and we have to add 8 more bits of 0's in the left, if we have 0 as the LMB of the binary representation of the number, to make it 8 bits. 

print(5<<3) # 5 * 2^3 = 40 (5 * 8) , convert 5 into binary and convert it into sign magnitude form(into 8 bits add 0's in the left of the binary value we get), then shift the bits to the left by 3 positions and fill the rightmost bits with 0, which gives us 40 in decimal.

#Example

a = 17
b = 43 
x = a<<2 # 17 * 2^2 = 68
y = b>>3 # 43 // 2^3 = 5

print(x,y) # 68 5

i = 0o23 #prefix 0o for octal numbers, 0o23 is 19 in decimal
j = 0x47
k = 0b11001001

a = (i<<2) + (j>>3)
b = (k<<3) + (i>>2)
c = (j<<2) + (k>>3)

print(a+b+c)    #2005

# Convert All number into decimal number system first 
#Then, apply the formula of right and left shift operation
