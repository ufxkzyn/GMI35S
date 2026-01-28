import random
import os
import csv
import json


with open("movies_labb2.csv",'r',encoding='utf-8', newline='') as csv_read_pointer:
    csv_reader = csv.reader(csv_read_pointer)
    for movie in csv_reader:
        print(csv_reader)