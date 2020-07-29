# Heritage
from player import Player

class Warrior(Player):
    def __init__(self, pseudo, health, attack):
        super().__init__(pseudo, health, attack)
        self.amor = 3


    def damage(self, damage):
        if self.amor > 0:
            self.amor -= 1
            damage = 0
        super().damege(damage)

    def blade(self):
        self.amor = 3
        print("Les points d'armures ont été rechargé")



print("Portez ce whisky au vieux juge blond qui fume !")
if issubclass(Warrior, Player):
    print("Le guérrier est bien une spécification de Player")

player3 = Warrior("MonkeyD", 100, 100)
player3.damage(4)
player3.damage(4)
player3.damage(4)
player3.damage(4)
print(player3.get_health())