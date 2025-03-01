# main.py

import src.mode as mode

def run(mode_choice):
    if mode_choice == "analyse":
        mode.analyze_mode()
    elif mode_choice == "validation":
        mode.validation_mode()
    elif mode_choice == "programmation":
        mode.programming_mode()
    elif mode_choice == "debug":
        mode.debug_mode()
    else:
        print("Mode inconnu. Veuillez réessayer.")

if __name__ == "__main__":
    run("analyse")
