from unittest import case
import requests
import os
import msvcrt as m
import json
import csv
import datetime

Clear = lambda: os.system('cls')
def wait_for_keypress():
    print("Tryck på valfri knapp för att fortsätta...")
    m.getch()


# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

#--------------------------------------------------------------------------------------
# -------- A function used to clean up the given data from the api --------------------
def Json_Clean_Up():
    cleaned_data = {}
    with open(os.path.join(SCRIPT_DIR, 'SpecificMovieDetails.json'), 'r') as api_file_pointer:
        api_data = json.load(api_file_pointer)
    for key, value in api_data.items():
        if value == "N/A":
            continue
        else:
            cleaned_data[key] = value
    with open(os.path.join(SCRIPT_DIR, 'SpecificMovieDetails.json'), 'w', encoding='utf-8') as cleaned_file_pointer: 
        json.dump(cleaned_data, cleaned_file_pointer, indent=4, ensure_ascii=False, ) #puts everything back into the same file
#--------------------------------------------------------------------------------------
# -------- Method to print out all keys in API data--------------------
def All_Keys_in_API():
    Json_Clean_Up()
    with open(os.path.join(SCRIPT_DIR, 'SpecificMovieDetails.json'), 'r', encoding='utf-8') as json_file_pointer:
        Movies_Data = json.load(json_file_pointer)
        print("Här är alla nycklar du kan få information om:")
        print('-------------------------')
        for key in Movies_Data.keys():
                print(f"{key}")
        print('-------------------------')
        try: 
            chosen_key = input("Skriv namnet på nyckeln du vill ha information om: ")
            if chosen_key in Movies_Data:
                print(f"{chosen_key}: {Movies_Data[chosen_key]}")
            else:
                print("Ogiltigt val, nyckeln finns inte.")
        except Exception:
            print(f"Ett fel uppstod:")
#--------------------------------------------------------------------------------------
# -------- Method to get specific movie details by IMDB ID from the API--------------------
def Specific_Movie_Details(IMDB_ID):
    with open(os.path.join(SCRIPT_DIR, 'API_Key.txt'), 'r') as api_file_specific:
        
        try:
            api_key_specific = api_file_specific.read().strip()
            API_Response_Specific = requests.get(f'http://www.omdbapi.com/?apikey={api_key_specific}&i={IMDB_ID}&plot=full&tomatoes=true')
            API_Data_Specific = API_Response_Specific.json()
        except Exception as e:
            print(f"Ett fel uppstod vid hämtning av filmdata: {e}")
        else:
            if API_Data_Specific.get('Response') == 'False':
                print('Ingen film hittades med det IMDB ID:t.')
                return
            with open(os.path.join(SCRIPT_DIR, 'SpecificMovieDetails.json'), 'w', encoding='utf-8') as specific_movie_file:
                json.dump(API_Data_Specific, specific_movie_file, indent=4, ensure_ascii=False)
            print(f"Title: {API_Data_Specific.get('Title')}")
            print(f"Year: {API_Data_Specific.get('Year')}")
            print(f"Director: {API_Data_Specific.get('Director')}")
            
            print('Vill du ha mer information om filmen? (j/n)')
            if input().lower() == 'j':# J har inte funkat tidigare, men det borde funka nu idk
                Clear()
                print('Här är all information du kan få:')
                All_Keys_in_API()
                
            else:
                Clear()
                print('Tack för att du använde vår tjänst!')
#--------------------------------------------------------------------------------------
# -------- Method to handle multiple movies found from the API--------------------
def Multiple_Movies_found(): 
    with open(os.path.join(SCRIPT_DIR, 'ApiResponse.json'), 'r', encoding='utf-8') as json_file_pointer:
        Movies_Data = json.load(json_file_pointer)
        if Movies_Data['Response'] == 'True':
            if (len(Movies_Data['Search']) >= 2):  
                print('Flera filmer hittades:')
                print('-------------------------')# denna metod printar ut alla filmer i ett fromat som du kan se nedan
                for movie in Movies_Data['Search']:
                    print(f"Titel: {movie['Title']}\nÅr: {movie['Year']}\nIMDB ID: {movie['imdbID']}")
                    print('-------------------------')
            elif (len(Movies_Data['Search']) == 1):  
                print('En film hittades:')
                print('-------------------------')
                movie = Movies_Data['Search'][0]
                print(f"Titel: {movie['Title']}\nÅr: {movie['Year']}\nIMDB ID: {movie['imdbID']}")
                print('-------------------------')
        elif Movies_Data['Response'] == 'False':
            print('Ingen film hittades med det namnet.')

    Specific_Movie_Details(input("Skriv dess IMDB ID (t:ex tt0111161, se sista snutten på informationen du fick): ")) 
    if Movies_Data['Response'] == 'False':
        print('Ingen film hittades med den IMDB ID:n finns.')
    
    
