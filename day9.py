# # class student:
# #     def __init__(self,name):
# #         self.name = name 

# # s1 = student("bhushan")        
# # print(s1.name)
# # del s1.name
# # print(s1.name)



# #   private attributes & methods 

# # class account:
# #     def __init__(self,acc_no,acc_pass):
# #         self.acc_no = acc_no
# #         self.__acc_pass = acc_pass # just add "__" befoire the object 

# #     def reset_pass():
# #         print("acc1.__acc_pass")
# # acc1 = account("12343","abcde")


# # print(acc1.acc_no)
# # print(acc1.__acc_passacc_pass)   
# # class person:
# #     __name = "unknown"
# #     def __hello(self):
# #         print("hello person")
# #     def welcome(self):
# #         self.__hello()

# # p1 =  person()


# # print(p1.welcome())


# #inheritance !!!!!!!!!
# # single inhertiance 
# # class Car:
# #     color = "yellow"

# #     @staticmethod
# #     def start():
# #         print("Car started.")

# #     @staticmethod
# #     def stop():
# #         print("Car stopped.")


# # class ToyotaCar(Car):
# #     def __init__(self, name):
# #         self.name = name


# # car1 = ToyotaCar("Fortuner")
# # car2 = ToyotaCar("WagonR")

# # print("Car Name:", car1.name)
# # print("Car Color:", car1.color)

# # car1.start()
# # car1.stop()

# # multilevel inheritance
# # class Car:
# #     @staticmethod
# #     def start():
# #         print("car started..")

# #     @staticmethod
# #     def stop():
# #         print("car stopped.")


# # class ToyotaCar(Car):
# #     def __init__(self, brand):
# #         self.brand = brand


# # class Fortuner(ToyotaCar):
# #     def __init__(self, type):
# #         self.type = type


# # car1 = Fortuner("diesel")
# # car1.start()

# # multiple inheritance 
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#     varC = "welcome to class c" 



# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = ToyotaCar("Prius", "Electric")

# print("Car Name:", car1.name)
# print("Car Type:", car1.type)


# class Person:
#     name = "unknown"

#     @classmethod
#     def changename(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changename("Rohit")

# print(p1.name)
# print(Person.name)



#property decorator

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return (self.phy + self.chem + self.math) / 3


# stud1 = Student(67, 89, 98)

# print(stud1.percentage)

# stud1.phy = 86
# print(stud1.percentage)


# polymorphism 

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real, "i +", self.img, "j")
    def __add__(self,num2): # addtion using dunder function 
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex( newReal , newImg)
    def __sub__(self,num2): # sub using dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex( newReal , newImg)

num1 = Complex(1, 3)
num1.shownumber()


num2 = Complex(2,4)
num2.shownumber()


num3 =  num1 - num2
num3.shownumber()