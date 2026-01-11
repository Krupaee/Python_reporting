# name = input("enter your name : ")
# print("My name is:", name)
# print(f"my name is {name}") # runtime
# print("my name is {name}".format(name=name))# flexible


name = "krupaee"
lastname = "sharma"
fullname = name + " "+ lastname
# print(fullname.upper())
# print(fullname.capitalize())
# print(fullname.replace("a" , "aa"))
# print(fullname.replace(" " , ""))
# print(fullname.strip())
# print(len(fullname))

filename  = "test.xaml"
if filename.endswith(".xaml"):
    print("this is xaml file")

phoneno = """+917775086315
+919921195530
+482699986532
"""
phonenumers = phoneno.split("\n")
for num in phonenumers:
    if num.startswith("+48"):
        print(num)
# nuber = ["+917775086315","+919921195530", "+482699986532"]
# for num in nuber:
#     if num.startswith("+48"):
#         print(num)

# print(fullname[:7])
# print(fullname[3:7])
# print(fullname[::-1])





#printfullname(upper())