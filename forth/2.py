import random

low = high = int()


def pick_low_and_high():
    global low, high

    user_input = input("Enter the low number > ")
    while not user_input.isdigit():
        print("Wrong input type !, Enter a number and try again > ")
        user_input = input("Enter the low number > ")

    while True:
        user_input2 = input("Enter the high number > ")
        while not user_input2.isdigit():
            print("Wrong input type !, Enter a number and try again > ")
            user_input2 = input("Enter the high number > ")

        low = int(user_input)
        high = int(user_input2)

        if abs(low - high) == 1:
            print("The difference between low and high numbers should be higher then 1")
            continue

        if low > high:
            print(f"You entered ({low}) as the low number and ({high}) as the high number, we will reverse them ")
            temp = low
            low = high
            high = temp

        comp_num = random.randint(low, high)
        break
    return comp_num


def guess_number():
    global low, high
    user_input = input(f"I am thinking of a number between {low} and {high} (including both)... could you guess it? > ")
    guess = int(user_input)
    return guess


def check():
    global low, high
    comp_num = pick_low_and_high()
    while True:
        try:
            guess = guess_number()
        except:
            print("Wrong input type !!, Enter a number and try again")
            continue
        if guess == comp_num:
            print("Correct, you win")
            return

        if guess < low:
            print(f"Lower the the low number ({low})!")
        elif guess > high:
            print(f"higher the the high number ({high})!")
        elif guess < comp_num:
            if abs(guess - comp_num) <= 10:
                print("low")
            else:
                print("Too low")
        else:
            if abs(guess - comp_num) <= 10:
                print("high")
            else:
                print("Too high")


check()
