while True:
    user_input = input("How many friends you want to invite? (press n to exit)> ")
    if user_input == "n":
        break
    try:
        friends_number = int(user_input)
        if friends_number < 10:
            for number in range(friends_number):
                friend_name = input(f"Enter your friend name (number:{number + 1}) > ")
                print(f"{friend_name} has been invited")
        else:

            print("Too many people")
    except:
        print("Wrong input type!!, Enter a number and try again")