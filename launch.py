# launch.py

import src.main as main

if __name__ == "__main__":
    print("Choisissez un mode de fonctionnement:")
    print("1 - Analyse Fonctionnelle")
    print("2 - Validation & Qualification")
    print("3 - Programmation")
    
    choice = input("Entrez le numéro du mode choisi : ")

    if choice == '1':
        main.run("analyse")
    elif choice == '2':
        main.run("validation")
    elif choice == '3':
        main.run("programmation")
    else:
        print("Choix invalide, veuillez réessayer.")
