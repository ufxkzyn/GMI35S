import random
import Modules
import os
import csv
import json

clear = lambda: os.system('cls')
csv_file = "movies_labb2.csv"


Dict_Movies = []
def save_movies_to_json():
    Dict_Movies = []
    with open(csv_file, 'r', encoding='utf-8',) as csv_file_pointer: #opening the csv file with read permissions and utf-8 encoding
        csv_reader = csv.DictReader(csv_file_pointer, delimiter=';')
        for movies in csv_reader:
            Dict_Movies.append(movies)

    with open ("json_file", 'w', encoding='utf-8',) as json_file_pointer: # quatation marks around all settings so they arent confused with parameters
        json.dump(Dict_Movies, json_file_pointer, ensure_ascii=False, indent=4)

def print_movies_list():
    save_movies_to_json()
    for movie in Dict_Movies:
        print(Dict_Movies[movie])


def Search_movies():
    with open('json_file', 'r', encoding = 'utf-8', ) as json_file_pointer:
        Search_movies = json.load(json_file_pointer)
        print('Sök efter genres tillgängliga:')
        for movie in json.load(json_file_pointer):
            print(movie['genre'])
    input('Ange genre du vill söka efter:')
    
save_movies_to_json()
x = 5