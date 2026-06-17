#oops 
# basic of class
# creating class 
# class student :
#     name = "bhushan"


# # # creating object
# s1 = student()
# print(s1.name)

# class car:
#     color ="blue"
#     brand ="mercedes"


# car1 = car()
# print(car1.color)

# car2 = car()
# print(car2.brand)


# class student:
#     # deafault constructors
#     college_name = "ABC college"
#     name = " randomm" # class attribute
#     def __init__(self):
#         pass
#     #   parametrizedd constructors
#     def __init__(self,name,marks):  # self is important ( argument)
#         self.name = name  # instance attribute obj . class
#         self.marks = marks #instance attribute
#         print("adding new studnrt in database")
#     def welcome(self):
#         print("welcomre student")
#     def get_marks(self):
#         return self.marks
# s1 = student("karan",79)
# print(s1.name,s1.marks)

# s2 = student("arjun",69)
# print(s2.name,s2.marks) 


# print(s1.get_marks())
# class :- data , methods

# methods are funcastions that belongs to objects  

# practice wurstions
# class student:
#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks

#     @staticmethod #decorator 
#     def hello():
#         print("hrllo bhushann")       

#     def get_avg(self):
        
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name,"your avg score is:-", sum/3)



# s1 = student("jarvis",[69,79,57])            
# s1.get_avg()

# s1.name="bhushan"
# s1.get_avg()
# s1.hello()



#abstraction in python

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started")

# car1 = car()
# car1.start()        


#encapsulation
# wrapping data and fucntions into a single unit (object)

# pracrtice

#2 create class with 2 attrituburtes - balance & account no.
   # create methods for debbit , credit & prinitng the balance

class Bank:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("Total balance =", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Bank(10000, 12345)

acc1.debit(1000)
acc1.credit(50000)
acc1.credit(400000)
acc1.debit(4500)