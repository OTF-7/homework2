while True:
    user_input = input("Enter a number between 10 and 20 > ")
    try:
        number = int(user_input)
        if number < 10:
            print("Too low")
        elif number > 20:
            print("Too high")
        else:
            print("Thank you")
            break
        print("Try again 😣")
    except:
        print("Wrong input type!!, Enter a number and try again")