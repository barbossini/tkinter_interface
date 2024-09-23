# configuration.py

import json

CONFIG_FILE = "settings.json"

# Exemple de configurations par défaut pour différents clients, versions et types de produit
DEFAULT_CONFIGURATIONS = {
    "client_1": {
        "version": "1.0",
        "type_produit": "standard",
        "paramètres": {
            "vitesse_actuateur": 100,
            "mode_test": "banc de test"
        }
    },
    "client_2": {
        "version": "1.5",
        "type_produit": "premium",
        "paramètres": {
            "vitesse_actuateur": 150,
            "mode_test": "condition réelle"
        }
    },
    "client_3": {
        "version": "2.0",
        "type_produit": "économie",
        "paramètres": {
            "vitesse_actuateur": 80,
            "mode_test": "bati de test"
        }
    }
}

def load_config():
    """Charge la configuration depuis un fichier JSON."""
    try:
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return DEFAULT_CONFIGURATIONS  # Retourne la configuration par défaut si le fichier n'existe pas

def save_config(config):
    """Sauvegarde la configuration dans un fichier JSON."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump(config, file, indent=4)

def update_config(client, version, type_produit):
    """Met à jour la configuration en fonction des caractéristiques choisies."""
    if client in DEFAULT_CONFIGURATIONS:
        config = DEFAULT_CONFIGURATIONS[client]
        if config["version"] == version and config["type_produit"] == type_produit:
            save_config(config["paramètres"])
            return config["paramètres"]
    raise ValueError("Configuration non trouvée pour le client, version ou type de produit spécifiés.")

def list_available_configurations():
    """Liste les configurations disponibles."""
    return DEFAULT_CONFIGURATIONS.keys()

if __name__ == "__main__":
    # Exemple d'utilisation
    available_clients = list_available_configurations()
    print("Clients disponibles :", available_clients)
