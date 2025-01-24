import random
import os

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

choices = [rock, paper, scissors]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rock_paper_scissors_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    human_score = 0
    computer_score = 0
    
    while True:
        print("\n" + "=" * 30)
        print("Type 'exit' to end the game.")
        print(f"Scores: You - {human_score}, Computer - {computer_score}")
        print("=" * 30)
        
        human_input = input("Press 0 for Rock, 1 for Paper, 2 for Scissors: ").lower()
        if human_input == 'exit':
            break

        if not human_input.isdigit() or int(human_input) not in [0, 1, 2]:
            print("Invalid input! Please choose 0, 1, or 2.")
            continue

        human = int(human_input)
        computer = random.randint(0, 2)

        print("\nYou chose:")
        print(choices[human])
        print("Computer chose:")
        print(choices[computer])

        if human == computer:
            print("It's a draw!")
        elif (human == 0 and computer == 2) or (human == 1 and computer == 0) or (human == 2 and computer == 1):
            print("You won!!!!")
            human_score += 1
        else:
            print("You lost, try again!")
            computer_score += 1

        input("Press Enter to continue...")
        clear_screen()

    print("\nFinal Scores:")
    print(f"You: {human_score}")
    print(f"Computer: {computer_score}")
    print("Thank you for playing!")

# Run the game
rock_paper_scissors_game()
