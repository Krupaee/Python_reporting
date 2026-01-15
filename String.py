# name = "krupaee"
# print(type(name))

# age = 24
# print(type(age))
# print("your age is:" + age) ----> Error

# age = 24
# print(type(age))
# print("your age is:" + str(age))

# passward = "23456a"
# print(len(passward))

# replace()
# phone = " 176-1234-789"
# print(phone.replace("-", "/"))

# join strings
# folder="C:/users/krupaee"
#file= "report.csv"
#full_file_path = folder + file ---> o/p - C:/users/krupaeereport.csv
# full_file_path = folder + "/" + file  ---> o/p - C:/users/krupaee/report.csv 
#print(full_file_path)

# f- string
name = "Sam"
age = 34
is_student = False
print("My name is " + "I am " + str(age) + "years old, and student status is" + str(is_student) + ".")
print(f"My name is {name}, I am {age} years old, and student status is {is_student}")