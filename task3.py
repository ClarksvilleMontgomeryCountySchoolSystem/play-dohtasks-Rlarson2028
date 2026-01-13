def main():
    color1 = "gray"
    color2 = "pink"
    print(f"1) Roll a ball using {color1}.")
    choice1 = input("Do you want  long body or a round body? ")
    # CAUTION: You must include the word "body" when checking!
    if choice1 == "Long body":
        print(f"2) Roll the ball into an egg shape")
    else:
        print(f"2) Keep it as a ball")
    print(f"3) Roll a smaller ball using Color 1 for the head.")
    print(f"4) Attach the head to one end of the body.")
    choice2 = input("Do you want a long tail or a short tail? ")
    if choice2 == "Long tail":
        print(f"5) Roll a thin rope using {color2} and attach to the back")
    else:
        print(f"5) Add a small bump using {color2} to the back")
    print(f"6) Add four small legs to the bottom using {color1}.")
    print(f"7) Add two dots for eyes and a tiny nose.")
    print(f"8) Name this creation: Mouse ")


if __name__ == "__main__":
    main()
