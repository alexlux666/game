import random
class Item():
    """Item classs:sword or potion"""
    def __init__(self, name: str, kind: str, value: int):
        self.name = name
        self.kind = kind
        self.value = value
    def __str__(self) -> str:
        return f"🧪{self.name} {self.kind}, baff: {self.value}"

class Human():
    """Base class for all chapter (Logic for all:thief , hero , dragon)"""
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = []

    def __str__(self) -> str:
        return f"👤 {self.name} | HP: {self.hp} | DMG: {self.damage}"

    def take_damage(self, value: int):
        """Получение урона. Не может быть меньше 0."""
        self.hp -= value
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} find {item.name}")
    def use_item(self):
        if not self.inventory:
            print("Backpack empty")
            return
    
        item = self.inventory.pop(0)
    
        if item.kind == "weapon":
            self.damage += item.value
            print(f"{self.name} equipped {item.name}. DMG + by {item.value}. Current DMG: {self.damage}")   

        if item.kind == "potion":
            self.hp += item.value
            print(f"{self.name} use {item.name}. HP + {item.value}. Current HP {self.hp}")


class Thief(Human):
    """Class thief"""
    def attack(self, enemy):
        print(f"🔪 {self.name} use fast attack on {enemy.name}!")
        enemy.take_damage(self.damage)

class Hero(Human):
    """Hero Class (uniq ability)"""
    def __init__(self, uniq_ability: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uniq = uniq_ability

    def attack(self, enemy):
        print(f"⚔️ {self.name} use {self.uniq} on {enemy.name}!")
        enemy.take_damage(self.damage)

class Dragon(Human):
    """Boss Dragon"""
    def attack(self, enemy):
        print(f"🔥🔥🔥 {self.name} fire {enemy.name}!")
        enemy.take_damage(self.damage)

def main():
    """Main Game Loop"""
    dragon=Dragon(name="Gorinich", hp=500, damage=10)
    hero=Hero(uniq_ability="Light punch", name="Valera", hp=120, damage=50)
    thief=Thief(name="Ezio", hp="40", damage=50)
    
    big_potion=Item(name="Big Heal Potion", kind="potion", value=55)
    small_potion=Item(name="Small Heal Potion", kind="potion", value=20)
    print("-" * 53)
    hero.add_item(small_potion)
    hero.add_item(big_potion)
    print("-" * 53)
    for i in hero.inventory:
        print(f"Inventory:{i}")
    print("-" * 53)
    
    while True:
        #logic alive chapters 
        alife_hero = []

        if hero.hp > 0:
            alife_hero.append(hero)

        elif not alife_hero:
            print(f"YOU LOSSE💀 -- {dragon.name} WIN")
            break
        #logic dragon and thief attack
        random_target = [dragon, hero]
        target = random.choice(random_target)
        
        
        print("---Menu game---")
        print("1.Attack\n2.Use potion\n3.Call thief\n4.Run away(exit)")

        user_choice=input("Your move:")

        if user_choice == "1":
            hero.attack(dragon)
            print(f"Dragon hp:{dragon.hp}")
            print()
            dragon.attack(target)
            print(f"Hero HP:{hero.hp}")

        elif user_choice == "2":
            hero.use_item()
            print()
            dragon.attack(target)
            print(f"Hero HP:{hero.hp}")

        elif user_choice == "3":
            thief.attack(target)
            print(f"{target.name} HP:{target.hp}")
            print()
            dragon.attack(target)

        elif user_choice == "4":
            print("bye bye...")
            print()
            print("\nHero run away...")
            break
        
        elif dragon.hp <= 0:
            print("YOU WIN🏆")
            break
        else:
            print("Wrong command!❌")

if __name__ == "__main__":
    main()
