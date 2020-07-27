
from models.player import Player
from models.weapon import Weapon

player1 = Player("Oracions", 100, 4)
#player1.attack = 143
#print(player1.attack)
#player1.damege(3)
#print(player1.health)

# Combat
player2 = Player("MonkeyD", 100, 2)
couteau = Weapon("Couteau", 10)
player2.set_weapon(couteau)

print(player1.get_pseudo(), " / Points de vie ", player1.get_health(), "/ attack ", player1.get_attack())
print(player2.get_pseudo(), " / Points de vie ", player2.get_health(), "/ attack ", player2.get_attack())

player1.attack_player(player2)
print(player1.get_pseudo(), " attaque ", player2.get_pseudo())

print(player1.get_pseudo(), " / Points de vie ", player1.get_health())
print(player2.get_pseudo(), " / Points de vie ", player2.get_health())

player2.attack_player(player1)
print(player2.get_pseudo(), " attaque ", player1.get_pseudo())

print(player1.get_pseudo(), " / Points de vie ", player1.get_health())
print(player2.get_pseudo(), " / Points de vie ", player2.get_health())