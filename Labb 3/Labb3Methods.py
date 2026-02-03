import requests
import random
import os
import msvcrt as m
import json
import JsonAndCSV
import csv
import Modules
import webbrowser
import datetime

#--------------------------------------------------------------------------------------
# -------- Method to remove dead values--------------------
def Json_Clean_Up():
    with open('SpecificMovieDetails.json', 'r') as api_file_pointer:
        api_data = json.load(api_file_pointer)
    cleaned_data = {}
    for key, value in api_data.items():
        if value != "" and value != "N/A": # The Values that sometimes show up empty look like "" or N/A
            cleaned_data[key] = value #ovewrites all inputs that are not empty or N/A
    with open('SpecificMovieDetails.json', 'w', encoding='utf-8') as cleaned_file_pointer: 
        json.dump(cleaned_data, cleaned_file_pointer, indent=4, ensure_ascii=False) #puts everything back into the same file
#--------------------------------------------------------------------------------------
# -------- Method to get specific movie details from the saved API data--------------------
def Get_Specific_Movie_Details():
    Specific_Key_Information = input("Ange vilken information du vill ha om filmen (t.ex. Title, Year, Director, etc.): ")
    with open('SpecificMovieDetails.json', 'r') as api_file_pointer:
        saved_api_data = json.load(api_file_pointer)
        if Specific_Key_Information in saved_api_data: #even though we cleaned up, we are still checking if the user writes a valid key
            print(f"{Specific_Key_Information}: {saved_api_data[Specific_Key_Information]}")
        else:
            print("Den angivna nyckeln finns inte i API-datan.")

#--------------------------------------------------------------------------------------
# -------- Method to print out all keys in API data--------------------
def All_Keys_in_API():
    Json_Clean_Up()
    with open('SpecificMovieDetails.json', 'r') as api_file_pointer:
        api_data = json.load(api_file_pointer)
        for key in api_data.keys():
            print(key)
    Get_Specific_Movie_Details()

#--------------------------------------------------------------------------------------
# -------- Method to get specific movie details by IMDB ID from the API--------------------
def Specific_Movie_Details(IMDB_ID):
    with open('API_Key.txt', 'r') as api_file_specific:
        api_key_specific = api_file_specific.read().strip()
        API_Response_Specific = requests.get(f'http://www.omdbapi.com/?apikey={api_key_specific}&i={IMDB_ID}')
        API_Data_Specific = API_Response_Specific.json()
        with open('SpecificMovieDetails.json', 'w', encoding='utf-8') as specific_movie_file:
            json.dump(API_Data_Specific, specific_movie_file, indent=4, ensure_ascii=False)
        print(f"Title: {API_Data_Specific['Title']},\n Year: {API_Data_Specific['Year']},\n Director: {API_Data_Specific['Director']}")
        print('Vill du ha mer information om filmen? (j/n)')
        if input().lower() == 'j':
            print('Här är all information du kan få:')
            All_Keys_in_API()
        else:
            print('Tack för att du använde vår tjänst!')
#--------------------------------------------------------------------------------------
# -------- Method to handle multiple movies found from the API--------------------
def Multiple_Movies_found():
    with open('ApiResponse.json', 'r', encoding='utf-8') as json_file_pointer:
        Movies_Data = json.load(json_file_pointer)
        if Movies_Data['Response'] == 'True':
            print('Flera filmer hittades:')
            for movie in Movies_Data['Search']:
                print(f"Titel: {movie['Title']}, År: {movie['Year']}, IMDB ID: {movie['imdbID']}")
        else:
            print('Ingen film hittades med det namnet.')
    Specific_Movie_Details(input("Skriv dess IMDB ID (t:ex tt0111161, se sista snutten på informationen du fick): "))
    
    
#--------------------------------------------------------------------------------------
# -------- Documents search history from previous method --------------------------------
def Write_Search_History(Movie_Searched, Search_Results):
    with open('search_history.csv', mode='a', newline='', encoding='utf-8') as Search_History_Pointer:
        writer = csv.DictWriter(Search_History_Pointer, delimiter=';',fieldnames=['Sökning', 'Resultat', 'Datum och Tid'])
        writer.writerow({'Sökning': Movie_Searched, 'Resultat': Search_Results, 'Datum och Tid': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        
#--------------------------------------------------------------------------------------
# -------- Method to search for specific movie by name from the API--------------------
def Api_search(Movie_Searched):
    with open('API_Key.txt', 'r') as api_file:
        api_key = api_file.read().strip()
    API_Response = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&s={Movie_Searched}')
    API_Data = API_Response.json()
    
    Search_Results = [] #To store all the titles found for logging purposes
    for movie in API_Data.get('Search', []):
        Search_Results.append(movie['Title'])
    Write_Search_History(Movie_Searched, Search_Results)
    
    with open('ApiResponse.json', 'w', encoding='utf-8') as fpoiner:
        workingdata = json.dumps(API_Data)
        fpoiner.write(workingdata)
    if API_Data['Search'] and len(API_Data['Search']) > 1:
        Multiple_Movies_found()

#--------------------------------------------------------------------------------------
# -------- Menu for search history--------------------------------
def Search_History_Options():
    with open ('search_history.csv', mode='r', newline='', encoding='utf-8') as Search_History_Pointer:
        reader = csv.reader(Search_History_Pointer)
        print("Sök historik:")
        print("Vad vill du göra?")
        print("1. Visa sökhistorik")
        print("2. Välj film att titta på från sökhistoriken")
        print("3. Rensa all sökhistorik")
        print("4. Backa till huvudmenyn")
        choice = input("Ange ditt val (1-4): ")


Api_search(Movie_Searched=input("Ange film att söka efter: "))