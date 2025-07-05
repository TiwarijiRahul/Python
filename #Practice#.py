#Practice#
# Basic Fundamentals#
# 1
# print("hello world")
# 2.#
# x = int(input("enter num : "))
# y = int(input("enter num : "))
# sum = x+y
# print("sum is :", sum)
# 3.
# my_num = int(input("enter num :"))
# if(my_num > 0):
#     print(" num is positive")
# elif(my_num < 0):
#     print(" num is negative")

# else:
#     print("num is 0")

# 4
# Num_ = int (input("num is :"))
# if(Num_ %2 == 0):
#     print("num is even")
# else:
#     print("num is odd")
#5 
# a = 9
# b = 10
# c = 6
# maximun = max(a,b,c)
# print("max num is :", maximun)
#6#
# n= int(input("enter num: "   ))
# fact = 1

# for i in range(1, n+1):
#     fact *= i
#     print("factorial ", fact)


# 7
# def is_prime(num):
#     if (num<2):
#         print(" Not a Prime number")
#     for i in range(2, int(num** 0.5) +1):
#         if(num % i == 0):
#            return False
#         return True

# # input from the user
# number = int(input("Enter num : "))
# if(is_prime(number)):
#     print(f"{number} is a prime number ")
# else:
#     print(f"{number} is not a prime number")

# def is_prime(num):
#     if(num < 2):
#         print("Not a prime number")
#     for i  in range(2, int(num** 0.5) +1):
#         if(num%i == 0):
#             return False
#         return True
# # Take an input#
# number = int (input("enter number : "))
# if(is_prime(number)):
#     print(f"{number} is a prime number")
# else:
#     print(f"{number} Not a prime number")
#8#
# def is_prime(num):
#     if (num <2):
#         return False
#     for i in range(2,int(num** 0.5) +1):
#         if num% i == 0:
#             return False
#         return True
    
# for number in range(1, 100):
#     if (is_prime(number)):
#         print(number)

# list1 = [1,2,1]
# list2 = [1,2,3]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("yes")
# else:
#     print("No"
#           )

#11.
# Lists = [18,89,56,97,90,64,35]
# Lists.sort()
# print(max(Lists))

# 12#
# Lists = [18,89,56,97,90,64,35]
# Lists.sort()
# print(min(Lists))

# 13#
# Lists = [18,89,56,97,90,64,35]
# Lists.sort()
# print(sum(Lists))
#14
# Lists = [18,89,56,97,90,64,35,56,98,34,67,56]
# Lists.sort()
# print(Lists.count(56))

#15
# Lists = [18,89,56,97,90,64,35,56,98,34,67,56]
# print(Lists[: : -1])

#16
# Lists = [18,89,56,94,90,64,35,56,98,34,67,56]
# Lists.sort()
# print(max(Lists))
# Lists.pop(-1)
# print(max(Lists))

#17####
# Lists = [18,89,56,94,90,64,35,56,98,34,67,56]
# my_set = set(Lists)
# print(my_set)
# my_list = list(my_set)
# print(my_list)

#18
# list= []
# print(len(list))
# if(len(list) == 0):
#     print("yes")
# else:
#     print("no")
#19
# List1 = [18,89,56,94,90,64,35,56,98,34,67,56]
# List2 = [65,89,34,12,25,35,37,72,19]
# List1.extend(List2)
# print(List1)
# print(List2)

#20
# List1 = [18,89,56,94,90,64,35,56,98,34,67,56]
# List2 = [65,89,34,12,18,56,98,25,35,37,72,19]
# my_set1 = set(List1)
# my_set2 = set(List2)
# my_set = my_set1.intersection(my_set2)
# my_list = list(my_set)
# print(my_list)

#### Tuples & Sets  ##
#26
# tuple_data = ()
# temp_list =[]
# tup_1 = int(input("enter num:"))
# tup_2 = int(input("enter num: "))
# tup_3 = int(input("enter num: "))

