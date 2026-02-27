#Relational Operators -> returns boolean value (True or False) based on the comparison of two values.

# ==, !=, >, <, >=, <=

print(5<7<9>11>=10<8!=7<11>=15) #Here, the expression is evaluated from left to right, and the result is False because operation 9>11 is false. The expression can be broken down as follows:

# 5 < 7 -> True and 7 < 9 -> True and 9 > 11 -> False and 11 >= 10 -> True and 10 < 8 -> False and 8 != 7 -> True and 7 < 11 -> True and 11 >= 15 -> False

print(9==7!=4==6!=5==3!=2==2)

#Here, 9==7 is False, 7!=4 is True, 4==6 is False, 6!=5 is True, 5==3 is False, 3!=2 is True, and 2==2 is True. So the overall result of the expression is False because of the presence of False in the expression.
