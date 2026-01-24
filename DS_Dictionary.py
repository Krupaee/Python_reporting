# my_dict ={
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 10
# }
# print(my_dict)
# print(my_dict['b'])

# my_dict['c'] = 80
# print(my_dict)

# Special methods
# user = {'id':1, 'age': 30, 'city': 'berlin'}
# # Access
# print(user['name']) # if not exists- it breaks code "ERROR"
# print(user.get('name'))  # OR
# print(user.get('name', 'unknown'))

# # checks
# print('age' in user)
# print('age' not in user)

# # view objects
# print(user.keys())
# print(user.values())
# print(user.items())

# print(user)

# # looping
# for u in user:          # too confusing to understand
#     print(u, user[u])
# for key, value in user.items():
#     print(key, value)

# user = {'id':1, 'age': 30, 'city': 'berlin'}
# # Add
# user["name"] =  'John' 
# user ["age"] = 35

# # Update
# user.update({"age": 40, "city" : "paris"})
# print(user)

# # Remove
# user.pop("age")
# print(user)

# age = user.pop("age")
# print(user)
# print("Removed Item :", age)

# # age = user.pop("salary")    "ERROR"
# age = user.pop("salary", "not found")
# print (user)
# print("removed item :", age)

# user.popitem()
# print(user)