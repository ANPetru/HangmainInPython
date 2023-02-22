import random

word_list = ["python", "asmr", "computer", "programming", "coding", "tutorial"]


def selected_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    # Create a list of underscores to represent the unknown letters of the word
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion+"\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            # If user guesses a letter
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else: 
                print("Good job!", guess, "is in the word")
                guessed_letters.append(guess)
                # Add guess to word_completion instead of _
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            # If user guesses a word
            if guess in guessed_words:
                print("You already guessed this word")
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion, "\n")

    if guessed: 
        print("Congratulations, you guessed the word!")
    else:
        print("Sorry, you ran out of tries. The word was", word, ".")
       

def display_hangman(tries):
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
        """,

    ]
    return stages[tries]


word = selected_word()
play(word)
