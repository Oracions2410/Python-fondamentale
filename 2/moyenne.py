# Calcul de la moyenne de trois notes

def main():
    # Saisie de la première note
    note1 = int(input("Entrez la première note "))
    note2 = int(input("Entrez la deuxième note "))
    note3 = int(input("Entrez la troixième note "))

    resultat = (note1 + note2 + note3) / 3

    print("La moyenne de l'élève est: ", str(resultat))

if __name__ == '__main__':
    main()