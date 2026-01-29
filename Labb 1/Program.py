import random
import Modules
import os
clear = lambda: os.system('cls')
while True:

    print("-------------------Huvud Meny-------------------")
    print("[1] Få filmtips inom en vald Genre             -")
    print("[2] Gissa vilken film som beskrivs             -")
    print("[3] Skriv ut alla filmer i listan              -")
    print("[5] Stäng                                      -")
    print("------------------------------------------------")
    choice = input()
    clear()
    match choice:
        case "1":
            Modules.MovieBasedOnGenre()
        case "2":
            Modules.MovieGeneration_Guess()
        case "3":
            Modules.PrintAllMovies()
            pass
        case "5":
            exit(0)


    
