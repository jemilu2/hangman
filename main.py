import hangman_lexicon as hl
import random

def update_guessed_word(word, guessed_word, guessed_letter):
    for index,letter in enumerate(word):
        if letter == guessed_letter:
            guessed_word[index] = guessed_letter
    return guessed_word

def main():
    lexicon = hl.HangmanLexicon()
    print("Welcome to Hangman!!")
    guesses = 8
    word = lexicon.get_word(random.randint(0,lexicon.size() - 1))
    guessed_word = ["-" for i in word]
    while guesses > 0:
        print("The word now looks like this: ","".join(guessed_word))
        print("You have %s guesses left." % guesses)
        guess = input("Your guess: ")
        if len(guess) > 1:
            print("Invalid Guess. One letter at a time please")
            continue
        else:
            if guess.upper() in word:
                print("That guess is correct.")
                update_guessed_word(word,guessed_word,guess.upper())
                if "".join(guessed_word) == word:
                    break
                else:
                    continue
            else:
                guesses -= 1
    if "".join(guessed_word) == word:
        print("You guessed the word:","".join(guessed_word))
        print("You win")
    else:
        print("The word was: ",word)
        print("You lose.")

if __name__ == "__main__":
    main()