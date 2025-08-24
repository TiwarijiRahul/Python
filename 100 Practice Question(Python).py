
# 100 Practice Problems of Python#
# Basics and Fundamentals (1–10)

# 1./ Write a program to print "Hello, World!"
# print("Hello World!")
# 2./ Write a Python program to add two numbers.
# a = int(input("enter a num:"))
# b = int(input("enter a num:"))
# sum = a+b
# print(sum)
# 3./ Create a program that takes a number as input and checks if it’s positive, negative, or zero.
# Num = int(input("enter a num: "))
# if Num == 0:
#     print("Num is zero")
# elif Num > 0:
#     print("Num is positive")
# else:
#     print("Num is negative")
# 4./ Write a Python program to check if a number is even or odd.
# Num  = int(input("enter a num"))
# if Num %2 == 0:
#     print("Even")
# else:
#     print("Odd")
# 5./ Find the maximum of three numbers.
# a = int(input("enter num: "))
# b = int(input("enter num: "))
# c = int(input("enter num: "))
# if a > b and a>c:
#     print(a)
# elif b> a and b>c:
#     print(b)
# else:
#     print(c)
# maximum = max(a,b,c)
# print(maximum)
# 6./ Write a Python program to calculate the factorial of a number.
# num = int(input("enter num: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial:", factorial)

# def fact(n):
#     factorial = 1
#     for i in range(1, n+1):
#         factorial *= i
#     print(factorial)

# res = fact(5)
# 7./ Create a program to check if a number is prime.
# we have to check the num <=1, then it is not prime, if num= 2&3, then prime
# then use loop for up to a range of num of its square root and it given remainder,0
# then false or other wise true.
# num = int(input("enter num: "))
# if num <=1:
#     print("Not Prime")
# elif num <= 3:
#     print("Num is Prime")
# else:
#     is_prime = True

#     for i in range(2, int(num ** 0.5)+1):
#         if num %i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("Prime Num")
#     else:
#         print("Not Prime")

# 8./ Write a Python program to print all prime numbers between 1 and 100.
# Take a for loop between (2, 101), then assume it is prime like is prime = True
# then iterate over square root of num and check it has a factor or not.

# for num in range(2, 101):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num,end = ' ')

# 9. Create a program to calculate the sum of natural numbers up to a given number.
# n = int(input("enter num: "))
# sum = n* (n+1)//2
# print(sum)
# sum = 0
# for i in range(1, n+1):
#     sum +=i
# print(sum)
### Data Structures: Lists (11–25)
# 11./ Write a Python program to find the largest number in a list.
# lists = [10,50,30,40,100]
# Highest = max(lists)
# print(Highest)
# 12./ Write a Python program to find the smallest number in a list.
# n = int(input("enter no of list: "))
# lists = []
# for i in range(n):
#     num = int(input("enter num: "))
#     lists.append(num)
# smallest = min(lists)
# print(smallest)
# 13./ Create a program to calculate the sum of all items in a list.

# num = list(map(int, input("enter num: ").split(',')))

# print(sum(num))
# sum = 0
# for i in(num):
#     sum +=i

# print(sum)
# 14./ Write a Python program to count the occurrences of an element in a list.
# use the count method in list for it.
# lists = [2,3,4,5,6,7,2,3,4,8,9]
# print(lists.count(2))

# 15./ Write a program to reverse a list without using the reverse function.
# lists = [1,2,3,4,5,6]
# newlist = lists[::-1]
# print(newlist)

# 16./ Find the second largest number in a list.
# n = int(input("no of list: "))
# lists = []
# for i in range(n):
#     num = int(input("enter num:"))
#     lists.append(num)
# lists.sort(reverse= True)
# second_largest = lists[1]

# print(second_largest)

# 17./ Remove duplicates from a list.
# lists = [2,3,4,5,2,3,4,5,6,7]
# sets = set(lists)
# new_list = list(sets)
# print(new_list)

# 18./ Write a Python program to check if a list is empty.
# my_list = []
# if not my_list:
#     print("list is empty")
# else:
#     print("not empty")

# if len(my_list)==0:
#     print("empty list")
# else:
#     print("not empty")

# 19./ Create a program to merge two lists.
# list1 = [2,3,4,5,6]
# list2 = [3,4,5,7,8,9,0]
# new_list = list1+list2
# print(new_list)

# 20./ Write a Python program to find common elements between two lists.
# list1 = [2,3,4,5,6]
# list2 = [3,4,5,7,8,9,0]
# common_list = list(set(list1)& set(list2))
# print(common_list)

