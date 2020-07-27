# Calcul le cout du produit et le somme restante après achat

def main():
    # Somme contenue dans le porte money
    somme = 154000
    print("Somme Initial: " + str(somme))

    # Prix du produit achté
    product_price = 52000
    print("Prix du produit: " + str(product_price))

    # Somme après achat
    somme_after_buy = somme - product_price
    print("Somme après achat: " + str(somme_after_buy))


if __name__ == '__main__':
    main()