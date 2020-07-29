# Simulateur de ville

class Batiment:
    def __init__(self, name, address, nb_etage):
        self.name = name
        self.address = address
        self.nb_etage = nb_etage
        print("Création d'un nouveau batiment")

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_nb_etage(self):
        return self.nb_etage

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_nb_etage(self, nb_etage):
        self.nb_etage = nb_etage


class Immeuble(Batiment):
    def __init__(self, name, address, nb_etage, nb_balcon):
        super().__init__(name, address, nb_etage)
        self.nb_balcon = nb_balcon
        print("Spécialisation: Immeuble")

    def get_nb_balcon(self):
        return self.nb_balcon

    def set_nb_balcon(self, nb_balcon):
        self.nb_balcon = nb_balcon

class Bank(Batiment):
    def __init__(self, name, address, nb_etage, nb_coffres):
        super().__init__(name, address, nb_etage)
        self.nb_coffres = nb_coffres
        print("Spécialisation: Bank")

    def get_nb_coffres(self):
        return self.nb_coffres

    def set_nb_coffres(self, nb_coffres):
        self.nb_coffres = nb_coffres


class Market(Batiment):
    def __init__(self, name, address, nb_rayon):
        super().__init__(name, address, 0)
        self.nb_rayon = nb_rayon
        print("Spécialisation: Supermarché")


    def get_nb_rayon(self):
        return self.nb_rayon

    def set_nb_rayon(self, nb_rayon):
        self.nb_rayon = nb_rayon


immeuble1 = Immeuble("FECOM", "Yaoundé - Elig Edjoua", 3, 8)
immeuble2 = Immeuble("La Régionale", "Yaoundé - rond point LongKak", 4, 4)
immeuble3 = Immeuble("Hilon", "Yaoundé - poste centrale", 13, 34)

bank1 = Bank("UBA", "Yaoundé - hypodrome", 0, 0)
bank2 = Bank("Ora", "Douala - Ange Raphael", 34, 65)

market1 = Market("Mokolo", "Yaoundé - Mokolo", 234)