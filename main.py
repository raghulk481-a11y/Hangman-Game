import random

def play_hangman():
    # List of words to choose from
    words = ['python', 'programming', 'software', 'developer', 'algorithm', 'jupiter', 'hangman', 'challenge', 'function', 'variable','computer','keyboard','monitor','mouse','internet','network','database','security','encryption','debugging','performance','optimization','artificial','intelligence','machine','learning','data','science','analytics','visualization','cloud','computing','virtualization','containerization','orchestration','automation','scripting','testing','deployment','scalability','reliability','availability','maintainability','usability','accessibility','compatibility','portability','interoperability','extensibility','modularity','reusability','efficiency','effectiveness','productivity','collaboration','communication','teamwork','leadership','innovation','creativity','problem-solving','critical-thinking','decision-making','time-management','organization','adaptability','resilience']
    word = random.choice(words).lower()
    
    guessed_letters = []
    attempts = 6
    
    # Visual representation of the gallows
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |      
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |      
           -
        """
    ]

    print("Welcome to Hangman!")
    
    while attempts > 0:
        # Create the display word (e.g., "p _ t h _ n")
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(stages[attempts])
        print(f"Word: {display_word}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        # Check if the player won
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").lower()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Nice! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not there.")
            attempts -= 1

    if attempts == 0:
        print(stages[0])
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
