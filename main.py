import PySimpleGUI as sg
import os
from wordleGame import *


def wordle():
    guess_1 = "     "
    guess_2 = "     "
    guess_3 = "     "
    guess_4 = "     "
    guess_5 = "     "
    guess_6 = "     "
    result_1 = ["white","white","white","white","white"]
    result_2 = ["white","white","white","white","white"]
    result_3 = ["white","white","white","white","white"]
    result_4 = ["white","white","white","white","white"]
    result_5 = ["white","white","white","white","white"]
    result_6 = ["white","white","white","white","white"]
    sg.theme("dark")
    layout = [
        [sg.Text(guess_1[0],text_color="black", background_color=result_1[0], size=(2,1),  justification="center", font=("Arial",36), key="G11"),sg.Text(guess_1[1],text_color="black", background_color=result_1[1], size=(2,1),  justification="center", font=("Arial",36), key="G12"),sg.Text(guess_1[2],text_color="black", background_color=result_1[2], size=(2,1),  justification="center", font=("Arial",36), key="G13"),sg.Text(guess_1[3], text_color="black", background_color=result_1[3], size=(2,1),  justification="center", font=("Arial",36), key="G14"),sg.Text(guess_1[4],text_color="black", background_color=result_1[4], size=(2,1),  justification="center", font=("Arial",36), key="G15")],
        [sg.Text(guess_2[0],text_color="black", background_color=result_2[0], size=(2,1),  justification="center", font=("Arial",36), key="G21"),sg.Text(guess_2[1],text_color="black", background_color=result_2[1], size=(2,1),  justification="center", font=("Arial",36), key="G22"),sg.Text(guess_2[2],text_color="black", background_color=result_2[2], size=(2,1),  justification="center", font=("Arial",36), key="G23"),sg.Text(guess_2[3], text_color="black", background_color=result_2[3], size=(2,1),  justification="center", font=("Arial",36), key="G24"),sg.Text(guess_2[4],text_color="black", background_color=result_2[4], size=(2,1),  justification="center", font=("Arial",36), key="G25")],
        [sg.Text(guess_3[0],text_color="black", background_color=result_3[0], size=(2,1),  justification="center", font=("Arial",36), key="G31"),sg.Text(guess_3[1],text_color="black", background_color=result_3[1], size=(2,1),  justification="center", font=("Arial",36), key="G32"),sg.Text(guess_3[2],text_color="black", background_color=result_3[2], size=(2,1),  justification="center", font=("Arial",36), key="G33"),sg.Text(guess_3[3], text_color="black", background_color=result_3[3], size=(2,1),  justification="center", font=("Arial",36), key="G34"),sg.Text(guess_3[4],text_color="black", background_color=result_3[4], size=(2,1),  justification="center", font=("Arial",36), key="G35")],
        [sg.Text(guess_4[0],text_color="black", background_color=result_4[0], size=(2,1),  justification="center", font=("Arial",36), key="G41"),sg.Text(guess_4[1],text_color="black", background_color=result_4[1], size=(2,1),  justification="center", font=("Arial",36), key="G42"),sg.Text(guess_4[2],text_color="black", background_color=result_4[2], size=(2,1),  justification="center", font=("Arial",36), key="G43"),sg.Text(guess_4[3], text_color="black", background_color=result_4[3], size=(2,1),  justification="center", font=("Arial",36), key="G44"),sg.Text(guess_4[4],text_color="black", background_color=result_4[4], size=(2,1),  justification="center", font=("Arial",36), key="G45")],
        [sg.Text(guess_5[0],text_color="black", background_color=result_5[0], size=(2,1),  justification="center", font=("Arial",36), key="G51"),sg.Text(guess_5[1],text_color="black", background_color=result_5[1], size=(2,1),  justification="center", font=("Arial",36), key="G52"),sg.Text(guess_5[2],text_color="black", background_color=result_5[2], size=(2,1),  justification="center", font=("Arial",36), key="G53"),sg.Text(guess_5[3], text_color="black", background_color=result_5[3], size=(2,1),  justification="center", font=("Arial",36), key="G54"),sg.Text(guess_5[4],text_color="black", background_color=result_5[4], size=(2,1),  justification="center", font=("Arial",36), key="G55")],
        [sg.Text(guess_6[0],text_color="black", background_color=result_6[0], size=(2,1),  justification="center", font=("Arial",36), key="G61"),sg.Text(guess_6[1],text_color="black", background_color=result_6[1], size=(2,1),  justification="center", font=("Arial",36), key="G62"),sg.Text(guess_6[2],text_color="black", background_color=result_6[2], size=(2,1),  justification="center", font=("Arial",36), key="G63"),sg.Text(guess_6[3], text_color="black", background_color=result_6[3], size=(2,1),  justification="center", font=("Arial",36), key="G64"),sg.Text(guess_6[4],text_color="black", background_color=result_6[4], size=(2,1),  justification="center", font=("Arial",36), key="G65")],
        [sg.Text("INPUT GUESS BELOW:", font=("Arial",22))],
        [sg.InputText(font=("Arial",22),size=(15,2),key="GUESS",background_color="white",text_color="Black"),sg.Button("SUBMIT", size=(7,2))]
    ]

    screen = sg.Window("Wordle", layout, element_justification= "center")

    words = main_game()
    guess_num=1
    while True:
        screen.refresh()
        event, values = screen.read()


        if event == "SUBMIT":
            guessed_word = values["GUESS"]
            if guess_num == 1:
                result_1 = guess(guessed_word,words[0],words[1])
                if len(result_1) == 5:
                    guess_1 = values["GUESS"].upper()
                    screen["G11"].update(guess_1[0],result_1[0])
                    screen["G12"].update(guess_1[1], result_1[1])
                    screen["G13"].update(guess_1[2], result_1[2])
                    screen["G14"].update(guess_1[3], result_1[3])
                    screen["G15"].update(guess_1[4], result_1[4])
                    guess_num +=1

            elif guess_num ==2:
                result_2 = guess(guessed_word,words[0],words[1])
                if len(result_2) == 5:
                    guess_2 = values["GUESS"].upper()
                    screen["G21"].update(guess_2[0],result_2[0])
                    screen["G22"].update(guess_2[1], result_2[1])
                    screen["G23"].update(guess_2[2], result_2[2])
                    screen["G24"].update(guess_2[3], result_2[3])
                    screen["G25"].update(guess_2[4], result_2[4])
                    guess_num += 1

            elif guess_num == 3:
                result_3 = guess(guessed_word,words[0],words[1])
                if len(result_3) == 5:
                    guess_3 = values["GUESS"].upper()
                    screen["G31"].update(guess_3[0],result_3[0])
                    screen["G32"].update(guess_3[1], result_3[1])
                    screen["G33"].update(guess_3[2], result_3[2])
                    screen["G34"].update(guess_3[3], result_3[3])
                    screen["G35"].update(guess_3[4], result_3[4])
                    guess_num += 1

            elif guess_num == 4:
                result_4 = guess(guessed_word,words[0],words[1])
                if len(result_4) == 5:
                    guess_4 = values["GUESS"].upper()
                    screen["G41"].update(guess_4[0],result_4[0])
                    screen["G42"].update(guess_4[1], result_4[1])
                    screen["G43"].update(guess_4[2], result_4[2])
                    screen["G44"].update(guess_4[3], result_4[3])
                    screen["G45"].update(guess_4[4], result_4[4])
                    guess_num += 1

            elif guess_num == 5:
                result_5 = guess(guessed_word,words[0],words[1])
                if len(result_5) == 5:
                    guess_5 = values["GUESS"].upper()
                    screen["G51"].update(guess_5[0],result_5[0])
                    screen["G52"].update(guess_5[1], result_5[1])
                    screen["G53"].update(guess_5[2], result_5[2])
                    screen["G54"].update(guess_5[3], result_5[3])
                    screen["G55"].update(guess_5[4], result_5[4])
                    guess_num += 1

            elif guess_num == 6:
                result_6 = guess(guessed_word, words[0], words[1])
                if len(result_6) == 5:
                    guess_6 = values["GUESS"].upper()
                    screen["G61"].update(guess_6[0], result_6[0])
                    screen["G62"].update(guess_6[1], result_6[1])
                    screen["G63"].update(guess_6[2], result_6[2])
                    screen["G64"].update(guess_6[3], result_6[3])
                    screen["G65"].update(guess_6[4], result_6[4])
                    guess_num += 1

            if guessed_word == words[1]:
                results = [words[1], guess_num-1]
                sg.popup("You guessed corrently!")
                break

            elif guess_num > 6:
                sg.popup("YOU LOSE! The word was " + words[1])
                results = [words[1], 0]
                break

            screen["GUESS"].update("")

        if event == sg.WINDOW_CLOSED:
            break
    screen.close()
    return results










results = wordle()







