# Achat des place du cinéma

def main():
    # Age de l'utilisateur
    age = int(input("Entrer votre age: "))
    ticket_price = 0

    # Vérification de l'age
    if age < 18:
        print("Le tichet va vous couter 7€")
        ticket_price = 7
    else:
        print("Le tichet va vous couter 12€")
        ticket_price = 12

    response = input("Voulez-vous du pop (O/N) ? ")


    if response.lower() == 'o' or response.lower() == 'oui':
        ticket_price += 5
    elif response.lower() == 'n' or response.lower() == 'non':
        print("Pas de pop corn")
    else:
        print("Response invalid")

    print("Cela vous coûtera {}€".format(ticket_price))


if __name__ == '__main__':
    main()
    #print('Porte CE WHISKY'.lower())