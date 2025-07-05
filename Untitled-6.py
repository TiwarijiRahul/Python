
# Create a program to calculate the sum of natural numbers up to a given number.#
# n = int(input("num is :"))
# sum_total =(n*(n+1))//2
# if(n<1):
#     print("enetr positive num")
# else:
#     print(sum_total)

# Write a Python program to find the largest number in a list.
# list_1 = [24,78,90,10,50,40]
# max(list_1)
# print(max(list_1))

# list_1 = [] # take as aempty list.

# n = int(input("enter  how many numbers: ")) # how many number you want to enter.

# for i in range(n):
#     num =int(input("enter number:")) 
#     list_1.append(num)

# largest = list_1[0]

# for i in list_1:
#     if i >largest:
#         largest = i
    
# print(largest)

# empty_list = [] # taking empty list
# n = int(input("numbers:")) #taking range of input , how many list 

# for i in range(n):
#     num = int(input("enter num :"))# take list as input
#     empty_list.append(num)# append the num in empty list

# largest = empty_list[0] #intialise largest using index

# for i in empty_list: # use for loop
#     if i >largest:
#         largest = i
# print(largest)

# my_list = []

# # num= (map(int, input("enter number").split()))
# # my_list = list(num)
# # print(max(my_list))

# n = int(input("enter n = "))

# for i in range(n):
#     num = int(input("entr num: "))
#     my_list.append(num)
# print(max(my_list))

# my_list= [37,90,89,333]  #12
# min_num = min(my_list)
# print(min_num)
# my_list = [] # take empty list first.

# # num = map(int ,input("enter num: ").split())
# # my_list = list(num)
# # print(min(my_list))

# # n =int(input("enter n "))  # taking range for how many numbers in list should we add#

# for i in range(n):
#     num = int(input("enter num: "))
#     my_list.append(num)
# print(min(my_list))
# print(my_list)

# Create a program to calculate the sum of all items in a list

# my_list = [78,90,67,90,23]
# sum = 0
# for i in my_list:
#     sum +=i
# print(sum)

# my_list  =[]
# n = int(input("enter n: "))
# for i in range(n):
#     num = int(input("enter num: "))
#     my_list.append(num)

# sum = 0
# idx = 0
# for i in my_list:
#     sum += i

# print(sum)
#using while loop#

# i = 0

# while i <n:
#     num = int(input("enter num: "))
#     my_list.append(num)
#     i +=1
# print(my_list)

# sum = 0
# j = 0 # we initalize the first for while loop.

# while j<n:
#     sum += my_list[j]
#     j+=1
# print(sum)

# Write a Python program to count the occurrences of an element in a list.#14

# my_list = []
# num = map(int, input("enter num: ").split())
# my_list = list(num)
# count_num = my_list.count(78)
# print(count_num)

#  Write a program to reverse a list without using the reverse function. # 15
# my_list = []

# num = map(int, input("enter num: ").split())
# my_list = list(num)
# print(my_list[: :-1])

# Find the second largest number in a list. #16

# mylist = []

# n = (int(input("enter n : ")))
# for i in range(n):
#     num = int(input("enter num: "))
#     mylist.append(num)
# print(mylist)
# mylist.sort()
# mylist.pop(-1)
# print(max(mylist))
# mylist.sort(reverse=True)
# print(mylist[1])

# Remove duplicates from a list. #17
# my_list = []
# num = map(int, input("enter num: ").split())
# my_list = list(num)
# new_set = set(my_list)
# new_list = list(new_set)
# print(new_list)

# Write a Python program to check if a list is empty.  #18

# mylist = [12,34,56]
# if(mylist == []):
#     print("empty list")
# else:
#     print("list is not empty")

#  Create a program to merge two lists. ##19
# my_list1 = [12,34,56,78]
# my_list2 = [23,56,78,90]
# my_list2.extend(my_list1)
# print(my_list1)
# print(my_list2)

# Write a Python program to find common elements between two lists. ##20
# my_list1 = [12,34,56,78,56,90,12,34,56,78,90]
# my_list2 = [23,56,78,90,12,45]
# new_set1 = set(my_list1)
# new_set2 = set(my_list2)
# common_set = new_set1.intersection(new_set2)
# new_list = list(common_set)
# print(new_list)

# Write a program to split a list into evenly sized chunks. ##21

# empty_list = []
# num = map(int, input("enter num: ").split())
# empty_list = list(num)
# chunk_size = int(input("chunk: "))

# i = 0

# while i <len(empty_list):
#     chunk = empty_list[i: i+chunk_size] # it is taking slicing using i and then increasing + chunk_size. 
#     print(chunk)
#     i+=chunk_size

# . Write a Python program to flatten a list of lists.# 23
# flatten list is like nested list in list.
# my_list = [[1,2,3],[4,5,6],[7,8,9,0]]
# flaten_list = []

