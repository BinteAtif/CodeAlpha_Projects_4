import random

# Small list of 5 predefined words
words = ["python", "hangman", "coding", "laptop", "keyboard"]

def play_hangman():
    # Randomly choose a word
    word = random.choice(words).lower()
    word_letters = set(word)          # Unique letters in the word
    guessed_letters = set()           # Letters guessed by player
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("🎮 Welcome to Hangman!")
    print("You have 6 incorrect guesses allowed.\n")
    
    while incorrect_guesses < max_incorrect:
        # Display current state of the word
        current_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: " + " ".join(current_word))
        
        # Show remaining guesses
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Get player guess
        guess = input("\nGuess a letter: ").lower().strip()
        
        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter only.")
            continue
        
        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!")
            continue
        
        # Add guess to guessed letters
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word_letters:
            print("✅ Good guess!")
            # Check if player has won
            if word_letters.issubset(guessed_letters):
                print("\n🎉 Congratulations! You guessed the word:", word.upper())
                break
        else:
            incorrect_guesses += 1
            print(f"❌ Wrong guess! {max_incorrect - incorrect_guesses} guesses left.")
    
    # Game Over
    if incorrect_guesses == max_incorrect:
        print("\n💀 Game Over! The word was:", word.upper())
    
    # Play again?
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again == 'y':
        print("\n" + "="*40)
        play_hangman()
    else:
        print("Thanks for playing Hangman! 👋")

# Start the game
if __name__ == "__main__":
    play_hangman()