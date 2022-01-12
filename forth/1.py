total = 0
while total <= 50:
    user_input = input("Enter a number > ")
    try:
        number = int(user_input)
    except:
        print("Wrong input type !!, Enter a number and try again")
        continue
    total += number
    print("The total is: " + str(total))
