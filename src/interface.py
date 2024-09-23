# interface.py

import tkinter as tk

def display_message(message):
    window = tk.Tk()
    label = tk.Label(window, text=message)
    label.pack()
    window.mainloop()

def display_graph(data):
    # Utilisation de matplotlib ou autre pour afficher des graphiques
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.show()

def ask_user_input(options):
    window = tk.Tk()
    var = tk.StringVar(window)
    var.set(options[0])  # Option par défaut

    dropdown = tk.OptionMenu(window, var, *options)
    dropdown.pack()

    def submit_choice():
        window.quit()
        window.destroy()

    button = tk.Button(window, text="Confirmer", command=submit_choice)
    button.pack()

    window.mainloop()
    return var.get()