# for sublist in my_list:       #You loop through each sublist (like [1, 2]) inside the main list.# Then loop through each item inside that sublist and add it to flat_list
#     for item in sublist:
#         flaten_list.append(item)
    

# print(flaten_list)


### Tupel and set
# Write a Python program to find the length of a tuple. #26
# tuples = (23,45,67,89,90,45)
# print(len(tuples))

#  Write a program to check if an element exists in a tuple.  #27

# tuples = (23,45,67,89,90,45)
# if(67) in tuples:
#     print("exit")
# else:
#     print("not exit")

# / Convert a tuple to a string #28
# tuples = (23,45,67,89,90,45)
# new_str = str(tuples)
# print(new_str)
# print(type(new_str))

# Write a Python program to reverse a tuple. 29

# tuples = (23,45,67,89,90,45)
# print(tuples[: : -1])

# Create a program to find the index of an item in a tuple. #30 
 # use index method.
# tuples = (23,45,67,89,90,45)

# print(tuples.index(67))

# /Write a Python program to create a set and add elements.# 31

# my_set = set()
# print(type(my_set))
# my_set.add(23)
# my_set.update([23,45,76,78,"Rahul"])
# print(my_set)

# Find the intersection of two sets.
# set1 = {1,2,3,4,5}
# set2 = {1,2,4,5,6,7,89,}
# newset = set1.intersection(set2)
# print(newset)

#35
# Set_1 = {24,68,98,36,98}
# set_2 = {67,88,14,89,58,56}

# disjoint = Set_1.isdisjoint(set_2)
# if disjoint:
#     print("the sets are disjoint")
# else:
#     print("they have common elemnts")

#36

# info = {"name" : "Rahul",
#         "Age" : 29,
#         "education" : "BCA ",
#         "Subject" : "Python",
#         "Topic" : "Dictonaries"
#         }
# print(info)
# print(info.values())
# print(info.keys())

#38

# info = {"name" : "Rahul",
#         "Age" : 29,
#         "education" : "BCA ",
#         "Subject" : "Python",
#         "Topic" : "Dictonaries"
#         }
# info.update({"Semester" : "(1,2,3,4)"})
# print(info.values())

#39 # 40
# info = {"name" : "Rahul",
#         "Age" : 29,
#         "education" : "BCA ",
#         "Subject" : "Python",
#         "Topic" : "Dictonaries"
#         }
# info.pop("Age")
# print(info)
# if ("Age") in info:
#     print("exist")
# else:
#     print("not")

#41
# info1 = {"name" : "Rahul",
#         "Age" : 29,
#         "education" : "BCA ",
#         "Subject" : "Python",
#         "Topic" : "Dictonaries"
#         }

# info2 ={ " University" : "Amity",
#         "Year" : 2025,
#         "Location" : "Noida"

# }
# Merged_Dict = {**info1, **info2}
# print(Merged_Dict)

#50
# name = "My name is Rahul Tiwari"

# New_name =name.split()
# reverse_word = New_name[: : -1]
# full_name =' '.join(reverse_word)
# print(full_name)
#46 

# sub_1 ="maths"
# sub_2 = "english"
# sub_3 = "hindi"
# Allsubject =  sub_1+" "+sub_2+ " " +sub_3 # " " is used as a seprator in words.#

# print(Allsubject)
# 47
# words = "abaa"
# if(words ==words[: : -1]):
#     print("Palindrome")
# else:
#     print("not")

# 48 Count vowels and consonants in a string.#
# S =  " My name is Rahul Tiwari"
# vowels = "aeiou"
# vowel_count = 0
# Consonent_count = 0

# for char in S:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count +=1
#         else:
#             Consonent_count +=1
    
# print("vowels:", vowel_count)

# Function Question#
# 1. Write a function to return the sum of two numbers.

# def sum(a,b):
#     sum =  a+b
#     return sum
# result =sum(10,111)
# print(result)
# print(sum(111,111))

# 2.Write a function that returns the square of a number.

# def square_num(num):
#   square_ =num **2
#   print(square_)
#   return square_
 
# square_num(6)
# print(square_num(3))
# print(f" square of a num : {square_num(9)}")

# 3. Write a function that checks if a number is even or odd.

# def check_num(num):
#     if(num%2 == 0):
#         print("even")
#     else:
#         print("odd")

# check_num(10)
# check_num(111)

# 4. Write a function that returns the length of a given list.  

# list1 = [10,191,28,"Rahul", "Tiwari","Utkarsh", 20,38,90]

# def len_list(list1):
#     result  = len(list1)
#     print(result)

# len_list(list1)

# 5. Write a function that takes a string and returns it in uppercase. 

