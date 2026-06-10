#file input and output 
# types of file 
        #text files
        #binary files 

# f = open("demo.txt","r")
# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)
# f.close()


# wririting of file 
# f = open("demo.txt","w")
# f.write("i want to go homne ")

# f.close()

# f = open("hello.txt","w")
# f.write("hello")

# f = open("demo.txt","r+")
# f.write("abc")

# print(f.read())
# f.write("abc")
# f.close()

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f :
#     f.write("new data")



# # deleting a file
# import os
# os.remove("demo.txt")

# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java" , "python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)



# def check_word():
#     word = "learning"

#     with open("practice.txt", "r") as f:
#         data = f.read()

#         if data.find(word) != -1:
#             print("Found")
#         else:
#             print("Not Found")


# def check_for_line():
#     word = "learning"
#     line_no = 1
#     data = True

#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()

#             if word in data:
#                 print("Word found at line:", line_no)
#                 return

#             line_no += 1

#     print("Word not found")


# check_word()
# check_for_line()


# 2nd practice queestion

with open("practice.txt", "r") as f:
    data = f.read 
    print(data())


    # num = ""
    # for i   in range(len(data())):
    #     if(data[i] == "," ):
    #         print(int(num))
    #         num =""
    #     else:
    #         num += data[i]

    nums = data.split(",")
    print(nums)
