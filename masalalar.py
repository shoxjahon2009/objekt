# def mapping(harflar):
#     a = {}
#     for x in harflar:
#         a[x] = x.upper()
#     return a
#
# print(mapping(["a", "v", "y", "z","h","d"]))

                    ## 2--masala

# def resalt(dict, resalt1):
#     for x in dict:
#         for w in x.values():
#             if type(w) == int:
#                 resalt1 = resalt1 + w
#     return resalt1
#
# print(resalt([
#   { "tile": "N", "score": 1 },
#   { "tile": "K", "score": 5 },
#   { "tile": "Z", "score": 10 },
#   { "tile": "X", "score": 8 },
#   { "tile": "D", "score": 2 },
#   { "tile": "A", "score": 1 },
#   { "tile": "E", "score": 1 }
# ], 0))

                ## 3--masala

# def get_budgets(lst):
#     resault = 0
#     for x in lst:
#         resault += x["budget"]
#     return resault
# print(get_budgets([
#   { "name": "John", "age": 21, "budget": 23000 },
#   { "name": "Steve",  "age": 32, "budget": 40000 },
#   { "name": "Martin",  "age": 16, "budget": 2700 }
# ]))

                ## 4 masala
# lst = input("enter")
# if len(lst) == 0:
#     print("no one online")
# elif len(lst) == 1:
#     print("user1 online")
# elif len(lst) == 2:
#     print("user_1 and user_2 online")

                #### 5-masala
# x10 = list(range(1, 10 ,3))
# a = []
# a.append(x10)
# print(a)
                ### 6-masala
# def get_student_names(lst):
#     a = []
#     for x in lst:
#         a.append(lst[x])
#     return sorted(a)
#
# print(get_student_names({
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# }))

                ### 7--masala
# family = {
#     "father":"Darth Vader",
#     "sister":"Leia",
#     "brother in law":"Han",
#     "droid":"R2D20",
# }
# name = input("name:")
# def relation_to_luke(name):
#     for x in family:
#         if family[x] == name:
#             return f"Luke, I am your {x}❗❗"
#         elif family[x] == name:
#             return f"Luke, I am your {x}❗❗"
#         elif family[x] == name:
#             return f"Luke, I am your {x}❗❗"
# print(relation_to_luke(name))
                #### 8-masala

# def calc(lst):
#     hisoblar = {"harflar": 0, "RAQAMLAR": 0}
#     for x in lst:
#         if x.isnumeric():
#             hisoblar["RAQAMLAR"] += 1
#         elif x.isalpha():
#             hisoblar["harflar"]+= 1
#     return hisoblar
# print(calc("Hello World"))
# print(calc("149990"))

                        ### 9-masala

# a = ["A", "B", "A", "A", "A"]
# b = { "A" : 4, "B" : 1 }
# c = dict.fromkeys(a, b)
# print(c)

                ####  10-masala

# a = int(input("❗son❗:"))
# resault = 0
# calc_diff = {"skate": 200, "painting": 200, "shoes": 1 }
# for x in calc_diff.values():
#     resault = resault + x
#     y = resault - a
# print(y)


