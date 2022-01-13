def add(a, b, *c):
    a += b + sum(c)
    return a


# print("Test 0 -> " +  add(7)) won't work
print("Test 1 -> " + str(add(7, 3)))
print("Test 2 -> " + str(add(7, 3, 4)))
print("Test 3 -> " + str(add(7, 3, 2, 1)))

choose = input("Enter 2 to add two numbers and 3 for three numbers > ")
while choose != '2' and choose != '3':
    print("Input exception")
    choose = input("Enter 2 to add two numbers and 3 for three numbers > ")

user_input = input("Enter the first number > ")
while not user_input.lstrip('-').isnumeric():
    print("Input exception")
    user_input = input("Enter the first number > ")
a = int(user_input)

user_input2 = input("Enter the second number > ")
while not user_input2.lstrip('-').isnumeric():
    print("Input exception")
    user_input2 = input("Enter the second number > ")
b = int(user_input2)

if choose == "3":
    user_input3 = input("Enter the third number > ")
    while not user_input3.lstrip('-').isnumeric():
        print("Input exception")
        user_input3 = input("Enter the third number > ")
    c = int(user_input3)
    print(f"The result is {add(a, b, c)}")
else:
    print(f"The result is {add(a, b)}")
