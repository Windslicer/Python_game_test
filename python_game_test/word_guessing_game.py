import random
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def word_guessing_game():
    print("Welcome to the Word Guessing Game!")
    
    # Initialize scores
    rounds_won = 0
    rounds_played = 0

    while True:
        print("\n" + "=" * 30)
        print("Type 'exit' at any time to quit the game.")
        print(f"Rounds played: {rounds_played} | Rounds won: {rounds_won}")
        print("=" * 30)
        
        word_list = ['apple', 'banana', 'cherry', 'grape', 'orange']
        
        word_to_guess = random.choice(word_list)
        word_length = len(word_to_guess)
        
        revealed_index = random.randint(0, word_length - 1)
        revealed_letter = word_to_guess[revealed_index]
        
        guessed_word = ['_'] * word_length
        guessed_word[revealed_index] = revealed_letter
        
        print(f"The word has {word_length} letters. A hint: The letter '{revealed_letter}' is at position {revealed_index + 1}.")

        attempts = word_length 
        
        # Emojis for the flags
        green_flag = "🟩"  
        red_flag = "🟥"    
        grey_flag = "⬜"  
        
        while attempts > 0:
            print("\nCurrent word: " + " ".join(guessed_word))
            guess = input(f"Guess a letter (You have {attempts} attempts left): ").lower()
            
            if guess == 'exit':
                print("Thank you for playing!")
                return
            
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a valid single letter.")
                continue
            
            if guess in word_to_guess:
                for index, letter in enumerate(word_to_guess):
                    if letter == guess and guessed_word[index] == '_':
                        guessed_word[index] = guess
                print(f"Good job! The letter {guess} is in the word.")
            else:
                print(f"The letter {guess} is not in the word.")
            
            print("Feedback on current letters:")
            for index, letter in enumerate(guessed_word):
                if letter == word_to_guess[index]:
                    print(f"Letter {letter}: {green_flag} (Correct position)")
                elif letter in word_to_guess and guessed_word[index] != word_to_guess[index]:
                    print(f"Letter {letter}: {red_flag} (Wrong position)")
                else:
                    print(f"Letter {letter}: {grey_flag} (Not in the word)")

            attempts -= 1
            
            if "_" not in guessed_word:
                print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
                rounds_won += 1
                break
        else:
            print(f"\nOut of attempts! The word was: {word_to_guess}")
        
        rounds_played += 1
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again == 'exit' or play_again != 'yes':
            print("Thank you for playing!")
            print(f"Final Scores: Rounds Played - {rounds_played}, Rounds Won - {rounds_won}")
            break
        
        clear_screen()

# Run the game
word_guessing_game()
