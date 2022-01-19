from functools import reduce

# reduce
list1 = [1, 2, 3, 4, 5]
summation = reduce(lambda x, y: x + y, list1)
print(summation)

items = [1, 24, 17, 14, 9, 32, 2]
all_max = reduce(lambda a, b: a if (a > b) else b, items)

print(all_max)

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


# map

# One list [5,6,7] with lambda
print(list(map(lambda x: x + 3, [5, 6, 7])))
# Two lists [1,2,3] and [5,6,7] with lambda
print(list(map(lambda x, y: x + y, [1, 2, 3], [5, 6, 7])))

# Dictionary objects in a list
total_marks = [
    {"user": 'john', "marks": 60},
    {"user": 'mike', "marks": 70},
    {"user": 'ken', "marks": 90},
]

print(list(map(lambda x: x['user'], total_marks)))
print(list(map(lambda x: x['marks'] + 10, total_marks)))
print(list(map(lambda x: x['user'] == "mike", total_marks)))

nums = [1, 2, 3, 4, 5]
square = list(map(lambda x: x ** x, nums))
print(square)

people = ["lokesh", "bob", "tom", "developer"]
up = list(map(lambda x: x.upper(), people))
print(up)

eq = [0, 1, 2, 3, 4, 5]

# filter
# result contains odd numbers of the list
result = filter(lambda x: x % 2, eq)
print(list(result))

print(list(filter(lambda x: x % 2 == 0, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])))
# filter users with marks greater than 80
total_marks = [
    {"user": 'john', "marks": 60},
    {"user": 'mike', "marks": 70},
    {"user": 'ken', "marks": 90},
]
print(list(filter(lambda x: x['marks'] > 80, total_marks)))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, eq)
print(list(result))

# zip
name = ["Manjeet", "Nikhil", "Shambhavi"]
marks = [40, 50, 60]

mapped = zip(name, marks)

print(dict(mapped))

name = ["Manjeet", "Nikhil", "Shambhavi"]
roll_no = [4, 1, 3]
marks = [40, 50, 60]

mapped = zip(name, roll_no, marks)

print(list(mapped))
