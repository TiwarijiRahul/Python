#CH - 3
# LIST AND TUPPLES#
# Marks = [98,78,56,90,29,56.8,78.7]
# print(Marks)
# print(type(Marks))
# print(Marks[3])

# std1 = ["Rahul", 98, 20, "Noida"]
# print(std1)
# std1[0] = "Tiwariji"
# print(std1)

#list slicing

# Marks = [98,78,56,90,29,56.8,78.7]
# print(Marks[1:3])
# print(Marks[-5:-2])

#Lists Methods

# list = [2,1,4]
# list.append(5)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse= True)
# print(list)
# list.reverse()
# print(list)
# list.insert(1,7)
# print(list)
# list.remove(2)
# print(list)


#Tupples#

# tup= (87,67,89,56,78)
# print(type(tuple))
# print(tup[1])
# tup[0] = 76#Not changeable

#Tupple methods#

# tup = (2,1,4,5,2)
# print(tup.index(1))
# print(tup.count(2))

 #practice questions#
#1. WAP to ask the user to enter names of their 3 favourite movies & store them in a list.
#2. WAP to check if a list contains a palindrome of elements.(use copy()).

#1#
# movies = []
# first_moives = input("enter 1st movies : ")
# second_moives = input("enter 2nd movies : ")
# third_moives = input("enter 3rd movies : ")

# movies.append(first_moives)
# movies.append(second_moives)
# movies.append(third_moives)
# print(movies)

# list1 = [1,2,3,2,1]#2#
# list2 = [1,2,3]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# grade = ("C","A","B","A")
# print(grade.count("A"))
# list = ["C","A","B","A"]
# list.sort()
# print(list)