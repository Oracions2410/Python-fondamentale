# Listes
from statistics import mean
from random import shuffle

def main():
    online_players = ["Oracions", "Vincen", "Louis", "Noel", "Marie"]
    print(online_players[len(online_players) - 1])

    online_players[2] = "Louis-Mary"
    print(online_players)

    #online_players[3:4] = ["Black Dexter", "Anne Marie"]

    #print(online_players[0:1])

    online_players.append("Gameur123")

    online_players.extend(["Martin", "Josée"])

    del online_players[1]
    online_players.pop(0)
    online_players.remove("Noel")

    # Suppréssion de la liste
    #del online_players[:]
    online_players.clear()

    print(online_players)


    # Calcul de la moyenne
    notes = [
        12, 2, 11,
        15, 8, 7,
        15, 20, 13,
    ]

    print(notes)
    shuffle(notes)
    print(notes)


    resultat = mean(notes)
    print("La moyenne de l'élève est {}".format(resultat))

    text = input("Entrer un text de la forme (email-pseudo-motdepasse) ").split("-")
    print("Salut  {}, ton email: {} et ton mot de passe: {}".format(text[1], text[0], text[2]))


if __name__ == '__main__':
    main()