# temp_list.append(tup_1)
# temp_list.append(tup_2)
# temp_list.append(tup_3)
# print(temp_list)
# tuple_data = tuple(temp_list)
# print(tuple_data)
# print(len(tuple_data))

#27

# Sample_data = (23,56,98,67,9,67,8,65,89,87,74,37,92)

# element = int(input("enter num: "))
# if element in Sample_data:
#     print(element," exit in data.")
# else:
#     print(element," doesn't exit in data.")

#28
# Sample_data = (23,56,98,67,9,67,8,65,89,87,74,37,92)
# Samp_data = str(Sample_data)
# print(Samp_data)
# print(type(Samp_data))

#29
# Sample_data = (23,56,98,67,9,67,8,65,89,87,74,37,92)
# Samp_data = Sample_data[::-1]
# print(Samp_data)

#30
# Sample_data = (23,56,98,67,9,67,8,65,89,87,74,37,92)
# indexs = Sample_data.index(65)
# print(indexs)

#31
# Sample_dat = set()
# Sample_dat.add(24)
# Sample_dat.add("rahul tiwari")
# Sample_dat.add("hello world")
# Sample_dat.add((24,78,89,56))

# print(type(Sample_dat))
# Sample_dat.remove("hello world")
# print(Sample_dat)

#35
# Set_1 = {24,68,98,36,98}
# set_2 = {67,98,24,89,68,56}

# disjoint = Set_1.isdisjoint(set_2)
# if disjoint:
#     print("the sets are disjoint")
# else:
#     print("they have common elemnts")

#36
# Info = {
#     "name" : "rahul tiwari",
#     "age" : 20,
#     "subject" : "Python",
#     "topics" : ("dictonary", "set", "tuple"),
#     "marks" : 89
# }
# print(Info)
# print(Info.values())
# Info.update({"subject" :("Python","Java","C")})
# # print(Info["subject"])
# # keytocheck_ = "subject"
# # if keytocheck_ in Info:
# #     print(keytocheck_,   "It exist")
# # else:
# #     print("not exist.")
# school = {
#     "name" : "dps",
#     "classes" : "1 to 10th",
#     "students" : 500,
#     "teacher" : {
#         "maths" : 10,
#         "english" : 7,
#         "science" : 15,
#         "hindi" : 11
#     }
# }

# merged_dict = {**Info, **school}
# print(merged_dict)

#42
# Info = {
#     "name" : "rahul tiwari",
#     "age" : 20,
#     "subject" : "Python",
#     "topics" : ("dictonary", "set", "tuple"),
#     "marks" : 89
# }
# print(Info)
# #iterating over the items.
# print("iterating over the dictionary items/n:")
# for key, value in Info.items():
#     print(f"{key}: {value}")

# sorted_key = sorted(Info)
# sorted_dict = {key: Info[key] for key in sorted_key}
# print("dict sorted by key:\n")
# for key in sorted_dict:
#     print(f"{key}: {sorted_dict[key]}")

#43
# Info = {
#     "name" : "rahul tiwari",
#     "age" : 20,
#     "subject" : "Python",
#     "topics" : ("dictonary", "set", "tuple"),
#     "marks" : 89
# }
# sorted_values = sorted(Info)
# sorted_dict = {value: Info[value] for value in sorted_values}
# for value in sorted_dict:
#     print(f"{value}: {sorted_dict[value]}")

#Strings#
#46

# sub_1 ="maths"
# sub_2 = "english"
# sub_3 = "hindi"
# allsubject = sub_1+ " "+sub_2+ " "+sub_3
# print(allsubject)

#47
# str_input =str(input("enter :"))
# copy = str_input
# resversed_str = copy[::-1]
# if(str_input ==resversed_str):
#     print("this is palindorme")
# else:
#     print("not")

#49
# name_ = "Rahul Tiwari"
# split_name = name_.split()
# print(split_name)
# reversed_name = split_name[::-1]
# print(reversed_name)