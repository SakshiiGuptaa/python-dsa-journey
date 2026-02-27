#Identity Operator
# is, is not

a = "Gate"
b = "Exam"
c = "Gate"  

print(a is c) # True (Here, the is operator checks if a and c refer to the same object in memory. Since both a and c are assigned the same string "Gate", they refer to the same object, so the result is True.)

print(a is not b) # True (Here, the is not operator checks if a and b do not refer to the same object in memory. Since a refers to the string "Gate" and b refers to the string "Exam", they do not refer to the same object, so the result is True.)

#Membership Operators

# in, not in

a = "Gate"
b = "G" in a # True (Here, the in operator checks if the substring "G" is present in the string "Gate". Since "G" is indeed a part of "Gate", the result is True.)

c = "X" not in a # True (Here, the not in operator checks if the substring "X" is not present in the string "Gate". Since "X" is not a part of "Gate", the result is True.)

#Example 
a = [10, 20, 30, 40, 50]
i = 10
while i<= 50: # 10, 25, 40, 55(stops the loop because 55 is greater than 50, condition becomes false)
    print(i in a) # True(10 in a) False(25 in a) True(40 in a)  
    i = i + 15 #25, 40, 