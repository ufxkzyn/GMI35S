import random
import os
import msvcrt as m
import json
#import csv

clear = lambda: os.system('cls')
  
def wait_for_keypress():
    print("Tryck på valfri knapp för att fortsätta...")
    m.getch()
# --------------------------------------------------------------------------------------
# ---------------------------Search of movies based on genre----------------------------
def MovieBasedOnGenre():
    try:
        with open('json_file', 'r', encoding = 'utf-8', ) as json_file_pointer:
            MovieBasedOnGenre = json.load(json_file_pointer)
            print('Sök efter genres tillgängliga:')
            Genre_list = []
            for movie in MovieBasedOnGenre:
                if movie['genre'] not in Genre_list:
                    Genre_list.append(movie['genre'])

            for genre in Genre_list:
                print(genre)
    except FileNotFoundError:
        print("Fel: 'json_file' hittades inte. Se till att filen finns i rätt katalog.")
        wait_for_keypress()
        clear()
        return
    except json.JSONDecodeError:
        print("Fel: 'json_file' innehåller ogiltig JSON. Kontrollera filens innehåll.")
        wait_for_keypress()
        clear()
        return
    
    Genre = input('Ange genre du vill söka efter: ')
    Temporary_List = []
    Temporary_List.clear()
    for movie in MovieBasedOnGenre:
        if movie['genre'].title() == Genre.title():
            Temporary_List.append(movie)

    Rekomended_Movie = random.randint(0, len(Temporary_List) - 1)
    print('Here is a recommendation for you based on the genre you choosed:' '\n')
    print(f"Rekommenderad film inom genren {Temporary_List[Rekomended_Movie]['genre']}:")
    print(f"Titel: {Temporary_List[Rekomended_Movie]['Titel']}")
    print(f"Beskrivning: {Temporary_List[Rekomended_Movie]['Beskrivning']}\n")
    wait_for_keypress()
    clear()
# --------------------------------------------------------------------------------------
# --------------------------- Movie guessing game --------------------------------------
def MovieGeneration_Guess():
    try:
        with open('json_file', 'r', encoding = 'utf-8', ) as json_file_pointer:
            TempList_Guess = []
            TempList_Guess.clear()
            TempList_Guess = [random.choice()] 
            print(f"Gissa utifrån detta: ", TempList_Guess[0]['Beskrivning'])
            if input("Vad är din gissning?") == TempList_Guess[0]['Titel']:
                print("Rätt gissat!\n")
            else:
                print(f"Fel gissat! Rätt svar är: {TempList_Guess[0]['Titel']}\n")
            wait_for_keypress()
            clear()
            
    except FileNotFoundError:
        print("Fel: 'json_file' hittades inte. Se till att filen finns i rätt katalog.")
        wait_for_keypress()
        clear()
        return
    except json.JSONDecodeError:  
        print("Fel: 'json_file' innehåller ogiltig JSON. Kontrollera filens innehåll.")
        wait_for_keypress()
        clear()
        return
# --------------------------------------------------------------------------------------   
# -------- Method to read out and display the movies contained in the json file --------
def PrintAllMovies():
    with open('json_file', 'r', encoding = 'utf-8', ) as json_file_pointer:
        Show_movies_from_json = json.load(json_file_pointer)
        for movie in Show_movies_from_json:
            print(f"{movie['titel']} {movie['genre']} {movie['beskrivning']}")
# --------------------------------------------------------------------------------------
