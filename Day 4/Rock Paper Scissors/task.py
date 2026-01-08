import random

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


print("ROCK, PAPER, SCISSORS")
rock_paper_scissors_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

if user_choice > 3 or user_choice < 0:
    print("Sorry, I didn't understand that. Please try again")

else:
    computer_choice = random.randint(0, 2)

    print(f"You chose: ")
    print(f"{rock_paper_scissors_list[user_choice - 1]} \n")
    print(f"Computer chose: ")
    print(f"{rock_paper_scissors_list[computer_choice - 1]} \n")

    if user_choice == 0:
        print("You lose!") if computer_choice == 1 else print("You win!")
    elif user_choice == 1:
        print("You lose!") if computer_choice == 2 else print("You win!")
    elif user_choice == 2:
        print("You lose!") if computer_choice == 0 else print("You win!")
    else:
        print("It's a tie!")