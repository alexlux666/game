class Human:
    """Base class for characters"""
    def __init__(self, name, hp, damage, enemy):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.enemy = enemy

    def __str__(self):
        return f"Name - {self.name}\nHP - {self.hp}\nPower - {self.damage}"

    def get_damage(self):
        """Return the damage value"""
        return self.damage

    def take_damage(self, value):
        """Reduce HP by damage value"""
        self.hp -= value
        return self.hp

class Thief(Human):
    """Thief character class"""

    def attack(self, enemy):
        enemy.take_damage(self.damage)
        print(f"{self.name} uses quick strike!")

    def take_damage(self, value):
        super().take_damage(value)
        print(f"{self.name} counter-attacks! HP = {self.hp}")
        
class Hero(Human):
    """Hero character class with unique ability"""
    def __init__(self, uniq, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uniq = uniq

    def attack(self, enemy):
        enemy.take_damage(self.damage)
        print(f"{self.name} uses powerful ability!")

    def take_damage(self, value):
        super().take_damage(value)
        print(f"{self.name} defends! HP = {self.hp}")

class Dragon(Human):

    def attack(self, enemy):
        enemy.take_damage(self.damage)
        print(f"{self.name} GHAAAA🐲")

    def take_damage(self, value):
        super().take_damage(value)
        print(f"{self.name} defends! HP = {self.hp}")

def main():
    """Main game loop"""
    dragon = Dragon(name="Dragon", hp=500, damage=50, enemy=None)
    thief = Thief(name="Горчун", hp=100, damage=10, enemy=None)
    print(thief)
    print()

    hero = Hero(uniq="Благословление(+5)", name="Валера", hp=105, damage=15, enemy=None)
    print(hero)
    print(f"Unique ability - {hero.uniq}")
    print()

    hero.attack(thief)
    print()

    thief.attack(hero)
    print()

    dragon.attack(hero)
    dragon.attack(thief)

    while True:
        thief.attack(dragon)
        print()
        hero.attack(dragon)
        print()
        if dragon.hp < 0:
            print("YOU WIN!🏆")
            break
if __name__ == "__main__":
    main()