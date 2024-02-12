# Rock, Paper, Scissors images in ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Game logic
import random
# Loop three times for three rounds
for i in range(3):
    # Ask user for input
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    # Generate random choice for computer
    computer_choice = random.randint(0, 2)
    
    # Display user's choice
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)
        
    # Display computer's choice
    print("Computer chose:")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)
    
    # Determine the winner
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 2 and computer_choice == 1:
        print("You win")
    elif user_choice == computer_choice:
        print("It's a draw")
    else:
        print("You lose")
    
    # Check if it's the last round and print "Game over"
    if i == 2:
        print("Game over")

