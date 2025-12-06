## Rock Paper Scissors Game

# In Rock Paper Scissors, two players simultaneously form one of three hand shapes: rock (a fist), paper (a flat hand), or scissors (a fist with two fingers extended). The winner is determined by these rules: rock crushes scissors, scissors cuts paper, and paper covers rock. If both players choose the same shape, the round is a tie, and it is played again. 

# Symbols or emojis:
# 1. Scissors - (✌️)
# 2. Rock - (✊)
# 3. Paper - (✋)

# Rule : 
# 1. Rock wins against Scissors
# 2. Scissors wins against Paper
# 3. Paper wins against Rock


# O for Rock
# 1 for Paper
# 2 for Scissors

# user has 0,1, and 2 choice
# Also computer has 0,1, and 2 choice 

# There are 9 possible patterns :
# 1.    0 - 0 : Draw 
# 2.    0 - 1 : computer wins (Paper wins)
# 3.    0 - 2 : user wins (Rock wins)
# 4.    1 - 0 : user wins (Paper wins)
# 5.    1 - 1 : Draw
# 6.    1 - 2 : computer wins (Scissors wins)
# 7.    2 - 0 : computer wins (Rock wins)
# 8.    2 - 1 : user wins (Scissors win)
# 9.    2 - 2 : Draw


import random 
#Imports Python’s built-in random module so the program can generate random numbers (used for the computer’s choice).

user_choice = int(input(f'Enter your choice : \n 0 for Rock \n 1 for Paper \n 2 for Scissor \n - '))
# input(...) displays the prompt and waits for the user to type something and press Enter.
# int(...) converts the typed string into an integer (so the program can compare choices numerically).
# The result is stored in the variable user_choice.
# Note: If the user types something that is not an integer (e.g., "a"), this line will raise a ValueError.

computer_choice = random.randint(0,2)
# Calls random.randint(0, 2) which returns a random integer 0, 1, or 2 (both endpoints included).
# Stores that integer in computer_choice. This is the computer’s move.

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
#Defines a multi-line string variable rock that contains ASCII art representing the "rock" hand.

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
#Defines a multi-line string variable paper that contains ASCII art representing the "paper" hand.

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#Defines a multi-line string variable scissors that contains ASCII art representing the "scissors" hand.

games_images = [rock, paper, scissors]
#Creates a list named games_images whose elements are the three ASCII-art strings in the order [rock, paper, scissors]. This makes it easy to print the matching image by index (0 → rock, 1 → paper, 2 → scissors).

if user_choice >= 3 or user_choice <0:
    print("You entered invalid choice!!")
#Checks whether the user entered a number outside the valid range (0, 1, 2).
# If the number is invalid, it prints an error message and the rest of the else: block is skipped.


else:
    print(f"user_choice : {user_choice}")
    print(games_images[user_choice])
    print(f"computer_choice : {computer_choice}")
    print(games_images[computer_choice])
    #Executed only when the user gave a valid choice (0–2).
        # Prints the numeric user choice.
        # Prints the ASCII art corresponding to the user’s choice by indexing games_images[user_choice].
        # Prints the numeric computer choice.
        # Prints the ASCII art for the computer’s choice.

    if computer_choice == user_choice:
        print("It's draw.")
        #If both choices are the same, it's a tie and prints “It’s draw.”

    elif user_choice==0 and computer_choice==2:
        print("You win.")
        #Special case: user picked Rock (0) and computer picked Scissors (2). Rock beats Scissors → user wins.

    elif user_choice==2 and computer_choice==0:
        print("You lose.")
        #Special case: user picked Scissors (2) and computer picked Rock (0). Rock beats Scissors → user loses.

    elif computer_choice > user_choice:
        print("You lose.")

    elif user_choice > computer_choice:
        print("You win")
    
        #These two numeric comparisons cover the remaining scenarios:
            # If computer_choice is numerically greater than user_choice, the program prints "You lose."
            # If user_choice is greater than computer_choice, it prints "You win".

    #Because the two special rock-scissors cases were handled first, these simple numeric comparisons work for the paper/rock/scissor relationships in the remaining cases.