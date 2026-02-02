import requests
import random
import os
import msvcrt as m
import json
import JsonAndCSV
import csv
import Modules
import webbrowser




# API_Response_Pic = 'http://img.omdbapi.com/?apikey=1951513b'
# print(API_Response)
# Pic_response = requests.get(API_Response_Pic)
# API_Picture = Pic_response.json()

#--------------------------------------------------------------------------------------
#Api_search(Movie_Searched=input("Vad vill du söka efter?")) är anropet för att söka i API:et
# -------- Method to search for specific movie by name from the API--------------------
def Api_search(Movie_Searched):
    with open('API_Key.txt', 'r') as api_file:
        api_key = api_file.read().strip()
    API_Response = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&s={Movie_Searched}')
    API_Data = API_Response.json()
    with open('ApiResponse.json', 'w', encoding='utf-8') as fpoiner:
        workingdata = json.dumps(API_Data)
        fpoiner.write(workingdata)
        print(workingdata)
    
#--------------------------------------------------------------------------------------
# -------- Method to search for specific movie by name --------------------------------
def Movie_Search():
    with open ('json_file', 'r', encoding='utf-8',) as json_file_pointer:
        Movie_Searched = []
        Movies_Data = json.load(json_file_pointer)
        Movie_Searched = input("Ange film att söka efter: ")
        Search_Results = []
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
# -------- Menu for search history--------------------------------
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


#Movie_Search()