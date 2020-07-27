

class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None
        print("Bienvenue au joueur ", pseudo, "/ Points de vie", health, "/ Attack: ", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
      return self.health

    def get_attack(self):
        return self.attack

    def get_weapon(self):
        return self.weapon

    def set_health(self, health):
        self.health = health

    def set_weapon(self, target_weapon):
        self.weapon = target_weapon

    def damege(self, damege):
        self.health -= damege
        if (self.health < 0):
            self.health = 0

    def attack_player(self, target_player):
        target_player.damege(self.attack)
        # si le Joueur a une arme, on ajoute les dégats causé par l'arme
        if self.weapon:
            print("####### ARME ({}) - puissance:`{}` ########".format(self.weapon.get_name(), self.weapon.get_damege()))
            target_player.damege(self.weapon.get_damege())
        else:
            print("------- MAIN NUES--------")


