def func():
    user_input = input("Please enter any number > ")
    while not user_input.lstrip('-').isdigit() or len(user_input.lstrip('-')) < 3:
        if not user_input.lstrip('-').isdigit():
            print("Wrong input type !!, Enter only numbers. ")
        else:
            print("Too short !!, It must be at least 3 numbers. ")
        user_input = input("Please enter any number > ")

    return user_input[2] if user_input.lstrip('-') == user_input else user_input[3]


print(func())
