import random
import JsonAndCSV
import Modules
import os
clear = lambda: os.system('cls')

#--------------------------------------- Method calling list -----------------------------------------
JsonAndCSV.save_movies_to_json()
JsonAndCSV.print_movies_list()

#------------------------------------------- Main Menu -----------------------------------------------
while True:
    print("-------------------Huvud Meny-------------------")
    print("[1] Få filmtips inom en vald Genre             -")
    print("[2] Gissa vilken film som beskrivs             -")
    print("[3] Skriv ut alla filmer i listan              -")
    print("[4] Lägg till en ny film                       -")
    print("[5] Ta bort en film från listan                -")
    print("[6] Stäng                                      -")
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
        case "4":
            Modules.Addmovie()
        case "5":
            Modules.Remove_movie()
        case "6":
            exit(0)
        

    
