import random
import os
import msvcrt as m

clear = lambda: os.system('cls')
  
def wait_for_keypress():
    print("Tryck på valfri knapp för att fortsätta...")
    m.getch()

List_Of_Movies = [ ## gör en lista med dictionaries för varje film
    {"Genre": "Sci-Fi", "Titel": "The Matrix", "Beskrivning": "En hacker upptäcker att verkligheten är en simulering skapad av maskiner."},
    {"Genre": "Sci-Fi", "Titel": "Inception", "Beskrivning": "En mästare i drömmar som försöker införa en idé i någon annans dröm."},
    {"Genre": "Crime", "Titel": "The Godfather", "Beskrivning": "En familj som kontrollerar en kriminell organisation i New York."},
    {"Genre": "Crime", "Titel": "Pulp Fiction", "Beskrivning": "En mästare i drömmar som försöker införa en idé i någon annans dröm."},
    {"Genre": "Drama", "Titel": "The Shawshank Redemption", "Beskrivning": "Två fångar bildar en oväntad vänskap under deras tid i Shawshank-fängelset."},
    {"Genre": "Drama", "Titel": "Forrest Gump", "Beskrivning": "En man upplever och påverkar flera historiska händelser i USA."}
]
#Genre index 0, Titel index 1, Beskrivning index 2


def MovieBasedOnGenre():
    print("Välj en Genre för att få en filmrekommendation:")
    print("Tillgängliga genrer är: Sci-Fi, Crime, Drama")
    genre = input("Ange en genre: ")
    genre.title()
    Amount_Of_Movies_In_Genre = 0
    Temporary_List = []
    Temporary_List.clear()
    for EachGenre in List_Of_Movies: # loopa igenom varje dictionary i listan för att hitta alla relaterade genrer
        if EachGenre["Genre"] == genre: # för varje genre som matchar den valda genren, lägg till den i en temporär lista
            Amount_Of_Movies_In_Genre += 1
            Temporary_List.append(EachGenre)
    clear()
    if Amount_Of_Movies_In_Genre == 0:
        print("Ingen film hittades inom den valda genren.")
        return
        
    Rekomended_Movie = random.randint(0, Amount_Of_Movies_In_Genre - 1)
    print(f"Rekommenderad film inom genren {genre}:")
    print(f"Titel: {Temporary_List[Rekomended_Movie]['Titel']}")
    print(f"Beskrivning: {Temporary_List[Rekomended_Movie]['Beskrivning']}\n")
    wait_for_keypress()
    clear()

def MovieGeneration_Guess():
    TempList_Guess = []
    TempList_Guess.clear()
    TempList_Guess = [random.choice(List_Of_Movies)] 
    print(f"Gissa utifrån detta: ", TempList_Guess[0]['Beskrivning'])
    if input("Vad är din gissning?") == TempList_Guess[0]['Titel']:
        print("Rätt gissat!\n")
    else:
        print(f"Fel gissat! Rätt svar är: {TempList_Guess[0]['Titel']}\n")
    wait_for_keypress()
    clear()
def PrintAllMovies():
    for movie in List_Of_Movies:
        print(f"Titel: {movie['Titel']}")
    print("")
    wait_for_keypress()
    clear()
