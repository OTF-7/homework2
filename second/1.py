favourite_colour = input("Enter your favourite colour > ")
if favourite_colour == "blue" \
        or favourite_colour == "BLUE" \
        or favourite_colour == "Blue":
    print("I like blue too")
else:
    print(f"I don’t like [{favourite_colour}], I prefer blue")