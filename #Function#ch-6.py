#Function#ch-6

# a = 5
# b = 8

# sum = a+b
# print(sum)

# #more lines of code#
# a = 12
# b= 17
# sum = a+b
# print(sum)

# def calc_sum(A,B):
#     sum = A+B
#     print(sum)
#     return sum
# calc_sum(7,10)
# calc_sum(19,29)
# calc_sum(10,92)

# def cal_sum (a,b):
#     return a+b

# sum = cal_sum(7,9)
# print(sum)
# def cal_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum

# cal_sum(19,98)

# def print_hello():
#     print("hello")

# print_hello()

# def cal_avg(a, b, c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# cal_avg(98,78,67)
# print(type(cal_avg))

#lets practice#
#1. WAF to print the length of a list.(list is the parameter)
# cities = ["delhi", "noida", "mumbai", "patna", "goa"]

# len(cities)
# def  print_len(cities):
#      print(len(cities))
    

# print(len(cities))





#2. WAF to print the elements od a list in a single line.(list is the parameter)
# cities = ["delhi", "noida", "mumbai", "patna", "goa"]

# len(cities)
# def  print_len(cities):
#      print(cities)
    

# print(cities)
#3  WAF to find the factorial of n.(n is the parameter)

n=5
# fact = 1
# for i  in range(1, n+1):
#     fact *=i

# print(fact)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)

#4. WAF to convert USD to INR.
# def converter (usd_val):
#     inr_val = usd_val*83
#     print(usd_val, "usd =", inr_val, "INR")

# converter(10)

# def cal_num(n):
#     if(n% 2 == 0):
#         print("even")
#     else:
#         print("odd")
   

# cal_num(8)
# cal_num(19)
# cal_num(10)
# cal_num(7)
# -----#
#------#
#Function Practice#

# a =5
# b =10
# sum =a+b
# print(sum)

# def add2num (a,b):
#     sum = a+b
#     print(sum)

# add2num(8,19)
# def add2num (a,b):
#     return a+b

# result = add2num(7,10)
# print(result)

# def cal_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# cal_sum(19,19)

# def print_Hello():
#     print("hello Rahul Tiwari")

# print_Hello()

# def Cal_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(sum)
#     return avg


# avg_2 = Cal_avg(10,20,30)
# print(avg_2)
# print(type(avg_2))

#1. WAF to print the length of a list.(list is the parameter)

# cities = ["delhi","Noida","patna", "pune","mumbai"]
# Heroes =["thor","captain","ironman","shaktiman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(Heroes)
n = 5
# fact =1
# for i in range(1,n+1):
#     fact *=i
# print(fact)

# def cal_fact(n):
#     fact =1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
    
# cal_fact(6)

#waf to convert USD to INR.
# def converter(usd_val):
#     inr_val = usd_val*83
#     print(inr_val,"INR")

# converter(10) 

#odd= string, even = even
# def odd_even(n):
#     if n %2 == 0:
#         print("even")
#     else:
#         print("string")

# num = int(input("enter num: "))
# odd_even(num)


def my_name (*kids):
    print("My name is " + kids[2])
my_name("Ram", "Raj", "Rahul")