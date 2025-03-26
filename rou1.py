import random
import tkinter as tk

prenoms = {
    "Ismael": 20, "Lavrin": 80, "Sean": 30, "Lou": 20, "Sarah": 20,
    "Mohamed": 20, "Tom": 40, "Younes": 10, "Lina": 20, "Mathis": 20,
    "Leo": 20, "Mathias": 30, "Idriss": 20, "Amir": 20, "Yoann": 10,
    "Ewan": 10, "Sakina": 30, "Sairam": 30, "Steven": 15, "Ruben": 10,
    "Guillaume": 15, "Dorian": 30, "Corentin": 25
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
