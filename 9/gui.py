# Interface graphique
from tkinter import *
import webbrowser

def open_covid19_page():
    webbrowser.open_new("https://covid19-ora.netlify.com")

window = Tk()

window.title("My Application")
window.geometry("720x480")
window.minsize(300, 150)
#window.maxsize(800, 600)

window.iconbitmap("@logo.xbm")
window.config(background="#007bff")

# Création d'une frame
#frame = Frame(window, bg='#007bff', bd=1, relief=SUNKEN)
frame = Frame(window, bg="#007bff")

# Ajout d'un label
label_title = Label(frame, text="Bienvenue dans l'application", font=("Helvetica", 30), bg="#007bff", fg="#FFF")

#label_title.pack(side=BOTTOM)
label_title.pack()
#window.minsize(400, 200)

# Ajout d'un autre text
label_subtitle = Label(frame, text="Hey, Salut comment allez vous ?", font=("Verdana", 15), bg="#007bff", fg="#FFF")
label_subtitle.pack()

# Ajout d'un bouton
covid19_button = Button(frame, text="Covid19", font=("Arial Black", 25), bg="#FFF", fg="#007bff", command=open_covid19_page)
covid19_button.pack(pady=32, fill=X)

frame.pack(expand=YES)

# Affichage
window.mainloop()
