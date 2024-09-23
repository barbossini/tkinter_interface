# Système de Gestion et Validation de Systèmes Complexes

Ce projet propose une interface graphique permettant de choisir entre plusieurs modes de fonctionnement pour l'analyse, la validation, et la programmation d'un système complexe. Chaque mode offre des fonctionnalités spécifiques, allant de la simulation d'éléments physiques à l'exécution de scénarios de test automatisés, en passant par la mise à jour et la gestion des paramètres du système.

## Modes de Fonctionnement

### 1. **Mode Analyse Fonctionnelle**
Ce mode est dédié à l'examen du système en temps réel, permettant la simulation d'éléments physiques et l'affichage de données critiques.

#### Fonctionnalités :
- **Simulation de périphériques physiques** : Permet de simuler des éléments comme des joysticks, des télécommandes, des capteurs ou des LEDs pour tester le système sans utiliser de matériel réel.
- **Surveillance de l’état du système** : Affichage en temps réel de l'état des capteurs et des actuateurs, avec acquisition de données sous forme graphique (par exemple, température, tension, vitesse).
- **Affichage de graphiques en temps réel** : Afficher les données en temps réel, telles que les valeurs des capteurs ou des variables systèmes, pour surveiller leur évolution pendant un test.
- **Messages d’erreur spécifiques** : Les erreurs liées à des dysfonctionnements sont capturées et affichées clairement, avec des instructions pour la résolution des problèmes.
- **Simulation de conditions spécifiques** : Permet de choisir les conditions de test (banc de test, bâti de test, conditions réelles) et de simuler des environnements pour voir la réaction du système.

### 2. **Mode Validation & Qualification**
Le mode Validation & Qualification exécute des scénarios de tests automatisés pour valider l’interface utilisateur ainsi que les composants du système.

#### Fonctionnalités :
- **Exécution de scénarios automatisés** : Permet de lancer des suites de scénarios de validation prédéfinis pour tester l'interface et les interactions du système en conditions réelles ou simulées.
- **Affichage de graphiques et acquisition de données** : Les données collectées pendant les tests (par ex. capteurs, actuateurs) sont visualisées sous forme de graphiques pour suivre leur évolution.
- **Sélection du matériel et des conditions de test** : L'utilisateur peut sélectionner le matériel à tester et choisir les conditions de test appropriées (banc de test, bâti de test, conditions réelles).
- **Génération automatique de rapports** : À la fin de chaque test ou scénario, un rapport complet est généré, contenant des données sur les performances du système, des graphiques et des messages d'erreurs.
- **Messages d’erreur spécifiques** : Si un scénario échoue, des messages d'erreur clairs et détaillés sont affichés pour permettre une résolution rapide des problèmes.

### 3. **Mode Programmation**
Le mode Programmation permet de configurer et de mettre à jour les paramètres du système en temps réel, avec la possibilité de sauvegarder et de restaurer des configurations spécifiques.

#### Fonctionnalités :
- **Mise à jour des paramètres système** : Permet de modifier et de programmer les paramètres système (calibration des capteurs, vitesse des actuateurs, etc.) via une interface graphique.
- **Sauvegarde et chargement de configurations** : Les utilisateurs peuvent sauvegarder des configurations système sous différents formats (JSON, XML, CSV) et les restaurer facilement pour différents scénarios d'utilisation.
- **Sélection du matériel à programmer** : Permet de sélectionner le matériel à configurer (capteurs, actuateurs, etc.) et de spécifier les conditions de test (banc de test, bâti de test, conditions réelles).
- **Génération de rapports sur les modifications** : Après chaque session de programmation, un rapport résume les modifications effectuées sur les paramètres, y compris les configurations mises à jour et les erreurs potentielles.
- **Messages d’erreur spécifiques** : Si la programmation échoue ou si des paramètres sont incorrects, un message d'erreur clair est affiché, expliquant le problème.

## Fonctionnalités Générales :
- **Affichage des graphiques en temps réel ou post-test** : Les graphiques permettent de suivre les variables système pendant l'exécution des tests ou d'analyser les résultats après coup.
- **Génération de rapports automatiques** : Les rapports sont générés à la fin des tests ou selon les besoins de l'utilisateur, facilitant la traçabilité et la validation des résultats.
- **Sélection des conditions de test** : Possibilité de choisir entre diverses conditions pour valider le matériel ou le système (banc de test, conditions réelles, bâti de test).
- **Messages d’erreur spécifiques et gestion des logs** : Tout au long des tests et des opérations, les erreurs sont loguées et des messages d’erreurs détaillés sont fournis pour faciliter le débogage et la maintenance.

## Structure des Fichiers
- **`launch.py`** : Point d'entrée principal de l'application, permettant de sélectionner le mode de fonctionnement (Analyse Fonctionnelle, Validation & Qualification, Programmation) via une interface graphique simple.
- **`main.py`** : Contient la logique principale de chaque mode et s'exécute avec les paramètres sélectionnés.

## Installation
Pour installer et exécuter ce projet, suivez ces étapes :

1. Clonez le projet :
    ```bash
    git clone 
    cd 
    ```

2. Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

3. Exécutez le fichier `launch.py` pour choisir le mode de fonctionnement :
    ```bash
    python launch.py
    ```

## Utilisation
- **Mode Analyse Fonctionnelle** : Permet d’examiner et de simuler le comportement du système en temps réel via une interface graphique.
- **Mode Validation & Qualification** : Utilisé pour exécuter des scénarios de tests automatisés, valider l’interface et générer des rapports de validation du système.
- **Mode Programmation** : Permet de modifier et de sauvegarder des configurations système, avec une gestion agile des paramètres et la génération de rapports après chaque session.

## Contribuer
Pour contribuer à ce projet, veuillez soumettre des pull requests ou signaler des problèmes dans la section des issues.

## Licence
Ce projet est sous licence COMROD FRANCE.

