# ==========================================
# FUNCTIONS AND RECURSION
# ==========================================


# ------------------------------------------
# Function: Sum of Two Numbers
# ------------------------------------------

# def sum(a, b):  # a and b are arguments
#     s = a + b
#     return s

# print(sum(2, 3))


# ------------------------------------------
# Function: Calculate Sum
# ------------------------------------------

# def cal_sum(a, b):
#     return a + b

# sum = cal_sum(4, 5)
# print(sum)


# ------------------------------------------
# Function: Print Hello
# ------------------------------------------

# def printhello():
#     print("hello")

# printhello()


# ------------------------------------------
# Function: Calculate Average
# ------------------------------------------

# def cal_avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# cal_avg(89, 34, 67)


# ------------------------------------------
# Function: Calculate Product
# ------------------------------------------

# def cal_prod(a=1, b=1):
#     print(a * b)
#     return a * b

# cal_prod()


# ==========================================
# PRACTICE PROBLEMS
# ==========================================


# ------------------------------------------
# Problem 1: Print Length of List
# ------------------------------------------

# cities = ["delhi", "mumbai", "chennai"]

# def print_len(list):
#     print(len(list))

# print_len(cities)


# ------------------------------------------
# Problem 2: Print Elements of a List
# ------------------------------------------

# heroes = ["thor", "ironman", "batman"]

# def print_len(list):
#     print(len(list))

# print(heroes[0], end="")
# print(heroes[1], end="")

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)


# ------------------------------------------
# Problem 3: Factorial of a Number
# ------------------------------------------

# n = 6

# def cal_fact(n):
#     fact = 1

#     for i in range(1, n + 1):
#         fact *= i

#     print(fact)

# cal_fact(6)


# ------------------------------------------
# Problem 4: USD to INR Converter
# ------------------------------------------

# def con(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "usd =", inr_val, "INR")

# con(89)


# ------------------------------------------
# Problem 5: Even or Odd
# ------------------------------------------

# def check_num(num):
#     if num % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"

# n = int(input("Enter a number: "))
# print(check_num(n))


# ==========================================
# RECURSION
# ==========================================


# ------------------------------------------
# Recursive Function Example
# ------------------------------------------

# def show(n):
#     if n == 0:  # Base Case
#         return

#     print(n)
#     show(n - 1)
#     print("end")

# show(5)


# ------------------------------------------
# Recursive Factorial
# ------------------------------------------

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)


# ==========================================
# RECURSION PRACTICE PROBLEMS
# ==========================================


# ------------------------------------------
# Problem 1: Sum of First n Natural Numbers
# ------------------------------------------

# def calc_sum(n):
#     if n == 0:
#         return 0

#     return calc_sum(n - 1) + n

# sum = calc_sum(5)
# print(sum)


# ------------------------------------------
# Problem 2: Print List Using Recursion
# ------------------------------------------

# def print_list(list, idx=0):
#     if idx == len(list):
#         return

#     print(list[idx])
#     print_list(list, idx + 1)

# fruits = ["mango", "banana", "apple", "lichie"]

# print_list(fruits)