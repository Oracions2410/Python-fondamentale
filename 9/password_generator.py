# Générateur de mots de passes

import string
from tkinter import *
from random import randint, choice

def generate_password():
    min = 6
    max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(min, max)))
    input_text.delete(0, END)
    input_text.insert(0, password)

window = Tk()
window.title("GÉNÉRATEUR DE MOT DE PASSE")
window.geometry("720x280")
#window.minsize(720, 480)
window.config(background="#41B77F")
window.iconbitmap("@logo1.xbm")

frame = Frame(window, bg="#41B77F")

# Création du canvas pour le dessin
width = 300
height = 300
image = PhotoImage(file="tenor.gif").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg="#41B77F", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# Création d'un panel pour le formulaire
right_frame = Frame(frame, bg="#41B77F")

# Ajout du titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg="#41B77F", fg="#FFF")
label_title.pack(expand=YES)

input_text = Entry(right_frame, font=("Verdana", 14), bg="#FFF", fg="#41B77F")
input_text.pack(pady=14)

button_generate = Button(right_frame, text="Générer le mot de passe", bg="#FFF", fg="#41B77F", command=generate_password)
button_generate.pack(fill=X)

right_frame.grid(row=0, column=2, sticky=W)

frame.pack(expand=YES)

# Création d'une barre de menu
menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Qutter", command=window.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)


# Affichage
window.mainloop()