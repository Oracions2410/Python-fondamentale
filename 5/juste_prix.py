# Jeu du juste prix
from random import randint

def main():

    price = randint(0, 10)
    price_input = int(input("Entrer un prix compris entre 0 et 10\n"))

    while price_input != price:
        if price_input < price:
            price_input = int(input("Trop petit ! Réssayer..\n"))
        elif price_input > price:
            print("Trop grand")
            price_input = int(input("Trop grand ! Réssayer..\n"))

    print("Bravo ! `{}` était le vrai prix".format(price))


if __name__ == '__main__':
    main()