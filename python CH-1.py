# # Chapter -2 Strings#
# str1 = "this is a string.\n"
# str2 = 'rahul tiwari.'
# # str3 = """this is a string."""
# # str4 = "this is a string.\n we are creating it in python."
# # print(str4)
# final_str = str1+str2
# print(final_str)

#Indexing#
# str= "Apna college"
# ch =str[0]
# print(ch)
# print(str[5])

#Slicing# Accessing parts of a string.#ending idx is not included.
# print(str[1:4])
# print(str[0:8])
# print(str[5:12])
# print(str[0:len(str)])
# print(str[:8]) #[0:8]

#negative indexing
# print(str[-4:-1])

#string functions#
# str ="i am studying python online."
# print(str.capitalize()
#       )
# name =str(input("enter your name: "))
# print("length of your name is:", len(name))

# Conditional statements 
# #1. if-elif-else(syntax)
# age =21
# if(age>= 18):
#     print("can vote & apply for license")

#practice
#1. WAP to check if a number enetered by the user is odd or even.
#2. WAP to find the greatest of 3 numbers entered by the user.
#3. WAP to check if a number is multiple of 7 or not.

# num= int(input("enter num:")) #1
# rem = num%2
# if(rem == 0):
#     print("even")
# else:
# #     print("odd")

# A = int(input("enter first num"))# 2
# B = int(input("enter second num"))
# C= int(input("enter third num"))

# if(A>=B and A>=C):
#     print("first num is largest",A)
# elif(B>=A and B>=C):
#     print("Second num is largest",B)  
# else:
#     print("Third num is largest", C)

num= int(input("enter num:")) #1
rem = num%7
if(rem == 0):
    print("Multiple of 7")
else:
    print("Not a multiple of 7")