menu_names = ["Omar Taha", "Maher Alhosiny", "Baker Omer", "Ziad Alswary", "Mohammed Alqershy", "Ziad Zaid",
              "Ala'a Alsalam"]


def view_names():
    global menu_names
    print("\n".join(menu_names))


def add_name():
    global menu_names
    name = input("Enter the name that you want to add to the menu > ")
    menu_names.append(name)


def delete_name():
    global menu_names
    name = input("Enter the name that you want to delete from the menu > ")
    while name not in menu_names:
        print(name + " is not in the menu, look at the names\n")
        view_names()
        name = input("Enter the name that you want to delete from the menu > ")
    menu_names.remove(name)


def modify_name():
    global menu_names
    name = input("Enter the name that you want to modify from the menu > ")
    while name not in menu_names:
        print(name + " is not in the menu, look at the names\n")
        view_names()
        name = input("Enter the name that you want to modify from the menu > ")
    new_name = input("Enter the new name > ")
    menu_names[menu_names.index(name)] = new_name


while True:
    user_input = input("""
    What do you want to do?
    Press 1 to view the menu names
    Press 2 to add a name to the menu
    Press 3 to to delete a name from the menu
    Press 4 to to modify a name in the menu
    Press 5 to end the program
    """)
    if user_input == "1":
        view_names()
    elif user_input == "2":
        add_name()
    elif user_input == "3":
        delete_name()
    elif user_input == "4":
        modify_name()
    elif user_input == "5":
        break
    else:
        print("I don't understand your order !!")
