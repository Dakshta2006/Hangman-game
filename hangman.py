import random

words_list = [
    'algorithm', 'function', 'variable', 'compile',
    'iterate', 'recursion', 'binary', 'array', 'syntax', 'pointer'
]

def choose_word():
    return random.choice(words_list)

def display_header(attempts_left):
    header = "HANGMAN"
    # Adjust the pointer position so it starts under 'H'
    pointer = " " * attempts_left + "^"
    print(header)
    print(pointer)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print("Word: " + display)

def play_game():
    word = choose_word()
    attempts = len("HANGMAN") - 1  # Number of incorrect guesses allowed
    guessed_letters = []
    correct_guesses = set(word)
    
    while attempts > 0:
        display_header(len("HANGMAN") - attempts)
        display_word(word, guessed_letters)
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in correct_guesses:
            correct_guesses.remove(guess)
            if not correct_guesses:
                display_word(word, guessed_letters)
                print("Phew… you are saved!")
                break
        else:
            attempts -= 1
            if attempts == 0:
                print("HANGMAN")
                print("You are hanged.")
                print(f"The word was: {word}")
                break

def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing :)")
            break

if __name__ == "__main__":
    main()