# def uppercase_str(text):
#     return text.upper()

# result = uppercase_str("rahul tiwari")
# print(result)

# 6. Write a function that returns the maximum of three numbers.

# def largest_num(a,b,c):
#     if( a > b and a >c):
#         return a
#     elif(b>a and b>c):
#      return b
#     else:
#        return c
    

# result  =  largest_num(10,20,30)
# print(result)
# print(largest_num(90,100,111))

# 7. Write a function to calculate the factorial of a number using recursion.

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# result = fact(5)
# print(result)

# 8. Write a function that takes a list and returns the sum of all elements.

# def sum_list(num):
#     sum = 0
#     for i in num:
#         sum += i
#     return sum
    
# print(sum_list([1,2,3,4,5,6]))

# 9. Write a function that takes a string and returns the number of vowels in it. 
# def vowels_count(text):
#     vowel_count = 0
#     vowel = "aeiou"
#     for i in range(len(text)):
#         if (text[i: i+1] in vowel):
#             vowel_count +=1

#     return vowel_count
# print(vowels_count("Rahul"))

#     vowels = "aeiou"
#     for char in text:
#         if char in vowels:
#             vowel_count +=1
    
#     return vowel_count
# print(vowels_count("rahul tiwari"))

# # 10. Write a function that swaps the values of two variables.  
# def swapval(a,b):
#     swap_val_a = b
#     swap_val_b = a
#     new_swap_value =("value of a : ", swap_val_a,"value of b : ",swap_val_b)
#     print(new_swap_value)

# swapval(10,15)

# def swapval(a,b):
#     return b,a

# x,y = swapval(10,15)
# print("val of a:",x)
# print("val of b:",y)

# 11. Write a function that returns the reverse of a string. 

# def reverse():
#     text = str(input("enter text")).split()
#     reverse_str = text[: : -1]
#     new_text = ' '.join(reverse_str)
#     print(new_text)

# reverse()
# def reverse(text):
#     return text[: : -1]

# result = reverse("Rahul")
# print(result)

# 12. Write a function that checks if a given number is prime. 

# def is_prime(n):
#     if n <=1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True

# result = is_prime(111111000001111000011)
# print(result)

# def is_prime(n):
#     if(n <= 1):
#         print("False")
    
#     for i in range(2,n):
#         if n% i == 0:
#             print("False")
    
#     else:
#         print("True")

# is_prime(11)

# 13. Write a function that removes duplicate elements from a list.

# def my_list():
#     data_ = map(int,input("enter data:").split())
#     set_ = set(data_)
#     list_ = list(set_)
#     result =(list_)
#     print(result)

# my_list()

# def my_list():
#     data = input("enter num: ").split()
#     int_data = list(map(int, data))
#     list1= []
    
#     for num in int_data:
#         if num not in list1:
#             list1.append(num)
#     print(list1)

# my_list()
    
# 14. Write a function to count the occurrences of a specific character in a string.
# def str_count(text, char):
#     text = input("text : ")
#     return text.count(char)

# name_ = str_count("Rahulla","l")
# print(name_)

# 16. Write a function that finds the greatest common divisor (GCD) of two numbers. 

# import math
# def gcd_(a,b):
#     return math.gcd(a,b)

# result = gcd_(80,18)
# print(result)

# 17. Write a function that returns the least common multiple (LCM) of two numbers.
# import math
# def  lcm_(a,b,c):
#     return math.lcm(a,b,c)

# result = lcm_(18,20,27)
# print(result)

# 18. Write a function that calculates the power of a number using recursion.
# def power_of_Num(base, exp):
#     if exp == 0:
#         return 1
#     else:
#         return base * pow(base, exp-1)

# result = power_of_Num(3,3)
# print(result)

# 19. Write a function that takes a list of numbers and returns a new list with only the even numbers.

# def even_list():

   
#     num =(map(int, input("enter num: ").split()))
#     my_list = []

#     for i in num:
#         if i %2 == 0:
#             my_list.append(i)
        
#     print(my_list)


# even_list()

# # 20. Write a function that finds the second largest element in a list.

# def sec_large_num():
#     num =(map(int, input("enter num: ").split()))
#     my_list = []
#     my_list= list(num)
#     my_list.sort(reverse= True)
#     sec_num = my_list[1]
#     print(sec_num)

# sec_large_num()

# 21. Write a function that merges two sorted lists into a single sorted list. 
# def merge_list():
#     num1= map(int, input("enter num: ").split())
#     num2 = map(int, input("enter num: ").split())

#     my_list1 = []
#     my_list2 = []

#     my_list1 = list(num1)
#     my_list2 = list(num2)
#     final_list = my_list1.extend(my_list2)
#     print(my_list2)
#     print(my_list1)
   

# merge_list()




    


    