# 21./ Write a program to split a list into evenly sized chunks.

# Step 1: Take input as a list of numbers
# data = list(map(int, input("Enter numbers separated by space: ").split()))

# # Step 2: Take the chunk size from user
# chunk_size = int(input("Enter chunk size: "))

# # Step 3: Initialize an empty list to store chunks
# chunks = []

# # Step 4: Loop through the list in steps of chunk_size
# for i in range(0, len(data), chunk_size):
#     # Step 5: Slice a chunk and append it
#     chunks.append(data[i:i + chunk_size])

# # Step 6: Print the result
# print("List in chunks:", chunks)
# data = list(map(int, input("enter num: ").split(',')))
# chunk_size = int(input("enter num: "))
# chunk = []

# for i in range(0,len(data),chunk_size):
#     chunk.append(data[i:i+chunk_size])

# print(chunk)
# 22./   Find all unique elements in a list.
# lists = [2,3,4,5,6,7,2,3,4,5,6]
# new_list = list(set(lists))
# print(new_list)
# 24. Create a program to rotate a list.
# Input list
# data = list(map(int, input("Enter list elements (space-separated): ").split()))
# k = int(input("Enter rotation count: "))
# direction = input("Rotate left or right? (left/right): ").strip().lower()

# # Normalize k (handle values greater than length)
# k = k % len(data)

# # Rotate
# if direction == 'left':
#     rotated = data[k:] + data[:k]
# elif direction == 'right':
#     rotated = data[-k:] + data[:-k]
# else:
#     print("Invalid direction.")
#     rotated = data  # No change

# # Output
# print("Rotated List:", rotated)

### Data Structures: Tuples and Sets (26–35)
# 26./ Write a Python program to find the length of a tuple.
# tup = (1,2,3,4,5,6,7,8)
# print(len(tup))

# 27./ Write a program to check if an element exists in a tuple.
# tup = (2,3,4,5,6,7,8)
# if 9 in tup:
#     print("found")
# else:
#     print("Not found")

# 28./ Convert a tuple to a string.
# tup  = (2,3,4,5,6,7)
# string = str(tup)
# print(type(string))

# 29./ Write a Python program to reverse a tuple.
# tup = (2,3,4,5,6,7,8,9)
# new_tup = tup[::-1]
# print(new_tup)

# 30./ Create a program to find the index of an item in a tuple.
# tup = (2,3,4,5,6,7,8,9)
# print(tup.index(5))

# 31. /Write a Python program to create a set and add elements.
# sets =set()
# n = input("enter num: ")
# sets.add(n)

# print(sets)

# 32. /Remove elements from a set.
# sets = {2,3,4,5,6,7}
# sets.remove(6)
# print(sets)
# 33./ Find the intersection of two sets.
# set1 = {2,3,4,5,6,7,8}
# set2 = {3,1,9,0,6,7,5}
# new_set = set1.intersection(set2)
# print(new_set)

# # 35./ Write a program to check if two sets are disjoint.

# set1 = {2,3,4,5}
# set2 = {1,9,0,6,7}
# if set1.isdisjoint(set2):
#     print("the sets are disjoint")
# else:
#      print("the sets are not disjoint")

### Data Structures: Dictionaries (36–45)
# 36./ Write a Python program to create a dictionary.
# dict={}
# dict['name'] = "Rahul"
# dict['age'] = 20
# dict["city"] = "Noida"
# dict['Subject'] = "Python"
# print(dict)
# my_dict = {}

# Example input: name,rahul,age,20,city,delhi
# input_ = input("Enter key and value pairs separated by commas: ").split(',')

# for i in range(0,len(input_),2):
#     key = input_[i].strip()
#     Value =input_[i+1].strip()
#     my_dict[key]= Value
# print(my_dict)
# 37./ Access values in a dictionary.
# my_dict = {
#     "name":"Rahul","Age": 20,"City":"Noida","Subject": "Python",
# }
# print(my_dict.values())
# print(my_dict.items())

# 38. /Write a Python program to update the value of a specific key.

# my_dict = {
#     "name":"Rahul","Age": 20,"City":"Noida","Subject": "Python",
# }
# my_dict.update({"Age": 30})
# print(my_dict)
# print(my_dict.get("Age"))
# my_dict["Topic"] = "Dict"
# print(my_dict)
# 39. /Create a program to remove a key from a dictionary.

# my_dict = {
#     "name":"Rahul","Age": 20,"City":"Noida","Subject": "Python",
# }
# my_dict.pop("Age")
# print(my_dict)
# 40./ Check if a key exists in a dictionary.

