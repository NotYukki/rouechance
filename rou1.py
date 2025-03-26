import random
import tkinter as tk

# Liste des prénoms et pourcentages
prenoms = {
    "Ismael": 20, "Lavrin": 25, "Sean": 25, "Lou": 20, "Sarah": 25,
    "Mohamed": 20, "Tom": 25, "Younes": 15, "Lina": 20, "Mathis": 20,
    "Leo": 20, "Mathias": 20, "Idriss": 20, "Amir": 20, "Yoann": 15,
    "Ewan": 15, "Sakina": 25, "Sairam": 20, "Steven": 15, "Ruben": 15,
    "Guillaume": 15, "Dorian": 25, "Corentin": 20
}

# Génération de la liste t avec les prénoms répétés selon les pourcentages
t = []
for prenom, pourcentage in prenoms.items():
    t += [prenom] * pourcentage

random.shuffle(t)

# Fonction pour afficher un prénom choisi au hasard
def afficher_prenom():
    prenom = random.choice(t)  # Choisit un prénom au hasard
    label.config(text=f"Le prénom choisi est : {prenom}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Choix de Prénom")

# Création du bouton et du label
button = tk.Button(root, text="Choisir un prénom", command=afficher_prenom, font=("Arial", 14))
button.pack(pady=20)

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=20)

# Lancer l'application
root.mainloop()

