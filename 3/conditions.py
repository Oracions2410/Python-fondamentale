# Les Conditions

def main():
    # Variables
    wallet = 5000
    computer_price = 1000

    if wallet >= computer_price:
        print("L'achat est possible")
        wallet -= computer_price
    else:
        print("L'achat n'est pas possible, vous n'avez que {}€".format(wallet))

    print(wallet)

    # Conditions ternaires
    temperature = 30
    #print(temperature <= 37)
    message = ('Il fait froid', 'Il fait chaud')[temperature <= 37]
    print(message)


if __name__ == '__main__':
    main()