# my_dict = {
#     "name":"Rahul","Age": 20,"City":"Noida","Subject": "Python",
# }
# if "Topic" in my_dict:
#     print("found")
# else:
#     print("not found")

# 41./ Merge two dictionaries.

# my_dict1 = {
#     "name":"Rahul","Age": 20,"City":"Noida","Subject": "Python",
# }
# my_dict2 = {
#     "Topic": "Dict","Aim": "Data Science","Next Topic": "Pandas",
# }
# new_dict = {**my_dict1,**my_dict2}
# print(new_dict)

# 42.//Write a Python program to iterate over dictionary items.
# Step 1: my_dict.items()
# This returns a list of (key, value) pairs (as tuples)
# my_dict2 = {
#     "Topic": "Dict","Aim": "Data Science","Next Topic": "Pandas",
# }
# for key, value in my_dict2.items():
#     print(f"key: {key}: value-{value}")

# Step 2: for key, value in my_dict.items():
# Yeh loop har tuple (key-value pair) ko unpack karta hai.

# 43./ Write a program to sort a dictionary by keys.

# my_dict2 = {
#     "Topic": "Dict","Aim": "Data Science","Next Topic": "Pandas",
# }
# sorted_dict = sorted(my_dict2.items())
# print(sorted_dict)

# # 44. Write a program to sort a dictionary by values.
# my_dict2 = {
#     "Topic": "Dict","Aim": "Data Science","Next Topic": "Pandas",
# }
# sorted_dict = dict(sorted(my_dict2.items(),key = lambda item:item[1]))
# print(sorted_dict)
# 45./ Create a nested dictionary and access elements within it.
# my_dict = {
#     "name": "Rahul", "Age": 20,
#     "Score": {"che": 90,"Phy": 89,"Math":70},
# }
# print(my_dict.get("Score"))
# print(my_dict["Score"]["Math"])

### Strings (46–60)
# 46./ Write a Python program to concatenate two strings.
# str1 = input("enter :")
# str2 = input("enter: ")
# new_str = str1+str2
# print(new_str)

# 47./ Write a program to check if a string is a palindrome.
# str1 = "abc"
# if str1 == str1[::-1]:
#     print('palindrome')
# else:
#     print('not palindrome')
# 48. Count vowels and consonants in a string.
# n =input("enter: ")
# vlowels = "aeiouAEIOU"
# vol_Count = 0
# Cons_count = 0
# for i in n:
#     if i.isalpha():
#         if i in vlowels:
#             vol_Count+=1
#         else:
#             Cons_count +=1

# print(vol_Count)
# print(Cons_count)
# 49. Find the frequency of each character in a string.
# str1 = input("enter str: ")
#use dict to store key and value for frequency
# dict1 = {}
# for ch in str1:
#     if ch in dict1:
#         dict1[ch]+=1
#     else:
#         dict1[ch]=1

# for key, value in dict1.items():
#     # print(f"{key}: {value}")
#     print(key, str(value))

# 50./ Write a program to reverse a string.
# str1 = input("enter : ")
# print(str1[::-1])
# str1 = input("Enter first string: ").replace(" ", "").lower()
# str2 = input("Enter second string: ").replace(" ", "").lower()

# if sorted(str1) == sorted(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")
# from collections import Counter

# str1 = input("Enter first string: ").replace(" ", "").lower()
# str2 = input("Enter second string: ").replace(" ", "").lower()

# if Counter(str1) == Counter(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")
# Use .replace(" ", "") if you want to ignore spaces (like in phrases)

# Use .lower() to make it case-insensitive

# 51. Create a program to check if two strings are anagrams.
# str1 = input("Enter first string: ").replace(" ", "").lower()
# str2 = input("Enter second string: ").replace(" ", "").lower()

# if sorted(str1) == sorted(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")
# from collections import Counter

# str1 = input("Enter first string: ").replace(" ", "").lower()
# str2 = input("Enter second string: ").replace(" ", "").lower()

# if Counter(str1) == Counter(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")
# Use .replace(" ", "") if you want to ignore spaces (like in phrases)

# Use .lower() to make it case-insensitive

# Counter is faster for large strings, especially if you don't care about order

# 52. Write a Python program to remove duplicate characters from a string.
# n = str("Rahultiwari")
# lists =list(n)
# sets = set(lists)
# strs =''.join(list(sets)) 
# print(strs)
# s = "banana"
# result = ''.join(dict.fromkeys(s))
# print(result)  # Output: 'ban'

### Functions and Lambda Expressions (71–80)
# 71. Write a function to find the maximum of two numbers.
# def maximum(a, b):
#     return max(a, b)

