import random
import tkinter as tk

prenoms = {
    "Ismael": 20, "Lavrin": 25, "Sean": 25, "Lou": 20, "Sarah": 25,
    "Mohamed": 20, "Tom": 25, "Younes": 15, "Lina": 20, "Mathis": 20,
    "Leo": 20, "Mathias": 20, "Idriss": 20, "Amir": 20, "Yoann": 15,
    "Ewan": 15, "Sakina": 25, "Sairam": 20, "Steven": 15, "Ruben": 15,
    "Guillaume": 15, "Dorian": 25, "Corentin": 20
}

t = []
for prenom, pourcentage in prenoms.items():
    t += [prenom] * pourcentage

random.shuffle(t)

def afficher_prenom():
    prenom = random.choice(t) 
    label.config(text=f"Le prénom choisi est : {prenom}")

root = tk.Tk()
root.title("Choix de Prénom")

button = tk.Button(root, text="Choisir un prénom", command=afficher_prenom, font=("Arial", 14))
button.pack(pady=20)

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20)

root.mainloop()

