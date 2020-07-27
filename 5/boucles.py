# Les boucles

def main():
    for num_client in range(1, 5):
        print("Vous etes le client N° ", num_client)

    # Envoie d'email
    emails = ["Oracions2410@gmail.com", "Superhidogawya@mail.com", "Oracions.dev@gmail.com", "Pdfyggtorrent@gmail.com"]
    blacklist = ["Oracions2410@gmail.com", "Pdfyggtorrent@gmail.com"]
    for email in emails:
        if email in blacklist:
            print("Envoie interdit! Email non envoyé")
            continue

        print("Email envoyé à ", email)

    # Boucle while
    salary = 2000
    while salary < 10000:
        salary += 120
        print(salary)


if __name__ == '__main__':
    main()
