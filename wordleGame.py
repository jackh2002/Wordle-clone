# Wordle bot
import random
import PySimpleGUI as sg


def grab_words(file):  # Grabs word list and guess list
    possible_words = []
    f = open(file,"r")
    for line in f:
        possible_words.append(line.strip())
    f.close()
    return possible_words


def guess(word, word_list, word_to_guess):  # Guess logic
    result = []
    if word not in word_list:
        return ["white","white","white","white","white","invalid"]
    else:
        for letter in range(0,5):
            if word.count(word[letter]) > word_to_guess.count(word[letter]):
                word = word.replace(word[letter], ".", word.count(word[letter])-word_to_guess.count(word[letter]))
            if word[letter] in word_to_guess:
                if word[letter] == word_to_guess[letter]:
                    result.append("green")

                else:
                    result.append("orange")

            else:
                result.append("white")



    return result


def main_game():  # guess log
    possible_words = grab_words("wordle-answers-alphabetical.txt")
    possible_guesses = grab_words("valid-wordle-guesses.txt")
    word_to_guess = possible_words[random.randint(0, len(possible_words) - 1)]
    values= [possible_guesses,word_to_guess]
    return values











