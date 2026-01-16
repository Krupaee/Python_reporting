# score = 94
# if score >= 90 :
#     print("A")

# if-else
# score = 50
# if score>= 90:
#     print("A")
# else:
#     print("F")

# elif
# score = 55
# if score >= 90:
#     print ("A")
# elif score >= 80:
#     print("B")
# else:
#     print("F")

# elif-elif
# score = 73
# if score >= 90:
#     print ("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")

# Nested if-else
# score =95
# submitted_project = False
# if score >= 90:
#     if submitted_project:
#         print("A+")
#     else:
#         print ("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# logical operators
# score =55
# submitted_project = True
# if score >= 90 and submitted_project:
#     print ("A+")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60 or submitted_project:
#     print("D")
# else:
#     print("F")

# Independent if-else
# score =95
# submitted_project = False
# if score >= 90:
#     print("High score")
# else:
#     print("Low score")

# if submitted_project:
#     print("Project is submitted")
# else:
#     print("Project is not submitted")

# CHALLENGE 
email = "Kru@paee@gmail.com!"
valid = True
# if-else is not used here because then the o/p would be just one error at a time |rather| Independent if statements are used so that all the errors are showed at once
# clean the string
email = email.strip()
# Email must not contain spaces
if email == "":
    print("Email cannot be empty")
    valid = False
# Email must contain a '.' and '@'
if not('.' in email and '@' in email):
    print("Email must contain a '.' and '@'")
    valid = False
# Email must contain only one'@'
if email.count('@') != 1 : # != -> not equals to
    print(" Email must contain exactly one @.")
    valid = False
# Email must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with '.com', '.org', or '.net'")
    valid = False
# Email must not be longer than 254 characters
if len(email)> 254:
    print("Email must not be longer than 254 characters")
    valid = False
# Email must start and end with a letter or a digit
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start or end with a letter or a digit")
    valid = False
if valid:
    print("Email is valid")
