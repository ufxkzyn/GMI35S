from concurrent.futures import thread
import Modules
import os
clear = lambda: os.system('cls')

#------------------------------------------- Main Menu -----------------------------------------------
while True:
    print("-------------------Huvud Meny-------------------")
    print("[1] Enkel title search (bästa matchning)       -")
    print("[2] Avancerad sökning (flera resultat)         -")
    print("[3] Sökhistorik inställningar                  -")
    print("[4] Avsluta                                    -")
    print("------------------------------------------------")
    choice = input("Välj ett alternativ (1-4): ")
    clear()
    match choice:
        case "1":
            movie_name = input("Ange filmtitel att söka efter: ")
            Modules.Api_search_best_match(movie_name)
            Modules.wait_for_keypress()
            clear()
        case "2":
            movie_name = input("Ange filmtitel att söka efter: ")
            Modules.Api_search(movie_name)
            
        case "3":
            Modules.Search_History_Options()
            Modules.wait_for_keypress()
            clear()
        case "4":
            print("Tack för att du använde vår tjänst!")
            break
        case _:
            print("Ogiltigt val. Försök igen.")
            clear()

