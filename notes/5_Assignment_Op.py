#Assignment Operators
#It assigns the RHS result to the LHS variable.
a = 5


# == vs =

a=3
b=5

c = a = b # c=5 (Here, the assignment operator (=) is evaluated from right to left, so first b is assigned to a, and then the result of that assignment (which is 5) is assigned to c. So the final values of a and c will both be 5.)

d = a == b # d = True (Here, the relational operator (==) is evaluated first  because it has more precedence, so it compares the values of a and b. Since a is now 5 (after the previous assignment) and b is also 5, the comparison returns True, which is then assigned to d.)

print(c,d) # 5 True

#Compound Assignment Operators Or Shorthand Assignment Operators
# +=, -=, *=, /=, //=, %=, **=

a = 5
a += 3 # a = a + 3
print(a) # 8

a -= 2 # a = a - 2
print(a) # 6

a *= 2 # a = a * 2
print(a) # 12

a /= 3 # a = a / 3
print(a) # 4.0

a //= 2 # a = a // 2
print(a) # 2.0

a %= 3 # a = a % 3
print(a) # 2.0

a **= 2 # a = a ** 2
print(a) # 4.0

x -= y-z
x = x - (y-z) # Here, the expression on the right-hand side is evaluated first, so y-z is calculated first, and then that result is subtracted from x. Finally, the result of that subtraction is assigned back to x.