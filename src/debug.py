from tkinter import *

def start_interface():
    mainWindow = Tk()

    label = Label (mainWindow, text ="Debug window for testing new features",width = 50,bg = "white")
    label.pack()


    # entrée
    value = StringVar() 
    value.set("texte par défaut")
    entree = Entry(mainWindow, textvariable="value : ", width=30)
    entree.pack()

    # bouton de validation de donnée
    boutonSend=Button(mainWindow, text="Send", command=mainWindow.update)
    boutonSend.pack()

    value = DoubleVar()
    scale = Scale(mainWindow, variable=value)
    scale.pack()

    # liste
    liste = Listbox(mainWindow)
    liste.insert(1, "Python")
    liste.insert(2, "PHP")
    liste.insert(3, "jQuery")
    liste.insert(4, "CSS")
    liste.insert(5, "Javascript")
    liste.pack()

    # checkbutton
    bouton = Checkbutton(mainWindow, text="Nouveau?")
    bouton.pack()

    # bouton de sortie
    boutonOutput=Button(mainWindow, text="Fermer", command=mainWindow.quit)
    boutonOutput.pack()

    mainWindow.mainloop()