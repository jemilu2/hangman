import hangman_lexicon as hl
import random

def update_guessed_word(word, guessed_word, guessed_letter):
    for index,letter in enumerate(word):
        if letter == guessed_letter:
            guessed_word[index] = guessed_letter
    return guessed_word

def main(hangman=None):
    lexicon = hl.HangmanLexicon()
    print("Welcome to Hangman!!")
    if hangman is not None:
        hangman.draw_scaffold()
    guesses = 8
    word = lexicon.get_word(random.randint(0,lexicon.size() - 1))
    guessed_word = ["-" for i in word]
    guessed_letters = ""
    while guesses > 0:
        if hangman is not None:
            hangman.display_words(guessed_word,guessed_letters)
        print("The word now looks like this: ","".join(guessed_word))
        print("You have %s guesses left." % guesses)
        guess = input("Your guess: ")
        if len(guess) > 1:
            print("Invalid Guess. One letter at a time please.")
            continue
        else:
            guessed_letters += guess.upper()
            if guess.upper() in word:
                print("That guess is correct.")
                update_guessed_word(word,guessed_word,guess.upper())
                if "".join(guessed_word) == word:
                    break
                else:
                    continue
            else:
                guesses -= 1
                print("There are no %s's in the word." % guess.upper())
                if hangman is not None:
                    hangman.note_incorrect_guess()
    if "".join(guessed_word) == word:
        print("You guessed the word:","".join(guessed_word))
        print("You win")
    else:
        print("You're completely hung!")
        print("The word was: ",word)
        print("You lose.")

if __name__ == "__main__":
    import hangman_canvas as hc
    import tkinter
    import time
    root = tkinter.Tk()
    app = hc.HangmanCanvas(master=root)
    main(hangman=app)
    time.sleep(5)