# even no. and ood no. in for loop

# for i in range(1,100):
#     if i % 2 == 0:
#         print(f"num is even {i}")
#     else:
#         print("num is odd ")


# count = 1
# while count <= 10 :
#     if count % 2 == 0:
#         print("num is even ")
#         continue
    
# else:
#         print("num is odd")



# name = "Krupaee"
# if len(name) == 7 and 's' in name:
#      print("my name is ", name)


#  no and uska square
# def number_fun(x):
#      y = x*x
#      print(y)
# number_fun(5)


# square = lambda x : x*x
# print(square(4))    

# prices = [ 30, 12 , 45, 60, 15]
# # print(list(map(lambda p : (p.replace('$', 'Rs')), prices )))/
# print(list(filter(lambda p : p >= 30, prices)))


# empty = [1,2, 3, 4,5,6,7,8,9]
# # print (empty)
# # empty.append("a")
# empty.pop()
# print (empty)

# #  
# greet = "hello world. how are you?"
# def count(greet):
#     {}


class Student:
    school_name = "Modern"
    def __init__(self, ag, nm):
        self.age = ag
        self.name = nm
    @classmethod
    def id(cls):
        cls.school_name
        print(cls.school_name)
   
stu1 = Student(15, 'jay')
stu2 = Student(17, 'raj')
print(stu1.__dict__)
print(stu1.id)







