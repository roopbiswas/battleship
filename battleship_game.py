print
"Welcome to battleship! "
print
'''
Select level:
Easy > Press E
Moderate > Press M
Hard > Press H
'''
level = raw_input("-> ")
while level != 'e' and level != 'E' and level != 'm' and level != 'M' and level != 'h' and level != 'H':
    print
    "Please enter valid key: "
    level = raw_input("-> ")

if level == 'e' or level == 'E':
    print
    """---------------------------------------------------------------------
Our radars have detected enemy submarine in this area of the ocean!
The radar system is faulty and could only tell that
the enemy is in this 3x3 grid area
Let's target them and make them bite the dust! 
Good Luck!
"""

    board = []
    for i in range(3):
        i = ("O") * 3
        board.append(i)
        print
        "--".join(i)
    from random import randint

    rand_row_one = randint(1, len(board))
    rand_col_one = randint(1, len(board))
    rand_row_two = randint(1, len(board))
    rand_col_two = randint(1, len(board))
    x = [rand_row_one, rand_col_one]
    y = [rand_row_two, rand_col_two]
    turn = 0

    for turn in range(5):
        print
        "-" * 30
        print
        " "
        ship_row = int(raw_input("Enter the row: "))
        ship_col = int(raw_input("Enter the column: "))
        a = [ship_row, ship_col]
        if (a == x) or (a == y):
            print
            "Bravo! Enemy submarine down! "
            break
        elif (ship_row < 1 or ship_row > 3) or (ship_col < 1 or ship_col > 3):
            if turn == 5:
                print
                "The enemy got away! Alert the ground forces! "
            else:
                print
                "Hey! Don't hit friendly islands! "
        else:
            print
            "Aim missed! "
        turn = turn + 1
        print
        "Ammunition left: %s" % (5 - turn)
        if turn == 5:
            print
            "\nWe are out of ammo! The enemy will get away! Alert the ground forces! "

    print
    "-" * 70
    response = raw_input("Do you want to know where the submarine was? Kindly type 'y' or 'n': ")
    if response == "y":
        print
        "It was at ((%s, %s) and (%s, %s)" % (rand_row_one, rand_col_one, rand_row_two, rand_col_two)
    elif response == "n":
        print
        "Never mind! "
    while response != 'y' and response != 'n':
        response = raw_input("Please Enter valid response: ")
        if response == "y":
            print
            "It was at ((%s, %s) and (%s, %s)" % (rand_row_one, rand_col_one, rand_row_two, rand_col_two)
        elif response == "n":
            print
            "\nNever mind! "
        else:
            print
            " "
    again = raw_input("If you want to play again, press y: ")
    while again == 'y':
        print
        """--------------------------------------------------------------------
Our radars have detected enemy submarine in this area of the ocean!
The radar system is faulty and could only tell that
the enemy is in this 3x3 grid area
Let's target them and make them bite the dust! 
Good Luck!
"""

        board = []
        for i in range(3):
            i = ("O") * 3
            board.append(i)
            print
            "--".join(i)
        from random import randint

        rand_row_one = randint(1, len(board))
        rand_col_one = randint(1, len(board))
        rand_row_two = randint(1, len(board))
        rand_col_two = randint(1, len(board))
        x = [rand_row_one, rand_col_one]
        y = [rand_row_two, rand_col_two]
        turn = 0

        for turn in range(5):
            print
            "-" * 30
            print
            " "
            ship_row = int(raw_input("Enter the row: "))
            ship_col = int(raw_input("Enter the column: "))
            a = [ship_row, ship_col]
            if (a == x) or (a == y):
                print
                "Bravo! Enemy submarine down! "
                break
            elif (ship_row < 1 or ship_row > 3) or (ship_col < 1 or ship_col > 3):
                if turn == 5:
                    print
                    "The enemy got away! Alert the ground forces! "
                else:
                    print
                    "Hey! Don't hit friendly islands! "
            else:
                print
                "Aim missed! "
            turn = turn + 1
            print
            "Ammunition left: %s" % (5 - turn)
            if turn == 5:
                print
                "\nWe are out of ammo! The enemy will get away! Alert the ground forces! "

        print
        "-" * 70
        response = raw_input("Do you want to know where the submarine was? Kindly type 'y' or 'n': ")
        if response == "y":
            print
            "It was at ((%s, %s) and (%s, %s)" % (rand_row_one, rand_col_one, rand_row_two, rand_col_two)
        elif response == "n":
            print
            "Never mind! "
        while response != 'y' and response != 'n':
            response = raw_input("Please Enter valid response: ")
            if response == "y":
                print
                "It was at ((%s, %s) and (%s, %s)" % (rand_row_one, rand_col_one, rand_row_two, rand_col_two)
            elif response == "n":
                print
                "Never mind! "
        else:
            print
            " "
        again = raw_input("If you want to play again, press y: ")
    else:
        print
        "\nNever Mind! "

    print
    "-" * 70
    print
    "Thanks for playing! "
    print
    " "

