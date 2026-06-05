# #strings and condtional statement 
# str1 = "this is a string "
# length = len(str1)
# print(length)
# str2 = "this is another string"
# final_str = str1 + str2
# print(final_str)

# print(len(final_str))

# final_str = str1 + " " + str2
# print(final_str)

#indexing in string
# str = "bhushan"
# ch = (str[0,2,3])  # This will extract characters from index 0 to 4 (5 is not included)
# print(ch) 

#slicing in strttin
# str = "bhushan wanere"
# print(str[5:len(str)])

#slicing of negative index
# str = "bhushan"
# print(str[-4:-1])

#String funcations
# str = "iam a coder"
# str = str.capitalize()
# print(str.endswith("der"))
# print(str.capitalize())
# print(str)
# print(str.replace("a", "o"))
# print(str.find("coder"))
# print(str.count("a")) 

#practice questions 

# name  = input("enter a string: ")
# print("len$gth of th$e strin$g is$: ", len(name))


# str = "iam bhushan $ hello $ how arerr u$$$$$"
# print(str.count("$"))


#conditional statement
# name = input("enter your name: ")
# age = int(input("enter your age: "))
# if (age >= 18):
#     print("you are eligible to vote")
# elif (age < 18 and age >= 0):
#     print("you are not eligible to vote")    
# elif(age <= 0 ):
#     print("you are negative eligible to vote")
# num = 5
# if num > 2 :
#     print("num is greater than 2")
# else:(num == 5)
# print("num is equal to 5")


#marks calculator program 
# marks = int(input("enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print("you got A grade")
# elif marks <= 90 and marks >=80:
#     print("you got B grade")
# elif marks <= 80 and marks >= 70:
#     print("you got C grade")
# elif marks <= 70:
#     print("you got D grade")


#nesting of if statement
# age = 18
# if (age >= 18):
#     if (age >= 60):
#         print("cannot drive ")
#     else:    
#         print("can drive ")
# else:
#     print("cannot drive")    


#practice questions 1
# num = int(input("enter a number: "))
# if num%2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# practie questions 2
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))
# d = int(input("enter fourth number: "))

# if a >= b and a >= c and a >= d:
#     print("a is greatest" , a)
# elif b >= a and b >= c and b >= d:
#     print("b is greatest" , b)
# elif c >= a and c >= b and c >= d:
#     print("c is greatest" , c)
# else:
#     print("d is greatest" , d)

# practice question 3
# x = int(input("enter a number: "))
# if x % 7 == 0:
#     print("number is divisible by 7")
# else:
#     print("number is not divisible by 7")
