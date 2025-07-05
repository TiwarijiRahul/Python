#Ch-5 - Loops#

# count = 1
# while count<= 5:
#     print("hello")
#     count +=1

#     print(count)
# i = 5
# while i >= 1:
#     print(i)
#     i -=1

#     print("loop ended")

#practice question#
#1. print numbers from 1 to 100.

# num = 1
# while num <= 100 :
#     print(num)
#     num +=1

    #2. print numbers from 100 to 1.
# num = 100
# while num> 1:
#         print(num)
#         num -=1

#3. Print the multiplication table of a number n.
# i = int(input("enter num : "))
# num  =  1
# while num <= 10:
#     print(i* num )
#     num +=1
    
#4. print the elemeints of the following list using a loop.
#[1,4,9,16,25,36,49,64,81,100]

# num = [1,4,9,16,25,6,49,64,8,100] #len(list)-1
# # print(num[0])

# idx = 0
# while idx <len(num):
#     print(num[idx])
#     idx +=1

# #5. Search for a number x in this tupple using loo[p:
# num = (1,4,9,16,25,36,49,64,81,100)

# x = 25

# i = 0
# while i < len(num):
#   if( num[i] == x):
#     print("fount at idx", i)
#     i += 1

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1

# nums = (1,4,9,16,25,36,49,64,81,100,36)

# x = 36

# i = 0
# while i <len(nums):
#     if(nums[i] == x):
#         print("found at idx", i)


# tup = (1,2,3,4,5,6,7,8,9)      
# for num  in tup:
#     print(num)

# str = "Rahul tiwari"

# for char in str:
#     if(char == 't'):
#        print("t found")
#        break
#     print(char)
   

# else:
#     print("end")

#Let's practice(using for loop)#

#print the elements of the following list using a loop:
#[1,,4,9,16,25,36,49,64,81,100]

# num  = [1,4,9,16,25,36,49,64,81,100]

# for el in num:
#     print(el)

#2. Search for a number x in this tupple using loop:
#[1,4,9,16,25,36,49,64,81,100]

#[1,4,9,16,25,36,49,64,81,100]

# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 49
# idx = 0

# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#         break
#     idx += 1

#RANGE#
# seq = range(10)
# # for i in range(5):
# #     print(i)

# for i in range(2,10,2):
#     print(i)

# n=  int(input("enter number :"))

# for i in range(1,11):
#     print(n*i)

#3. WAP to find the sum of first n numbers.(using  while )
# n = 8
# sum = 0
# i = 1
# while i <=n:
#     sum +=i
#     i +=1
# print(sum)
# for i in range(1, n+1):
#     sum +=i
#     print(sum) # usnig for loop

#print the number 1 to 10

# n = 1
# while n<= 10:
#     print(n)
#     n +=1

# print("----")
# print("Even No :")
# n =20
# i = 2
# while i<= 20:
#     print(i)
#     i+=2

#Continue statement
# i = 2
# while i<= 20:
#     if (i%2 == 0):
#         i= i+1
#         continue;
#     print(i)
#     i +=1

#break statement

# i = 1
# while i <= 20:
#     if i == 7:
#         break;
#     print(i)
#     i +=1

#range
# print(list(range(1,20,2)))

#for Loop
# for i in range(1,21,2):
#     print(i)

# print("----")

# for i in range(5):
#     a = int (input("enter a no: "))
#     b = int (input("enter a no: "))
    
#     print(a+b)
# for i in range(6):
#    for j in range(i):
#     print("*",end= "")
#    print("")

#1. Print numbers from 1 to 100

# for i in range(1,101):
#     print(i)
#     i +=1

# i = 1
# while i <= 100:
#     print(i)
#     i+=1

#2. Print even numbers from 1 to 50

# for i in range(1,51):
#     if i%2 !=0:
#         i = i+1
#         continue;
#     print(i)
#     i +=1

# i = 1

# while i <= 50:
#     if (i%2 != 0):
#         i = i+1
#         continue;
#     print(i)
#     i +=1

#3. Print the multiplication table of a number.

# NUm = int(input("enter a number: "))

# for i in range(1,11):
#     print(NUm * i)
#     i +=1

# num = int(input("enter a no: "))
# i= 1
# while i<= 10:
#     print(num *i)
#     i +=1

#4 Sum of all numbers from 1 to N

# N= int(input("enter a num: "))

# # for i in range(1,N+1):
# #     print(i)
# #     i +=1

# i = 1
# while i<= N:
#     print(i)
#     i +=1

#5 Print a right angled stars.

# for i in range(1,6):
#     for j in range(i):
#         print("*", end="")
#     print("")

#6 Print all odd numbers between N

# N = int (input("enter a num: "))

# for i in range(1, N+1):
#     if(i %2 == 0):
#         i = i+1
#         continue;
#     print(i)
#     i +=1

# i = 1
# while i <=N:
#     if(i %2 == 0):
#         i = i+1
#         continue;
#     print(i)
#     i +=1

#7 Print Fibonacci series up to N Terms

# N_terms = int(input("enter the num: "))

# #first 2 terms
# a,b = 0,1

# for i in range(N_terms):
    
#     n_terms=a+b
#     a =b
#     b= n_terms
#     print(n_terms)

#8 Sum of digits of a number

# n = int(input("enter digit: "))


# sum = 0

# for i in range(len(str(n))):
#     rem = n%10
#     sum = sum+rem
#     n = n//10
# print("sum is : ", sum)


# n= int(input("sum of digits: "))

# sum = 0

# for i in range(len(str(n))):
#     rem = n%10
#     sum = sum +rem
#     n = n//10
# print("sum of digit is :", sum)

