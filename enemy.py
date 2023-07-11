import random
class zombie:
    
    def __init__(self, health, armor, attack, damage):
        self.health = health
        self.armor = armor
        self.attack = attack
        self.damage = damage
    
    def take_damage(self, damage):
        self.health -= damage

    def give_damage(self):
        return self.damage

    def accuracy(self, player_armor):
        hit = self.attack + random.randint(0,100)
        if hit / 2 >= player_armor:
            return True
        else:
            return False