# print(maximum(10, 20))
# 72. Write a function to calculate the factorial of a number.
# def fact(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial *=i
#     return factorial

# print(fact(5))
# 76. Create a function to find the sum of all elements in a list.

# def lists():
#     n = int(input("enter no:"))
#     list1 =[]
#     for i in range(n):
#         inputs =int(input("enter num:"))
#         list1.append(inputs)
#     print(list1)
#     print(sum(list1))

# lists()
### File Handling (61–70)
# 61. Write a program to create a file and write data into it.
# file = open("myfile.txt","w")
# file.write("Hello Rahul kumar Tiwari")
# file.close()
# 62. Write a Python program to read data from a file.
# file = open("myfile.txt","r")
# print(file.readline())
# 63. Write a program to append data to an existing file.
# file = open("myfile.txt","w")
# file.write("Hello Rahul kumar Tiwari\n")
# file = open("myfile.txt","a")
# file.write("This is new line")

# file = open("myfile.txt","r")
# print(file.read())
# file.close()
# 64. Count the number of words in a file.
# file = open("myfile.txt","r")
# content = file.read()
# words = content.split()
# word_count = len(words)
# print(word_count)
# file.close()
# 65. Write a Python program to find the longest word in a file.
# file = open("myfile.txt","r")
# content = file.read()
# words =content.split() # split is used to split the text in words in list form.
# longest = max(words,key=len)
# print(longest)
# file.close()

# 66. Write a program to copy contents from one file to another.
# file2 =open("file2.txt","w")
# file2.write("this is new file\n")
# file = open("myfile.txt","r")
# data = file.read()
# file.close()

# file2.write(data)
# file.close()
# file2 = open("file2.txt","r")
# print(file2.read())
# file2.close()
# 67. Write a program to merge two files into one.
# file = open("myfile.txt","r")
# file2 = open("file2.txt","r")
# data2 = file2.read()
# data = file.read()
# file.close()
# file2.close()
# merged_file = open("merged.txt","w")
# merged_file.write(data)
# merged_file.write("\n")
# merged_file.write(data2)
# merged_file.close()
# merged_file = open("merged.txt","r")
# merged = merged_file.read()
# print(merged)

# 68. Write a program to read the contents of a file line by line.
# merged_file = open("merged.txt","r")
# for line in merged_file:
#     print(line.strip())
# merged_file.close()
# with open("merged.txt","r") as file:
#     for line in file:
#         print(line.strip())

# 69. Write a Python program to remove newline characters from a file.
# with open("myfile.txt","r") as file:
# # Step 1: Open the original file in read mode

#     lines = file.readlines()  # Read all lines as a list

# # Step 2: Remove newline characters
# cleaned_lines = [line.strip() for line in lines]

# # Step 3: Join all lines into a single string (no newlines)
# final_text = "".join(cleaned_lines)

# # Step 4: Overwrite the file with the cleaned content
# with open("myfile.txt", "w") as file:
#     file.write(final_text)

# print("Newline characters removed successfully.")

# 70. Write a program to count occurrences of a specific word in a file.

# Step 1: Open the file in read mode
# file = open("myfile.txt", "r")

# # Step 2: Read the content of the file
# content = file.read()

# # Step 3: Ask user for the word to search
# word = input("Enter the word to count: ")

# # Step 4: Split content into words and count occurrences
# words = content.split()
# count = words.count(word)

# # Step 5: Print the result
# print(f"The word '{word}' occurs {count} times in the file.")

# # Step 6: Close the file
# file.close()


# Write the code for students of a hostel, ask their course and their age. calculate the avg of age.

# n = int(input("enter no of stud: "))

# students = []
# total_age = 0

# for i in range(n):
#     # print("student")
#     i +=1

#     course = input("enter course name: ")
#     age = int(input("enter age: "))
#     students.append({"course": course,"age": age})
#     total_age +=age

# avg_age = total_age/n
# print("students data", students)
# print("avg_age", avg_age)

### Functions and Lambda Expressions (71–80)
# 71. Write a function to find the maximum of two numbers.
# def max_(a,b):

#     if a>b:
#         return a
#     else:
#         return b

# maximum= max_(10,30)
# print(maximum)
# 72. Write a function to calculate the factorial of a number.
# def fact_():
#     n = int(input("enter num:"))
#     factorial =1
#     if n == 0 or n ==1:
#         print(1)
#     for i in range(1, n+1):
#         factorial *=i
    
#     print(factorial)

