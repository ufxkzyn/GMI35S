import random
import Modules
import os
import csv
import json
import Class_file

clear = lambda: os.system('cls')
csv_file = "movies_labb2.csv"

# Create a single instance to share across modules
movies_container = Class_file.CustomDictOne()
#movies_container = []

def save_movies_to_json():
    List_Movies = []
    with open(csv_file, 'r', encoding='utf-8') as csv_file_pointer:
        csv_reader = csv.DictReader(csv_file_pointer, delimiter=';')
        for movies in csv_reader:
            List_Movies.append(movies)
    
    # Store in the class instance
    movies_container.set_movies(List_Movies)
    
    with open("json_file", 'w', encoding='utf-8') as json_file_pointer:
        json.dump(List_Movies, json_file_pointer, ensure_ascii=False, indent=4)
    print("Succsess")
    Modules.wait_for_keypress()
    clear()

def Save_Movies_to_CSV():
    movies = movies_container.get_movies()
    with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file_pointer:
        Headers = ['titel', 'genre', 'beskrivning']
        csv_writer = csv.DictWriter(csv_file_pointer, fieldnames=Headers, delimiter=';')
        csv_writer.writeheader()
        for movie in movies:
            csv_writer.writerow(movie)
        print("Succsess")
        Modules.wait_for_keypress()
        clear()
        
        
#unsed used method, 
def print_movies_list():
    save_movies_to_json()
    for movie in movies_container.get_movies():
        print(movie)


