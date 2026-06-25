print('''.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
.            _.,.__       .                                   .
.           ((o\\o\))     .                                   .
.     .-.    `  \\``      .    A tropical island              .
.  __(   )___.o"^^".,___  .                                   .
.     ===    ~~~~~~~~     .                                   .
.      ==             ldb .                                   .
.       =                 .                                   .
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?").lower()
        if choice3 == "red":
        elif choice3 == "yellow":
        elif choice3 == "blue":
        else:
else:
    print("You got attacked by an angry trout. Game Over.")

else:
    print("You fell in to a hole. Game Over.")
