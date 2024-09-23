# main.py

import mode

def run(mode_choice):
    if mode_choice == "analyse":
        mode.analyze_mode()
    elif mode_choice == "validation":
        mode.validation_mode()
    elif mode_choice == "programmation":
        mode.programming_mode()
    else:
        print("Mode inconnu. Veuillez réessayer.")

if __name__ == "__main__":
    run("analyse")
