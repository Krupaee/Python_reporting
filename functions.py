# def make_coffee():
#     print("Start machine")
#     print("Make Coffee")
#     print("Add milk")
#     print("Enjoy it")
# print("Wake up")
# make_coffee()
# print("working for a while")
# make_coffee()


# print(len("Python")) # built in function

# import math      # functions from libraries(Import then call)
# number = 4.2
# print(math.ceil(number))

# def greet():       # User defined function (define then call)
#     print("hello")
# greet()


# # Parameters & Arguments

# def multiple_two(x):
#     print(x*2)
#
# multiple_two(4)

# def clean_name(name):
#     print(name.strip().capitalize())
#
# clean_name(" mariA  ")
# clean_name(" KUMAR")

# f=2   # Global variable
# def multiple_factor(x):    # Parameter
#     y = x * f            # Local variable
#     print(y)
# multiple_factor(8)
# print(y)  # ERROR

# def clean_text(name):
#     cleaned = name.strip().lower()
#     print("Raw :", name)
#     print("Cleaned :", cleaned)

# clean_text("MaRiA ")
#                          # OR


# case_rule = "lower"      # Global variable

# def clean_text(name):           # Parameter
#     cleaned = name.strip()        # Local variable
#     if case_rule == "lower":
#         cleaned = cleaned.lower()
#     print("Cleaned :", cleaned)

# clean_text("MaRiA ")
# print(case_rule)            # Global variable

# # Lambda Function
# prices = ['$12.50', '$9.99','$100.00']

# print(list(map(lambda p: float(p.replace('$', '')), prices)))

prices = [120, 30, 300, 80] 

print(list(filter( lambda p: p >= 100, prices)))
      