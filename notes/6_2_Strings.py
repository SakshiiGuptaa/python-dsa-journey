i = "EXAMINATION"

# Access of individual characters of given string using indexing

# Indexing can be positive or negative.
# In general, indexing starts from the beginning of the string 
# Positive indexing starts from 0 , from beginning of a string and ends with len(string)-1.
# Negative indexing starts from -len(string), from beginning of a string goes till end at (-1).

'''EXAMINATION

E  X  A  M  I  N  A  T  I  O  N
0  1  2  3  4  5  6  7  8  9  10(len(string)-1)           length of string = 11
-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

-11<-10<-9<-8<-7<-6<-5<-4<-3<-2<-1
'''

print(i[7]) # T (Here, the character at index 7 is 'T')
print(i[-4]) # T (Here, the character at index -4 is 'T')

#How to access substring of given string using slicing

#using slice operator [start:stop:step]
# start is the index from which slicing starts (inclusive)      default value is 0
# stop is the index at which slicing ends (exclusive)           default value is len(string)
# step is the number of characters to skip while slicing (optional)   default value is +1
# In general, all options are optional, but at least one of start or stop must be provided.

string = "EXAMINATION"

print(string[0:7]) # EXAMINA (Here, the substring from index 0 to 6 is 'EXAMINA')
print(string[0:10:2]) # EAIAI
print(string[3: :3]) # string[3:11:3] # MA0
print(string[-8:-2]) # MINATI
print(string[-11 :]) # EXAMINATION (Here, the substring from index -11 to end of the string is 'EXAMINATION') stop index is 0 (because starting is -ve so -11+1 = -10 till -1) and step is 1 (default value)

print(string[-10: -2: 2]) # XMNT

print(string[ : : -2]) # NIAIAE (It will starts from the end of the string and goes till the beginning of the string with a step of -2, which means it will skip one character and take the next character in reverse order)

print(string[4:5]) #I (Here, the substring from index 4 to 4 is 'I') stop index is 5 (exclusive) and step is 1 (default value)

print(string[2:-3]) # AMINAT (Here, the substring from index 2 to -4 is 'AMINAT') stop index is -3 (exclusive) and step is 1 (default value)
print(string[1 : -7 : -2]) # Nothing is printed because the start index (1) is less than the stop index (-7) and the step is negative (-2), which means it will try to slice the string in reverse order, but since the start index is less than the stop index, it will not be able to slice any characters and will return an empty string.
print(string[1 : -7 : -1]) # In case of negative step, the current index or start should be greater than the stop index, then, only we will get any value

#string = "EXAMINATION"
print(string[-9: 3 : 3]) #A (Here, the substring from index -9 to 2 with a step of 3 is 'A') stop index is 3 (exclusive) and step is 3. The slicing starts from index -9 which is 'A' and then it skips 2 characters and takes the next character at index -6 which is 'M', but since the stop index is 3 (exclusive), it does not include the character at index 3 which is 'M' and returns 'A' as the result.

print(string[4:4]) # Nothing is printed because the start index (4) is equal to the stop index (4) and the step is 1 (default value), which means it will try to slice the string from index 4 to index 4, but since the start and stop indices are the same, it will not be able to slice any characters and will return an empty string.

#split method

S = "Hello How are you"
print(S.split()) #['Hello', 'How', 'are', 'you']
print(S.split('o')) #['Hell', ' H', 'w are y', 'u']

