def main():
    color1 = "blue"
    color2 = "yellow"
    print(f") Use {color2} to roll a ball.")
    choice1 = input("1, 2, or 3? ")
    if choice1 == "1":
        print(f"1) Make the ball flat.\n")
    if choice1 == "2": # elif is a second check only if the first check fails.
        print(f"2) Form the ball into an egg shape.\n")
    if choice1 == "3": # else runs if all previous checks fail.
        print(f"3) Keep it round.")
    print(f") Use {color1} to roll two thin ropes.")
    choice2 = input("A or B? ")
    # Use == to check the User's choice.
    # Use the correct string.
    # Remember you are checking equality to a string. You must use quotes.
    if choice2 == "A":
        print(f"4) Pinch off pieces of the thin ropes to make and attach spots.\n")
    else:
        print(f"4) Use the ropes to make stripes.\n")
    print(f") Add two tiny dots for eyes on the front.")
    choice3 = input("")
    print(f") Write {choice3} on the name card.")

if __name__ == "__main__":
    main()
