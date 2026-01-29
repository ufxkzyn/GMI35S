import random
import Modules
import os
import csv
import json

clear = lambda: os.system('cls')
csv_file = "movies_labb2.csv"

class jsonfile_handling:
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
        jsonfile_handling.save_movies_to_json()
        for movie in jsonfile_handling.Dict_Movies:
            print(jsonfile_handling.Dict_Movies[movie])





jsonfile_handling.save_movies_to_json()
#print_movies_list()
#print(load_movies_from_csv)
#jsonfile_handling.print_movies_list()

#printlist = jsonfile_handling
#jsonfile_handling.print_movies_list()
x = 5