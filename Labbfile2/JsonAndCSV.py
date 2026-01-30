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

def save_movies_to_json():
    Dict_Movies = []
    with open(csv_file, 'r', encoding='utf-8') as csv_file_pointer:
        csv_reader = csv.DictReader(csv_file_pointer, delimiter=';')
        for movies in csv_reader:
            Dict_Movies.append(movies)
    
    # Store in the class instance
    movies_container.set_movies(Dict_Movies)
    
    with open("json_file", 'w', encoding='utf-8') as json_file_pointer:
        json.dump(Dict_Movies, json_file_pointer, ensure_ascii=False, indent=4)

def print_movies_list():
    save_movies_to_json()
    for movie in movies_container.get_movies():
        print(movie)

save_movies_to_json()