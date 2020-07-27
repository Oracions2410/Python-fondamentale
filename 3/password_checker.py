# Vérification de mot de passe

def main():
    password = input("Entrer un mot de passe: ")
    password_length = len(password)

    if password_length < 8:
        print("Mot de passe trop court.")
    elif 8 <= password_length <= 12:
        print('Mot de passe moyen.')
    else:
        print("Mot de passe trop long.")


if __name__ == '__main__':
    main()
