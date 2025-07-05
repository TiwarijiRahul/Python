
# f = open("Demo1.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("Demo1.txt", "w")
# f.write("This is a new line.")

# f.close()

# f =  open("Demo1.txt", "a")
# f.write("\nI am learning Python.")
# f.close()
# f = open("sample.txt", "w")
# f.close()

#Practice#
# 1. Write a program to read the text from given file 'poems.txt' and find out the word contains 'twinkle'

# import random

# def game():

#     score = random.randint(1,100)

#     f = open("Hiscore.txt","r") 
#     hiscore = f.read()
#     f.close()
#     print(hiscore)

#     if(hiscore != ""):
#         hiscore = int(hiscore)
      
      
#     else:
#         hiscore = 0
       

#     print(f"your score : {score}")

#     if score > hiscore:
#         f = open("Hiscore.txt","w")
#         f.write(str(score))
#     print(score)

# game()

# #3 Write a tables file from 2 to 20 and store table of them in a file.

# def generatetable(n):
#     table = ""

#     for i in range(1,11):
#         table += f"{n} * {i} = {n*i}\n"
        
    
#     with open(f"tables/table_{n}","w") as f:
#         f.write(table)

# for i in range(2,21):
#     generatetable(i)

# 4. Write a file where replaces donkey as ####.
# word = "Donkey"

# f = open("Donkey.txt","r")
# content =  f.read()
# new_content = content.replace("Donkey","####")
# f= open("Donkey.txt","w")
# f.write(new_content)

#5 Write a progarm to replaces a list of words or more than 1  words in a file.

# words = ["Donkey", "bad", "ganda"]

# f = open("donkey.txt", "r")
# content = f.read()

# for word in words:
    

#     content =  content.replace(word,"#" * len(word))
# f = open("donkey.txt","w")
# f.write(content)

#6 Write a program to identify thr word from minilog and line no.
# Lineno = 1
# f = open("log.txt","r")
# Lines = f.readlines()
# for line in Lines:
#     if("python" in line):
#         print("Yes present",Lineno)
#         break
#     Lineno +=1

# else:
#     print("Not present")

#7 Create a new file "Practice.txt" using Python. Add the items.

# with open("practices.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.\nI like programming in Java.")

# f = open("practices.txt","r")
# data = f.read()
# data = data.replace("Java", "Python")
# print(data)
# f.close()

# with open("practices.txt","w") as f:
#     f.write(data)

#8 WAF to find in which line of the file does the word"learning"
# occur first. 

# def check():
#     word = "learning"
    
#     with open("practices.txt","r") as f:
#         data = f.read()
#         if(word in data):
#             print("found")

#         else:
#             print("not found")
    
#     line1 = 1
#     count = 0
#     with open("practices.txt","r") as f:
#         Lines = f.readlines()
#         for line in Lines:
#             if("Python" in line):
#                 print("present", line1)
#                 break
#             line1 +=1
#             count+= line.count("Python")

#         else:
#             print("not present")



# check()

