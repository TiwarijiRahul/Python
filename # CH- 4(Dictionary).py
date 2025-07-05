# CH- 4(Dictionary)
# info = {
#     "name" : "Rahul Tiwari",
#     "Key" : "value",
#     "learning" : "python",
#     "topics" : ("dict", "sets"),
#     "age " : 20,
#     "is adult" : "True",
#     "marks" : 94.4
# }
# print(info["topics"])
# print(info)
# info["name"] =  "Tiwari ji"
# info["surname"] = "rahul"
# print(info)

#nested dictonary#
# std = {
#     "name" : "rahul",
#     "subject" : {
#         "phy" : 98,
#         "chem" : 89,
#         "math" : 67,
#     }
# }

# print(std.keys())
# print(list(std.keys()))
# print(std.items())
# print(std.get("key"))
# std.update({"city": "Noida"})
# print(std)

# // Sets in python//#
# collection = {1,2,3,4,5,"hello","world","hello","world",2,3,4,5,1}
# print(collection)
# print(len(collection)) #Duplicates are not allowed in sets in python.
# collection = set () #Null sets#
# print(type(collection))

#set methods
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add("hello")
# collection.add((1,2,3,4,5,6,7))


# collection.remove((1))
# print(collection)
# set1 = {1,2,3,4,5,6,"Hello","world"}
# set2 ={2,3,4,5,6,7,8,9,"world","hellow"}
# print(set1.union(set2))
# print(set1)
# print(set2)
# print(set1.intersection(set2))

#practice question#
#1.Store following word meaings in a python dictonary:
"""table: "a piece of furniture", "list of facts & figures" """
"cat : ""a small animal" ""



#2. You are given a lists of subjects for students. Assume one classroom is required for 1 subject.How many classrooms are needed by all students.
"python", "java", "C++", "python", "javascript", "java", "python", "C++", "C"

# dict1 = {
#     "cat": "a small animal",
#     "table" : ["a piece of furniture", "list of facts & figures"]
# } #1.#

# Subject = {"python", "java", "C++","python","javascript","java","python","C++","C"}
# print(Subject)
# print(len(Subject))  #2.#

#3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one . Use subject name as key & marks as value.

# marks = {}
# x = int(input("enter phy :"))
# marks.update({"Phy" : x})

# x = int(input("enter chem :"))
# marks.update({"chem" : x})

# x = int(input("enter maths :"))
# marks.update({"maths" : x})

# print(marks)

# values = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)



