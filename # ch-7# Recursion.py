# ch-7# Recursion
#recursive function
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5) # 5,4,3,2,1

# def  fact (n):
#     if(n == 1 or n == 0 ):
#         return 1
    
#     return fact(n-1)*n

# print(fact(6))

#1. write a recursive function to calculate the sum of  first n natural numbers.

# def cal_sum(n):
#     if(n == 0):
#        return 0
   
#     return cal_sum(n-1)+1

# print(cal_sum(8))

#2. write a recursive function to calculate the sum of first n natural numbers.(hint: use list & index as parameters)
#  def  print_list(list, idx):
#       if(idx== len(list)):
#          return 0
#       print_list(list, idx+1)

# fruits = ["mango","litchi", "apple"]

# print_list(fruits) 