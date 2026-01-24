# empty = []
# print(empty)
# print(type(empty))

# empty = []
# letters = ['a', 'b', 'c']
# print(letters)
# print (type(letters))

# empty = list()
# print(empty)

# letters = 'python'
# print(letters)

# letters = list('python')
# print (letters)

# numbers = list(range(7))
# print(numbers)

# nested list
# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f']
# ]
# print (matrix)
# print(type(matrix))

# Indexing
# lst = ['a', 'b', 'c', 'd']
# print (lst)
# print (lst[0])
# print (lst[-1])

# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i']
# ]
# # print (matrix)
# print (matrix[-1])
# print (matrix[-1][-2])
# print (matrix[-1][2])
# print (matrix[-1][-1])
# print (matrix[0][0])
# print (matrix[1][1])

# Slicing
# lst = ['a', 'b', 'c', 'd']
# print (lst[:2])
# print (lst[2:])

# matrix = [
#      ['a', 'b', 'c'],
#      ['d', 'e', 'f'],
#      ['g', 'h', 'i']
# ]
# print(matrix[:2])
# print(matrix[2:])

# print(matrix[2][:2])

# unpacking
# person = ['Maria', 29, 'data engineer','spain']
# # name, age, role, country = person
# # name, *details = person
# # name, _, _, country = person
# name, *_ = person
# print (name)

# numbers = [1, 5, 5, 4, 3]
# print("Max:" , max(numbers))
# print("Min:" , min(numbers))
# print("Sum:" , sum(numbers))
# print("Length:" , len(numbers))

# print("All:" , all(numbers))
# print("All:" , all([1,0,2]))
# print("All:" , all(['a', '', 'b']))

# print("Any:" , any(numbers))
# print("Any:" , any([1,0,2]))
# print("Any:" , any([0, 0, 0]))

# print("Count :" , numbers.count(5))
# print("Index :", numbers.index(5))

# print(4 in numbers)
# print(8 not in numbers)

# list1 = [1,2,3]
# list2 = [5,2,3]
# print(list1 == list2)
# print(list1 < list2)
# print(list1 is list2)

# Add 
# letters = ['a', 'b', 'c']
# # letters.append('x')
# # letters.append('y')
# letters.insert(0,'x')
# letters.insert(3,'y')
# print(letters)

# matrix = [
#      ['a', 'b', 'c'],
#      ['d', 'e', 'f'],
#      ['g', 'h', 'i']
# ]
# # matrix.append(['x', 'y', 'z'])
# # matrix.insert(0,['a', 'a', 'a'])
# matrix[1].append('x')
# matrix[0].insert(0,'z')
# print(matrix)

# # Remove
# letters = ['a', 'b', 'a']
# # letters.clear()
# # letters.remove('a')
# # letters.pop(1)
# removed = letters.pop()
# print(letters)
# print('Removed Item :' , removed)

# letters = [5,2,3,4,5,6]
# letters.remove(5)
# print (letters)

# matrix = [
#      ['a', 'b', 'c'],
#      ['d', 'e', 'f'],
#      ['g', 'h', 'i']
# ]
# matrix.remove(['a', 'b', 'c'])
# matrix.pop()
# matrix[1].remove('e')
# matrix[-1].pop(0)
# matrix[0].pop()
# print(matrix)

# #  Update
# letters = ['a', 'b', 'c']
# letters[0] = 'x'
# letters[-1] = 'y'
# print (letters)

# matrix = [
#      ['a', 'b', 'c'],
#      ['d', 'e', 'f'],
#      ['g', 'h', 'i']
# ]
# matrix[-1] = ['x', 'y', 'z']
# matrix[0][0] = '-'
# matrix[1][1] = '-'
# matrix[-1][-1] = '-'
# print (matrix)