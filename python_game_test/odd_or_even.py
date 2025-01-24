import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def odd_or_even_game():
    print("Welcome to Odd or Even!")

    player1_score = 0
    player2_score = 0
    computer_score = 0
    
    while True:
        print("\n" + "=" * 30)
        print("Type 'exit' at any prompt to end the game.")
        print(f"Scores: Player 1 - {player1_score}, Player 2/Computer - {player2_score + computer_score}")
        print("=" * 30)
        
        num_players = input("How many players (1 or 2)? ").lower()
        if num_players == 'exit':
            break
        
        if num_players == '1':
            player_choice = input("Player, do you choose Odd or Even? ").lower()
            if player_choice == 'exit':
                break

            while player_choice not in ['odd', 'even']:
                player_choice = input("Please choose either 'odd' or 'even': ").lower()

            computer_choice = 'even' if player_choice == 'odd' else 'odd'
            print(f"Computer chose {computer_choice}.")
            
            player_number = input("Player, choose a number between 1 and 5: ")
            if player_number == 'exit':
                break

            player_number = int(player_number)
            computer_number = random.randint(1, 5)
            print(f"Computer chose the number {computer_number}.")
            
            total_sum = player_number + computer_number
            print(f"Sum of the numbers: {total_sum}")

            if total_sum % 2 == 0:
                if player_choice == 'even':
                    print("Player wins!")
                    player1_score += 1
                else:
                    print("Computer wins!")
                    computer_score += 1
            else:
                if player_choice == 'odd':
                    print("Player wins!")
                    player1_score += 1
                else:
                    print("Computer wins!")
                    computer_score += 1

        elif num_players == '2':
            player1_choice = input("Player 1, do you choose Odd or Even? ").lower()
            if player1_choice == 'exit':
                break

            while player1_choice not in ['odd', 'even']:
                player1_choice = input("Player 1, please choose either 'odd' or 'even': ").lower()

            player2_choice = 'even' if player1_choice == 'odd' else 'odd'
            print(f"Player 2, you must choose {player2_choice}.")
            
            player1_number = input("Player 1, choose a number between 1 and 5: ")
            if player1_number == 'exit':
                break

            player2_number = input("Player 2, choose a number between 1 and 5: ")
            if player2_number == 'exit':
                break

            player1_number = int(player1_number)
            player2_number = int(player2_number)
            
            total_sum = player1_number + player2_number
            print(f"Sum of the numbers: {total_sum}")
            
            if total_sum % 2 == 0:
                print(f"Even sum! Player 1 chose {player1_choice}, so Player 1 wins!")
                player1_score += 1
            else:
                print(f"Odd sum! Player 2 chose {player2_choice}, so Player 2 wins!")
                player2_score += 1

        else:
            print("Invalid number of players. Choose 1 or 2.")
            continue

        input("Press Enter to continue...")
        clear_screen()


    print("\nFinal Scores:")
    print(f"Player 1: {player1_score}")
    if num_players == '1':
        print(f"Computer: {computer_score}")
    else:
        print(f"Player 2: {player2_score}")
    print("Thank you for playing!")

# Run the game
odd_or_even_game()
