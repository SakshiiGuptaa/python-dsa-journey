#Lists in ppython
'''
1. Secondary/ Non-primitive/ Derived data type 
2. Ordered Collection => Elements are organized as in the order of insertion.
3. Mutable => We can change the elements of a list after it is created.
4. Heterogeneous => A list can contain elements of different data types.
5. Duplicates => A list can contain duplicate elements.
6. Indexing and Slicing => We can access individual elements of a list using indexing and slicing.
7. List Methods => Python provides various built-in methods to manipulate lists, such as append(), extend(), insert(), remove(), pop(), sort(), reverse(), etc.
8. List Comprehension => A concise way to create lists using a single line of code

'''
l = [1, "Hello", 3.14, True, [1, 2, 3], (4, 5), {'name': 'Alice', 'age': 30}, None]

#Empty list
empty_list = []
lis = list() # using list constructor

#List methods

#Modification/ Insertion in a list
lis.append(10) # adds an element to the end of the list
lis.insert(1, "World") # inserts an element at a specific index
lis.extend([1, 2, 3]) # adds all the elements of an iterable (e.g., another list) to the end of the list
lis[1] = "Python" # Modifying an element at a specific index
print(lis) # [10, 'Python', 1, 2, 3]
lis[2:4] = ["value at index 2", "value at index 3"] # Removing an element using slicing
print(lis) # [10, 'Python', 'value at index 2', 'value at index 3', 3]

#Deletion in a list
lis.remove("value at index 2") # removes the first occurrence of a specific value from the list
print(lis) # [10, 'Python', 'value at index 3', 3]
lis.pop(2) # removes and returns the element at a specific index
print(lis) # [10, 'Python', 3]

lis.clear() # removes all the elements from the list
print(lis) # []

li=[1,2,3,4,5]
del li # deletes the entire list  
print(li) # NameError: name 'li' is not defined (because the list has been deleted)

#Some other methods

'''
reverse() => Reverses the order of the elements in the list.
sort() => Sorts the elements of the list in ascending order (by default) or in descending order (if the reverse parameter is set to True).
count() => Returns the number of occurrences of a specific value in the list.
index() => Returns the index of the first occurrence of a specific value in the list.
copy() => Returns a shallow copy of the list.
'''