# Pokemon Gen V1
import random


def welcome():
    print("""
    ⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
    WELCOME TO THE POKEDEX
    """)


def menu():
    menuChoice = input("""
    Please select a choice :
    1. Create a new Pokemon
    2. View current Pokemon in the pokedex
    3. Exit
    >>>""")
    if menuChoice == "1":
        createPokemon()
    elif menuChoice == "2":
        pass
    elif menuChoice == "3":
        pass
    else:
        print("Option not valid")


def createPokemon():
    name = input("Enter name: ")
    HP = random.randint(1, 100)
    DEFENCE = random.randint(1, 100)
    SPEED = random.randint(1, 100)
    SPEEDATTACK = random.randint(1, 100)
    SPEEDDEFENCE = random.randint(1, 100)
    print(f"HP {HP}")
    print(f"DEFENCE {DEFENCE}")
    print(f"SPEED {SPEED}")
    print(f"SPEEDATTACK {SPEEDATTACK}")
    print(f"SPEEDDEFENCE {SPEEDDEFENCE}")

    Types = ["Fire", "Water", "Ground", "Rock", "Poison", "Fairy", "Ice", "dragon", "flying", "Ghost", "Dark", "Bug"]
    randomType = random.choice(Types)
    print(f"{name}'s type is: {randomType}")

#Friday 05/12/2025
    pokeFile = open("pokemon.txt", "a")
    pokeFile.write(f"Name: {name}\n")
    pokeFile.write(f"HP: {HP}\n")
    pokeFile.write(f"DEFENCE: {DEFENCE}\n")
    pokeFile.write(f"SPEED: {SPEED}\n")
    pokeFile.write(f"SPEEDATTACK: {SPEEDATTACK}\n")
    pokeFile.write(f"SPEED DEFENCE: {SPEEDDEFENCE}\n")
    pokeFile.write(f"TYPE: {randomType}\n")
    pokeFile.close()





welcome()
menu()