#--------------------------------------------------------------------------------------
# -------- Documents search history from previous method --------------------------------
def Write_Search_History(Movie_Searched):
    with open(os.path.join(SCRIPT_DIR, 'search_history.csv'), mode='a', newline='', encoding='utf-8') as Search_History_Pointer:
        writer = csv.DictWriter(Search_History_Pointer, delimiter=';',fieldnames=['Sökning', 'Datum och Tid'])
        writer.writerow({'Sökning': Movie_Searched, 'Datum och Tid': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        
#--------------------------------------------------------------------------------------
# -------- Method to search for specific movie by name from the API--------------------
def Api_search(Movie_Searched):
    with open(os.path.join(SCRIPT_DIR, 'API_Key.txt'), 'r') as api_file:
        api_key = api_file.read().strip()
    API_Response = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&s={Movie_Searched}')
    API_Data = API_Response.json()
    # this method also saves the API response in a json file for later use, this is used to store the data for the multiple movies found method
    with open(os.path.join(SCRIPT_DIR, 'ApiResponse.json'), 'w', encoding='utf-8') as fpoiner:
        json.dump(API_Data, fpoiner, indent=4, ensure_ascii=False)
    if API_Data.get('Response') == 'True' and len(API_Data['Search']) >= 1:
        Multiple_Movies_found()

#--------------------------------------------------------------------------------------
# -------- Method to search for specific movie by name from the API and get the best match----------------
def Api_search_best_match(Movie_Searched):
    with open(os.path.join(SCRIPT_DIR, 'API_Key.txt'), 'r') as api_file:
        api_key = api_file.read().strip()
    API_Response = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&s={Movie_Searched}')
    API_Data = API_Response.json()
    
    Write_Search_History(Movie_Searched)
    
    if not API_Data.get('Search'):
        print('Ingen film hittades med det namnet.')
        return
    
    # Find the closest match using simple string similarity
    best_match = None
    best_score = 0
    
    for movie in API_Data['Search']:
        # Count matching characters (simple similarity)
        score = sum(1 for c in Movie_Searched.lower() if c in movie['Title'].lower())
        if score > best_score:
            best_score = score
            best_match = movie
    # This only gives the best matching movies, and then it prints the infromation about it.
    if best_match:
        print(f"Bästa matchning: {best_match['Title']} ({best_match['Year']})")
        Specific_Movie_Details(best_match['imdbID'])
    else:
        print('Ingen film hittades.')

#--------------------------------------------------------------------------------------
# -------- Menu for search history--------------------------------
def Search_History_Options():
    # Load history data from CSV
    history_data = []
    try:
        with open(os.path.join(SCRIPT_DIR, 'search_history.csv'), mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            history_data = list(reader)
    except FileNotFoundError:
        history_data = []
    
    print("Sök historik:")
    print("Vad vill du göra?")
    print("----------------------------------------------")
    print("1. Visa sökhistorik                          -")                        
    print("2. Rensa all sökhistorik                     -")
    print("3. Backa till huvudmenyn                     -")
    print("----------------------------------------------")
    choice = input("Ange ditt val (1-3): ")
    
    match choice:
        case "1":
            print('Here is your search history:')
            print('-------------------------')
            for row in history_data:
                if row:  # Skip empty rows
                    print(f"Sökning: {row[0]}, \nTid: {row[1]}\n-------------------------")
        case "2":
            open(os.path.join(SCRIPT_DIR, 'search_history.csv'), 'w').close()
            print("Historik raderad.")

        case "3":
            return  
        case _:
            print("Ogiltigt val.")
