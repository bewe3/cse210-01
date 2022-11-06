# bryan welton iii
# cse 210 week 1 - tic tac toe

one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"

turn = 10
player = ""

taken1 = 0
taken2 = 0
taken3 = 0
taken4 = 0
taken5 = 0
taken6 = 0
taken7 = 0
taken8 = 0
taken9 = 0

advance = 0


def main():
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

    # print the board
    print("\n")
    print(f" {one} | {two} | {three}")
    print(" - + - + -")
    print(f" {four} | {five} | {six}")
    print(" - + - + -")
    print(f" {seven} | {eight} | {nine}\n")
    turns()


def turns():
    global turn
    global player
    global advance

    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

    global taken1
    global taken2
    global taken3
    global taken4
    global taken5
    global taken6
    global taken7
    global taken8
    global taken9

    # determine whose turn it is
    if turn % 2 == 1:
        player = "o"
    else:
        player = "x"

    # by default, advance to next turn
    advance = 1

    if advance == 1:
        print(f"it's {player}'s turn to choose a square (1-9)\n")
    elif advance == 0:
        print("")

    # takes user input and changes the board accordingly if the space isn't taken
    choice = input(">>> ")
    match choice:
        case "1":
            if taken1 == 0:
                one = player
                taken1 = 1
            elif taken1 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "2":
            if taken2 == 0:
                two = player
                taken2 = 1
            elif taken2 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "3":
            if taken3 == 0:
                three = player
                taken3 = 1
            elif taken3 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "4":
            if taken4 == 0:
                four = player
                taken4 = 1
            elif taken4 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "5":
            if taken5 == 0:
                five = player
                taken5 = 1
            elif taken5 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "6":
            if taken6 == 0:
                six = player
                taken6 = 1
            elif taken6 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "7":
            if taken7 == 0:
                seven = player
                taken7 = 1
            elif taken7 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "8":
            if taken8 == 0:
                eight = player
                taken8 = 1
            elif taken8 == 1:
                print("\nPlease pick a free space\n")
                main()

        case "9":
            if taken9 == 0:
                nine = player
                taken9 = 1
            elif taken9 == 1:
                print("\nPlease pick a free space\n")
                main()

        case _:
            print("\nPlease enter a valid space\n")
            main()

    # if 3 not in a row, advance to the next turn.
    detect()
    if advance == 1:
        turn = turn + 1

        # if the game is too long, then it's a draw
        while turn < 19:
            main()

    # if 3 in a row, game over
    elif advance == 0:
        print("Game over.")

    if turn == 19:
        print("Draw.")


# function to detect 3 in a row
def detect():
    global advance
    if one == two == three:
        print(f"\nGood game. {one} wins!")
        advance = 0
    elif four == five == six:
        print(f"\nGood game. {four} wins!")
        advance = 0
    elif seven == eight == nine:
        print(f"\nGood game. {seven} wins!")
        advance = 0
    elif one == four == seven:
        print(f"\nGood game. {one} wins!")
        advance = 0
    elif two == five == eight:
        print(f"\nGood game. {two} wins!")
        advance = 0
    elif three == six == nine:
        print(f"\nGood game. {three} wins!")
        advance = 0
    elif one == five == nine:
        print(f"\nGood game. {one} wins!")
        advance = 0
    elif three == five == seven:
        print(f"\nGood game. {three} wins!")
        advance = 0
    return advance


main()
