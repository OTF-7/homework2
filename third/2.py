numbers = list()
user_number = int()


def user_input_validation(direction, user_input):
    global numbers, user_number
    try:
        user_number = int(user_input)
        if direction == "1":
            numbers = range(1, user_number)
            if user_number <= 1:
                print("The input is out of the range !!, Enter a number above 1 and try again")
                return False
        else:
            numbers = reversed(range(user_number + 1, 21))
            # if we want to consider negative numbers, we can remove this condition user_number < 0
            if user_number >= 20 or user_number < 0:
                print("The input is out of the range !!, Enter a number between 20 and 0 and try again")
                return False
    except:
        print("Wrong type input !!, Enter a number and try again")
        return False
    return True


def my_func():
    global run_again
    try:
        direction = input("Enter the direction, 1 or up and 2 for down (if you want to quit press n) > ")
        if direction == "1":
            user_input = input("Enter the top number, it should be above 1 (if you want to quit press n)> ")
        elif direction == "2":
            user_input = input("Enter a number below 20 (if you want to quit press n)> ")
        elif direction == "n":
            run_again = False
            return
        else:
            print("I don't understand.")
            return

        if user_input == "n":
            run_again = False
            return

        inner_run_agin = user_input_validation(direction, user_input)
        while not inner_run_agin:
            if direction == "1":
                user_input = input("Enter the top number, it should be above 1 (if you want to quit press n)> ")
            elif direction == "2":
                user_input = input("Enter a number below 20 (if you want to quit press n)> ")
            if user_input == "n":
                inner_run_agin = False
                run_again = False
                return
            inner_run_agin = user_input_validation(direction, user_input)

        global numbers, user_number
        for number in numbers:
            print(number)
        print("And you Entered " + str(user_number))
    except Exception:
        print("Wrong type input !!, Enter a number and try again")


run_again = True
while run_again:
    my_func()
