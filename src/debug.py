import tkinter as tk

def start_interface():
    # Fonction appelée lorsque le bouton est cliqué
    def transfer_value():
        # Récupère le texte dans la première Entry
        value = entry1.get()
        
        # Insère cette valeur dans la deuxième Entry
        entry2.delete(0, tk.END)  # Supprime le texte précédent
        entry2.insert(0, value)   # Ajoute la nouvelle valeur

    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("Exemple avec Frames")

    # Création de la première frame
    frame1 = tk.Frame(root, padx=10, pady=10)
    frame1.pack(padx=10, pady=10)

    # Ajout d'une première Entry pour entrer un chiffre
    entry1 = tk.Entry(frame1, width=20)
    entry1.pack(side=tk.LEFT, padx=5)

    # Ajout d'un bouton pour envoyer la valeur dans la deuxième box
    button = tk.Button(frame1, text="Send", command=transfer_value)
    button.pack(side=tk.LEFT, padx=5)

    # Création de la deuxième frame
    frame2 = tk.Frame(root, padx=10, pady=10)
    frame2.pack(padx=10, pady=10)

    # Ajout d'une deuxième Entry pour afficher la valeur transférée
    entry2 = tk.Entry(frame2, width=20)
    entry2.pack(side=tk.LEFT, padx=5)

    # Lancement de la boucle principale
    root.mainloop()
