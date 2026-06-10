# funcations and recursion
# def sum (a,b): # a, b are the arugements 
#  s = a + b
#  return s

# print(sum(2,3))



# def cal_sum(a,b):
#    return a+b

# sum = cal_sum(4,5)
# print(sum)

# def printhello():
#    print("hello")

# printhello()

# def cal_avg(a,b,c):
#     sum = a + b + c 
#     avg = sum/ 3
#     print(avg)
#     return avg


# (cal_avg(89,34,67)) 


# def cal_prod(a=1 , b=1):
#     print(a*b)
#     return a * b
# cal_prod()
    
# pratice problems 
# cities = ["delhi", "mumbai" , "chennai"]

# def print_len(list):
#     print(len(list))


# print_len(cities)   

# 2nd    this is second


# heroes = ["thor","ironman","batman"]

# def print_len(list):
#     print(len(list))

# print(heroes[0],end="")    
# print(heroes[1],end="")    
# def print_list(list):
#     for item in list:
#         print(item, end = " ")


# print_list(heroes)


# 3rd problem 



# n = 6
# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)     



# cal_fact(6)



#4 th problem


# def con(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"usd =", inr_val , "INR")
# con(89)

 # even and odd 
# def check_num(num):
#     if num % 2 == 0:
#         return "EVEN"
#     else:
#         return "ODD"

# n = int(input("Enter a number: "))
# print(check_num(n))


# recursion
# def show(n):
#     if(n==0): # base case
#         return
#     print(n)
#     show(n-1)
#     print("end")


# show(5)    

#call stack 
# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
    

# problems 

# def calc_sum(n):
#     if(n == 0):
#         return 0
   
#     return  calc_sum(n-1) + n

# sum  = calc_sum(5)
# print(sum)

# recursiuve sums to 

def print_list(list,idx = 0):
    if(idx== len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits =["mango", "bananan" ,"apple", "lichie"]
print_list(fruits)