# fact_()
# 76. Create a function to find the sum of all elements in a list.
# def sum_():
#     list_= []

#     n =input("enter num seperated by commas: ")
#     list_.append(n)
#     print(list_)
#     print(type(list_))

# sum_()
#WAP to print table of 1 to 20.

# for num in range(1,21):
#     print(f"\nTable of {num}")

#     print("-" *10)

#     for i in range(1,11):
#         print(num*i)
# print 1, 11,21,1211,111221,312211
# def look_and_say(n):
#     if n <=0:
#         return
#     s = "1"
#     print(s)
#     for _ in range(2, n+1):
#         i = 0
#         next_s = []
#         while i <len(s):
#             count = 1

#             while i +1 <len(s) and s[i]== s[i+1]:
#                 count+=1
#                 i+=1
#             next_s.append(str(count))
#             next_s.append(s[i])
#             i +=1
#         s = "".join(next_s)
#         print(s)
    
# look_and_say(6)

#WAF that replace all occurance of Java with python.

# with open("demo.txt","w") as f:
#     f.write("\nThis is my Java course.")
#     f.write("\nI am learning Java Programming.")
   

# with open("demo.txt","r") as f:
#     data  = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)


# From a file containing numbers seprated by commas, print the count of even numbers.
# with open("demo.txt","w") as f :
#     f.write("1,2,3,4,5,6,7,8,9,10,11,12")
# count = 0
# with open("demo.txt","r") as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if (int(val)%2 ==0):
#             count +=1
    
# print(count)

# Creating class and objects;
# class student:

#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks

#         print("adding new students in the databases...")
    
# s1 = student("Rahul Tiwari",90)
# print(s1.name,s1.marks)

# Ques. Create students class that takes name and marks of 3 subjects as arguments. Then create a method to print the avg of marks.

# class student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

    
   
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:

#             sum +=val
        
#         print("hi", self.name,"avg marks is: ", sum/3)

# s1 = student("Rahul", [90,91,92])
# print(s1.get_avg()) 
    
# Ques. Create an account class with 2 attributes- balance and account no. Create a method for credit ,debit and print the balance.

# class account:

#     def __init__(self,bal,acc_no):

#         self.balance = bal
#         self.account_no = acc_no

#     def credit(self,amount):
#         self.amount = amount
#         self.balance +=amount

#         print("Your account is credited", self.amount)
#         print("your total balance is : ", self.balance)
    
#     def debit(self, amount):
#         self.amount = amount
#         self.balance -= amount

#         print("your account is debited: ", self.amount)
#         print("your total balance is : ", self.balance)

# acc1 = account(10000,123)

# print(acc1.balance)
# print(acc1.account_no)
# acc1.debit(1000)
# acc1.credit(2000)

#Qus. Define a circle with constructor radius  and find the area and perimeter of a circle.

# class circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7)* self.radius**2
    
#     def perimeter(self):
#         return 2*(22/7)*self.radius
    
# c1 = circle(10)
# print(c1.area())
# print(c1.perimeter())

# Que. Define an employee class with attributes ,role, dept, salary. Create an engineer class with name and age attributes. Show role, dept, and salary of eng.

# class Employee:

#     def __init__(self,role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
    
#     def showdetails(self):
#         print("\nRole = ", self.role, "\nDept = ", self.dept, "\nSalary = ", self.salary)


# class Engineer(Employee):

#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#         super().__init__("Engineer","IT", 75000)

# Eng1 = Engineer("Rahul", 25)
# Eng1.showdetails()

# Ques . Create a class order with attributes item and price.Use dunder function __gt__ to convey that, order1>order2 if price of order1>order2.

# class order:

#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#     def __gt__(odr1,odr2):
#         return odr1.price>odr2.price

# odr1 = order("chips",20)
# odr2 = order("tea", 25)

# print(odr1>odr2)    

# Ques. Guess the Number.

# import random

# target = random.randint(1,100)
# attempts = 0
# while True:

#     UserNum = int(input("enter the num: "))
#     attempts +=1

#     if(UserNum ==target):
#         print("Correct Guess", target)
#         print("You have guessed in",attempts,"attempts")

#         break
#     elif(UserNum>target):
#         print("Take a smaller num:")
#     else:
#         print("Take a bigger num")

# print("Game Over....")

# Random Password generator.

# import random
# import string

# pas_len = 12
# password= ""
# charvalues = string.ascii_letters+string.digits+string.punctuation

# for i in range(pas_len):
#     password += random.choice(charvalues)
# print(password)





        

        
        
        


    
    

        

    




   






    






















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































    



    