elif level == 'm' or level == 'M':
    print
    """---------------------------------------------------------------------
Our radars have detected enemy submarine in this area of the ocean!
The radar system is faulty and could only tell that
the enemy is in this 5x5 grid area
Let's target them and make them bite the dust! 
Good Luck!
"""

    board = []
    for i in range(5):
        i = ("O") * 5
        board.append(i)
        print
        "--".join(i)
    from random import randint

    rand_row_one = randint(1, len(board))
    rand_col_one = randint(1, len(board))
    rand_row_two = randint(1, len(board))
    rand_col_two = randint(1, len(board))
    x = [rand_row_one, rand_col_one]
    y = [rand_row_two, rand_col_two]
    z = [rand_row_one + 1, rand_col_one]
    turn = 0
    for turn in range(10):
        print
        "-" * 30
        print
        " "
        ship_row = int(raw_input("Enter the row: "))
        ship_col = int(raw_input("Enter the column: "))
        a = [ship_row, ship_col]
        if (a == x) or (a == y) or (a == z):
            print
            "Bravo! Enemy submarine down! "
            break
        elif (ship_row < 1 or ship_row > 5) or (ship_col < 1 or ship_col > 5):
            if turn == 10:
                print
                "The enemy got away! Alert the ground forces! "
            else:
                print
                "Hey! Don't hit friendly islands! "
        else:
            print
            "Aim missed! "
        turn = turn + 1
        print
        "Ammunition left: %s" % (10 - turn)
        if turn == 10:
            print
            "\nWe are out of ammo! The enemy will get away! Alert the ground forces! "
    print
    "-" * 70
    response = raw_input("Do you want to know where the submarine was? Kindly type 'y' or 'n': ")
    if response == "y":
        print
        "It was at ((%s,%s), %s) and (%s, %s)" % (
        rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
    elif response == "n":
        print
        "Never mind! "
    while response != 'y' and response != 'n':
        response = raw_input("Please Enter valid response: ")
        if response == "y":
            print
            "It was at ((%s,%s), %s) and (%s, %s)" % (
            rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
        elif response == "n":
            print
            "\nNever mind! "
        else:
            print
            " "
    again = raw_input("If you want to play again press y: ")
    while again == 'y':
        print
        """--------------------------------------------------------------------
Our radars have detected enemy submarine in this area of the ocean!
The radar system is faulty and could only tell that
the enemy is in this 5x5 grid area
Let's target them and make them bite the dust! 
Good Luck!
"""

        board = []
        for i in range(5):
            i = ("O") * 5
            board.append(i)
            print
            "--".join(i)
        from random import randint

        rand_row_one = randint(1, len(board))
        rand_col_one = randint(1, len(board))
        rand_row_two = randint(1, len(board))
        rand_col_two = randint(1, len(board))
        x = [rand_row_one, rand_col_one]
        y = [rand_row_two, rand_col_two]
        z = [rand_row_one + 1, rand_col_one]
        turn = 0

        for turn in range(10):
            print
            "-" * 30
            print
            " "
            ship_row = int(raw_input("Enter the row: "))
            ship_col = int(raw_input("Enter the column: "))
            a = [ship_row, ship_col]
            if (a == x) or (a == y) or (a == z):
                print
                "Bravo! Enemy submarine down! "
                break
            elif (ship_row < 1 or ship_row > 5) or (ship_col < 1 or ship_col > 5):
                if turn == 10:
                    print
                    "The enemy got away! Alert the ground forces! "
                else:
                    print
                    "Hey! Don't hit friendly islands! "
            else:
                print
                "Aim missed! "
            turn = turn + 1
            print
            "Ammunition left: %s" % (10 - turn)
            if turn == 10:
                print
                "\nWe are out of ammo! The enemy will get away! Alert the ground forces! "

        print
        "-" * 70
        response = raw_input("Do you want to know where the submarine was? Kindly type 'y' or 'n': ")
        if response == "y":
            print
            "It was at ((%s,%s), %s) and (%s, %s)" % (
            rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
        elif response == "n":
            print
            "Never mind! "
        while response != 'y' and response != 'n':
            response = raw_input("Please Enter valid response: ")
            if response == "y":
                print
                "It was at ((%s,%s), %s) and (%s, %s)" % (
                rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
            elif response == "n":
                print
                "Never mind! "
        else:
            print
            " "
        again = raw_input("If you want to play again, press y: ")
    else:
        print
        "\nNever Mind! "

    print
    "-" * 70
    print
    "Thanks for playing! "
    print
    " "

elif level == 'h' or level == 'H':
    print
    """---------------------------------------------------------------------
Our radars have detected enemy submarine in this area of the ocean!
The radar system is faulty and could only tell that
the enemy is in this 5x5 grid area
Let's target them and make them bite the dust! 
Good Luck!
"""

    board = []
    for i in range(5):
        i = ("O") * 5
        board.append(i)
        print
        "--".join(i)
    from random import randint

    rand_row_one = randint(1, len(board))
    rand_col_one = randint(1, len(board))
    rand_row_two = randint(1, len(board))
    rand_col_two = randint(1, len(board))
    x = [rand_row_one, rand_col_one]
    y = [rand_row_two, rand_col_two]
    z = [rand_row_one + 1, rand_col_one]
    turn = 0
    for turn in range(5):
        print
        "-" * 30
        print
        " "
        ship_row = int(raw_input("Enter the row: "))
        ship_col = int(raw_input("Enter the column: "))
        a = [ship_row, ship_col]
        if (a == x) or (a == y) or (a == z):
            print
            "Bravo! Enemy submarine down! "
            break
        elif (ship_row < 1 or ship_row > 5) or (ship_col < 1 or ship_col > 5):
            if turn == 5:
                print
                "The enemy got away! Alert the ground forces! "
            else:
                print
                "Hey! Don't hit friendly islands! "
        else:
            print
            "Aim missed! "
        turn = turn + 1
        print
        "Ammunition left: %s" % (5 - turn)
        if turn == 5:
            print
            "\nWe are out of ammo! The enemy will get away! Alert the ground forces! "

    print
    "-" * 70
    response = raw_input("Do you want to know where the submarine was? Kindly type 'y' or 'n': ")
    if response == "y":
        print
        "It was at ((%s,%s), %s) and (%s, %s)" % (
        rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
    elif response == "n":
        print
        "Never mind! "
    while response != 'y' and response != 'n':
        response = raw_input("Please Enter valid response: ")
        if response == "y":
            print
            "It was at ((%s,%s), %s) and (%s, %s)" % (
            rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
        elif response == "n":
            print
            "\nNever mind! "
        else:
            print
            " "
    again = raw_input("If you want to play again press y: ")
    while again == 'y':
        print
        """--------------------------------------------------------------------
Our radars have detected enemy submarine in this area of the ocean!
The radar system is faulty and could only tell that
the enemy is in this 5x5 grid area
Let's target them and make them bite the dust! 
Good Luck!
"""

        board = []
        for i in range(5):
            i = ("O") * 5
            board.append(i)
            print
            "--".join(i)
        from random import randint

        rand_row_one = randint(1, len(board))
        rand_col_one = randint(1, len(board))
        rand_row_two = randint(1, len(board))
        rand_col_two = randint(1, len(board))
        x = [rand_row_one, rand_col_one]
        y = [rand_row_two, rand_col_two]
        z = [rand_row_one + 1, rand_col_one]
        turn = 0

        for turn in range(5):
            print
            "-" * 30
            print
            " "
            ship_row = int(raw_input("Enter the row: "))
            ship_col = int(raw_input("Enter the column: "))
            a = [ship_row, ship_col]
            if (a == x) or (a == y) or (a == z):
                print
                "Bravo! Enemy submarine down! "
                break
            elif (ship_row < 1 or ship_row > 5) or (ship_col < 1 or ship_col > 5):
                if turn == 5:
                    print
                    "The enemy got away! Alert the ground forces! "
                else:
                    print
                    "Hey! Don't hit friendly islands! "
            else:
                print
                "Aim missed! "
            turn = turn + 1
            print
            "Ammunition left: %s" % (5 - turn)
            if turn == 5:
                print
                "\nWe are out of ammo! The enemy will get away! Alert the ground forces! "

        print
        "-" * 70
        response = raw_input("Do you want to know where the submarine was? Kindly type 'y' or 'n': ")
        if response == "y":
            print
            "It was at ((%s,%s), %s) and (%s, %s)" % (
            rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
        elif response == "n":
            print
            "Never mind! "
        while response != 'y' and response != 'n':
            response = raw_input("Please Enter valid response: ")
            if response == "y":
                print
                "It was at ((%s,%s), %s) and (%s, %s)" % (
                rand_row_one, rand_row_one + 1, rand_col_one, rand_row_two, rand_col_two)
            elif response == "n":
                print
                "Never mind! "
        else:
            print
            " "
        again = raw_input("If you want to play again, press y: ")
    else:
        print
        "\nNever Mind! "

    print
    "-" * 70
    print
    "Thanks for playing! "
    print
    " "

closeInput = raw_input("Press ENTER to exit")