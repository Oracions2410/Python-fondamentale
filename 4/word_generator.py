# Générateur de mots
from random import shuffle

def main():
    words = input("Entrer une phrase de la forme (mot1/mot2/mot3/mot4)").split("/")
    shuffle(words)

    words_len = len(words)

    print(words)

    if words_len < 5:
        print(words[0:2])
    else:
        print(words[words_len - 3:words_len - 2:words_len - 1])


if __name__ == '__main__':
    main()