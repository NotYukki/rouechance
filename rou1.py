import random
import tkinter as tk

prenoms = {
    "Ismael": 20, "Lavrin": 25, "Sean": 25, "Lou": 20, "Sarah": 25,
    "Mohamed": 20, "Tom": 25, "Younes": 15, "Lina": 20, "Mathis": 20,
    "Leo": 20, "Mathias": 20, "Idriss": 20, "Amir": 20, "Yoann": 15,
    "Ewan": 15, "Sakina": 25, "Sairam": 20, "Steven": 15, "Ruben": 15,
    "Guillaume": 15, "Dorian": 25, "Corentin": 20
}

def choisir_prenom():
    noms = list(prenoms.keys())
    poids = list(prenoms.values())
    return random.choices(noms, weights=poids, k=1)[0]

def retourner_carte():
    bouton.config(state="disabled", text="✨ Tirage...")
    carte_label.config(text="", fg="white")
    animer_rotation(1.0, shrink=True)

def animer_rotation(scale, shrink):
    if shrink and scale > 0:
        carte.scale("all", 0, 0, 0.9, 1.0)  # simulation de zoom X
        carte.update()
        root.after(20, animer_rotation, scale - 0.1, True)
    elif shrink:
        prenom = choisir_prenom()
        carte_label.config(text=prenom, fg="#1a1a1a")
        carte.config(bg="#f0f8ff")
        glow()
        animer_rotation(0.1, False)
    elif not shrink and scale < 1:
        carte.scale("all", 0, 0, 1.1, 1.0)
        carte.update()
        root.after(20, animer_rotation, scale + 0.1, False)
    else:
        bouton.config(state="normal", text="🔁 Tirer un prénom")

def glow(step=0):
    # animation légère de glow
    couleurs = ["#f0f8ff", "#e0f0ff", "#d0ecff", "#e0f0ff", "#f0f8ff"]
    if step < len(couleurs):
        carte.config(bg=couleurs[step])
        root.after(60, glow, step + 1)

# --- GUI SETUP ---

root = tk.Tk()
root.title("✨ Tirage Stylé de Prénom")
root.geometry("420x320")
root.configure(bg="#1e1e2f")

titre = tk.Label(root, text="🎴 Prénom Mystère", font=("Helvetica", 24, "bold"), bg="#1e1e2f", fg="white")
titre.pack(pady=20)

# Carte visuelle
carte = tk.Canvas(root, width=200, height=100, bg="white", highlightthickness=0)
carte.pack(pady=20)

carte_label = tk.Label(root, text="❓", font=("Helvetica", 28, "bold"), bg="white", fg="#333")
carte.create_window(100, 50, window=carte_label)

# Bouton principal
bouton = tk.Button(
    root,
    text="🔮 Tirer un prénom",
    command=retourner_carte,
    font=("Helvetica", 14, "bold"),
    bg="#00adb5",
    fg="white",
    activebackground="#007b7f",
    relief="flat",
    padx=20,
    pady=10
)
bouton.pack(pady=10)

root.mainloop()
