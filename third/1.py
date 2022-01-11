def my_func():
    try:
        user_input = input("Enter a number below 50 (if you want to quit press n)> ")
        if user_input == "n":
            global run_again
            run_again = False
            return
        user_number = int(user_input)
        # if we want to consider negative numbers, we can remove this condition user_number < 0
        if user_number >= 50 or user_number < 0:
            print("The input is out of the range !!, Enter a number between 49 and 0 and try again")
            return
        for number in reversed(range(user_number + 1, 51)):
            print(number)
        print("And you Entered " + str(user_number))
    except Exception:
        print("Wrong type input !!, Enter a number and try again")


run_again = True
while run_again:
    my_func()
