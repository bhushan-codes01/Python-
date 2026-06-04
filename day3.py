#Lists and tuples in Python

#Lists 

# marks1 =  87.8
# marks2 =  90.98
# marks3 =  78.78
# marks = [87.8, 90.98, 78.78] #List of marks
# print(marks)
# print(type(marks))
# print(marks[1]) #Accessing the first element of the list
# print(marks[0]) #Accessing the first element of the list

# student =["bhushan", 21, "bhushan@gmail.com", 9876543210] #List of student details
# print(student,len(student))
# print(type(student))

# print(student[0]) #Accessing the first element of the list
# student[0] = "bhushan patil" #Updating the first element of the list
# print(student)

#list slicing
# marks = [87.8, 90.98, 78.78, 85.5, 92.3]
# print(marks[1:4]) #Slicing the list from index 1 to 3
# print(marks[-3:-1])

#list methods
# marks = [87.8, 90.98, 78.78, 85.5, 92.3]
# marks.append(35.45)
# print(marks)
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)
# marks.reverse()
# print(marks)
# marks.insert(2, 80.5)
# print(marks)
# marks.pop(2) #Removes the element at index 2
# print(marks)
# marks.remove(85.5) #Removes the first occurrence of 85.5
# print(marks)

#tuples In Python
# marks = (87.8, 90.98, 78.78, 85.5, 92.3) #Tuple of marks
# print(marks[1])
# print(type(marks))
# tup = (1,)
# print(tup)
#methods of tuple
# print(marks.count(85.5))
# print(marks.index(85.5))


#praactice questions 

# enter the name of three movies and store them in a list. Then print the list.
# movies = []

# movies.append(input("Enter first movie name: "))
# movies.append(input("Enter second movie name: "))
# movies.append(input("Enter third movie name: "))

# print("Movies List:", movies)

#check if list contains a palindrOME
# list1 = ["n","a","m","a","n"]

# copy_list = list1.copy()
# copy_list.reverse()

# if list1 == copy_list:
#     print("Palindrome")
# else:
#     print("Not a palindrome")



#grade 
#                                                     