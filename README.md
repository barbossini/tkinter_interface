# Structure du Projet
** /lib **
└── requirement.py # Gestion des dépendances et configurations de l'environnement

**/src**
├── analyze.py # Module d'analyse fonctionnelle 
├── configuration.py # Gestion des paramètres système et configurations 
├── interface.py # Interface graphique et interactions utilisateur 
├── main.py # Point d'entrée logique pour exécuter les différents modes 
├── mode.py # Gestion des différents modes (analyse, validation, programmation) 
├── peripherals.py # Gestion et simulation des périphériques physiques

**/test**
├── test_interface.py # Tests pour l'interface graphique 
├── test_system_validation.py # Tests pour la validation système 
└── test_system_qualification.py # Tests pour la qualification système

launch.py # Point d'entrée principal pour sélectionner le mode de fonctionnement settings.py # Paramètres globaux et configurations du projet

## Résumé

- **`/lib/requirement.py`** : Gestion des dépendances.
- **`/src/analyze.py`** : Mode Analyse Fonctionnelle.
- **`/src/configuration.py`** : Chargement et sauvegarde des paramètres.
- **`/src/interface.py`** : Interface graphique.
- **`/src/main.py`** : Gère l'exécution du programme.
- **`/src/mode.py`** : Gère les modes (analyse, validation, etc.).
- **`/src/peripherals.py`** : Simulation et gestion des périphériques.
- **`/test/`** : Tests unitaires pour l'interface, la validation, et la qualification.
- **`launch.py`** : Point d'entrée pour choisir le mode de fonctionnement.
- **`settings.py`** : Gestion des paramètres globaux.