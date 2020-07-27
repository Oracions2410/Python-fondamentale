class Weapon:
    def __init__(self, name, damege):
        self.name = name
        self.damege = damege

    def get_damege(self):
        return self.damege

    def get_name(self):
        return self.name