import random
import os
import msvcrt as m
import json
import JsonAndCSV

clear = lambda: os.system('cls')
#List_Of_Movies = []

def wait_for_keypress():
    print("Tryck på valfri knapp för att fortsätta...")
    m.getch()
    
# --------------------------------------------------------------------------------------
# ---------------------------Search of movies based on genre----------------------------
def MovieBasedOnGenre():
    movies = JsonAndCSV.movies_container.get_movies()
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
    # User input for genre
    Genre = input('Ange genre du vill söka efter: ')
    Temporary_List = []
    Temporary_List.clear()
    for movie in MovieBasedOnGenre:
        if movie['genre'].title() == Genre.title():
            Temporary_List.append(movie)
    # Check if any movies were found    
    if not Temporary_List:
        print("Inga filmer hittades för den valda genren.")
        wait_for_keypress()
        clear()
        return
    # Random choice from the temporary list
    Rekomended_Movie = random.choice(Temporary_List)
    print('Here is a recommendation for you based on the genre you choosed:' '\n')
    print(f"Rekommenderad film inom genren {Rekomended_Movie['genre']}:")
    print(f"Titel: {Rekomended_Movie['titel']}")
    print(f"Beskrivning: {Rekomended_Movie['beskrivning']}\n")
    wait_for_keypress()
    clear()
# --------------------------------------------------------------------------------------
# --------------------------- Movie guessing game --------------------------------------
def MovieGeneration_Guess():
    try:
        with open('json_file', 'r', encoding='utf-8') as json_file_pointer:
            movies = json.load(json_file_pointer)
            
            if not movies:
                print("Inga filmer tillgängliga.")
                wait_for_keypress()
                clear()
                return
            
            Chosen_Movie = random.choice(movies)
            print(f"Gissa utifrån detta: {Chosen_Movie['beskrivning']}")
            if input("Vad är din gissning? ") == Chosen_Movie['titel']:
                print("Rätt gissat!\n")
            else:
                print(f"Fel gissat! Rätt svar är: {Chosen_Movie['titel']}\n")
            wait_for_keypress()
            clear()
    #Fel hantering för filen
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
    movies = JsonAndCSV.movies_container.get_movies()
    if not movies:
        print("Inga filmer tillgängliga.")
        return
    print("-------------------------------- Alla filmer i listan -----------------------------------")
    for movie in movies:
        print(f"{movie['titel']}\n{movie['genre']}\n{movie['beskrivning']}")
        print("------------------------------------------------")
    print("Press any key to continue...")
    wait_for_keypress()
    clear()
# --------------------------------------------------------------------------------------
# -------- Method to add a movie to the json file --------------------------------------
def Addmovie():
    with open('json_file', 'r', encoding='utf-8') as json_file_pointer:
        Show_movies_from_json = json.load(json_file_pointer)
    #information som behövs för att lägga till en ny film
    New_movie_title = input("Ange filmtitel: ")
    clear()
    New_movie_genre = input("Ange filmgenre: ")
    clear()
    New_movie_description = input("Ange filmbeskrivning: ")
    clear()
    # Skapa en ny filmpost och lägg till i listan
    New_movie = {
        'titel': New_movie_title,
        'genre': New_movie_genre,
        'beskrivning': New_movie_description
    }
    Show_movies_from_json.append(New_movie)
    # Spara den uppdaterade listan tillbaka till json-filen
    with open('json_file', 'w', encoding='utf-8') as json_file_pointer:
        json.dump(Show_movies_from_json, json_file_pointer, ensure_ascii=False, indent=4)

    # Uppdatera delad container så resten av programmet får senaste listan
    JsonAndCSV.movies_container.set_movies(Show_movies_from_json)
    
    print(f"Filmen '{New_movie_title}' har lagts till i listan.")
    print("Press any key to continue...")
    wait_for_keypress()
    clear()
#--------------------------------------------------------------------------------------
# -------- Method to remove a movie from the json file --------------------------------
def Remove_movie():
    with open('json_file', 'r', encoding='utf-8') as json_file_pointer:
        Show_movies_from_json = json.load(json_file_pointer)
    
    Movie_to_remove = input("Ange titeln på filmen du vill ta bort: ")
    clear()
    for movie in Show_movies_from_json:
        if movie['titel'].title() == Movie_to_remove.title():
            Show_movies_from_json.remove(movie)

            # Spara ändringen och uppdatera delad container
            with open('json_file', 'w', encoding='utf-8') as json_file_pointer:
                json.dump(Show_movies_from_json, json_file_pointer, ensure_ascii=False, indent=4)
            JsonAndCSV.movies_container.set_movies(Show_movies_from_json)

            print(f"Filmen '{Movie_to_remove}' har tagits bort.")
            break
    # Om filmen inte hittades
    else:
        print(f"Filmen '{Movie_to_remove}' hittades inte.")
    print("Press any key to continue...")
    wait_for_keypress()
    clear()
    
#--------------------------------------------------------------------------------------
# -------- Method to remove all movies from the json file --------------------------------
def Remove_all_movies():
    with open('json_file', 'w', encoding='utf-8') as json_file_pointer:
        json.dump([], json_file_pointer, ensure_ascii=False, indent=4)


#--------------------------------------------------------------------------------------
# -------- Method to search for specific movie by name --------------------------------
def Movie_Search():
    with open ('json_file.json', 'r', encoding='utf-8',) as json_file_pointer:
        Movie_Searched = []
        Movies_Data = json.load(json_file_pointer)
        Movie_Searched = input("Ange film att söka efter: ")
        Search_Results = []
        print(Movies_Data)
        for movie in Movies_Data:
            if movie['title'].title() == Movie_Searched.title():
                Search_Results.append(movie)
                print("Film hittad:")
                print(movie)
                Write_Search_History()
        if not Search_Results:
            print("Ingen film hittades med det namnet.")

#--------------------------------------------------------------------------------------
# -------- Documents search history from previous method --------------------------------
def Write_Search_History():
    with open ('search_history.csv', mode='w', newline='', encoding='utf-8') as Search_History_Pointer:
        writer = csv.DictWriter(Search_History_Pointer, delimiter=';')
        writer.writeheader(['Sökning', 'Resultat', 'Datum och Tid'])
        writer.writerow({'Sökning': Movie_Searched, 'Resultat': Search_Results, 'Datum och Tid': Modules.get_current_datetime()})

#--------------------------------------------------------------------------------------
# -------- Menu for searching movies --------------------------------
def Search_History_Options():
    with open ('search_history.csv', mode='r', newline='', encoding='utf-8') as Search_History_Pointer:
        reader = csv.reader(Search_History_Pointer)
        while True:
            print("Sök historik:")
            print("Vad vill du göra?")
            print("1. Visa sökhistorik")
            print("2. Välj film att titta på från sökhistoriken")
            print("3. Rensa all sökhistorik")
            print("4. Backa till huvudmenyn")
            choice = input("Ange ditt val (1-4): ")
