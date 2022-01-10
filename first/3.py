print("Enter three names of your friends names (each in line)")
friends = list()
friends.append(input("> "))
friends.append(input("> "))
friends.append(input("> "))

print("Do you want to add more friends, if yes enter thier names else enter no")
check = input("> ")
while check != "no":
    friends.append(check)
    check = input("> ")

print(len(friends))