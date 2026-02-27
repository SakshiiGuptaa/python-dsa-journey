# Creation of list
arr =[10,20,30,40]

#Accessing elements
print(arr[0]) #10
print(arr[-1]) #40

#Modifiying elements
arr[1]= 99
print(arr) #[10, 99, 30, 40]

#Appending (Add at end)
arr.append(50)
print(arr) #[10, 99, 30, 40, 50]

#Inserting (Add at specific index)
arr.insert(2, 25)
print(arr) #[10, 99, 25, 30, 40, 50]

#Extending (Merging another list)
new_list = [60, 70, 80]
arr.extend(new_list)
print(arr) #[10, 99, 25, 30, 40, 50, 60, 70, 80]

#Removing by value
arr.remove(99)
print(arr) #[10,25, 30, 40, 50, 60, 70, 80] first occurrence of 99 is removed

#Removing by index
arr.pop(2) #removes element at index 2 (30)
print(arr) #[10, 25, 40, 50, 60, 70, 80]

#Searching
print(arr.index(40)) #2 Returns index of first occurrence of 40
print(60 in arr) #Return True if 60 is in arr, else False

#Length
print(len(arr))

#Slicing
print(arr[1:4]) #[25, 40, 50] elements from index 1 to 3
print(arr[-1:-4:-1]) #[80, 70, 60] last 3 elements in reverse order

#Reversing
arr.reverse() #Reverses the list in place
print(arr) #[80, 70, 60, 50, 40, 25, 10]

#Sorting
arr.sort() #Sorts the list in ascending order
print(arr) #[10, 25, 40, 50, 60, 70, 80]

arr.sort(reverse=True) #Sorts the list in descending order
print(arr) #[80, 70, 60, 50, 40, 25, 10]