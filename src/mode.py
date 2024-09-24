# mode.py

import src.analyze as analyze
import src.configuration as configuration
import src.debug as debug
def analyze_mode():
    analyze.start_analysis()

def validation_mode():
    pass

def programming_mode():
    # Charger des configurations depuis configuration.py et lancer la programmation
    pass

def debug_mode():
    debug.start_interface()