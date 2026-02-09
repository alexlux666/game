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
    dragon=Dragon(name="Gorinich", hp=500, damage=25)
    hero=Hero(uniq_ability="Light punch", name="Valera", hp=120, damage=50)
    thief=Thief(name="Ezio", hp=40, damage=50)
    
    sword=Item(name="Gold Sword", kind="weapon", value=25)
    big_potion=Item(name="Big Heal Potion", kind="potion", value=55)

    print("-" * 53)
    hero.add_item(sword)
    hero.add_item(big_potion)
    print("-" * 53)

    for i in hero.inventory:
        print(f"Inventory:{i}")
    print("-" * 53)
    
    while True:
        if hero.hp <= 0:
            print(f"\n☠️ {hero.name} killed...\n{dragon.name} WIN!☠️")
            break
        if dragon.hp <= 0:
            print(f"\n🏆 {dragon.name} killed!!!\n{hero.name} CHAMPION! 🏆")
            break
        
        print("---Menu game---")
        print(f"1.Attack {dragon.name}")
        print("2.Buff (Use Item)")
        if thief.hp > 0:
            print(f"3.Call {thief.name}(RISK!)")
        print("4.Run away(exit)")
        print(f"Hero HP: {hero.hp} | Dragon HP: {dragon.hp} | Thief HP: {thief.hp}")
        user_choice=input("Your move:")

        hero_move = False

        if user_choice == "1":
            hero.attack(dragon)
            hero_move = True
            print()

        elif user_choice == "2":
            hero.use_item()
            hero_move = True
            print()

        elif user_choice == "3":
            if thief.hp > 0:
                print(f"🥷 From shadow {thief.name}...")
                target_75 = [dragon, dragon, dragon, hero]
                thief_target = random.choice(target_75)
                thief.attack(thief_target)
                hero_move = True
            else:
                print(f"{thief.name} Dead💀")
            print()

        elif user_choice == "4":
            print("bye bye...")
            print()
            print("\n🏃Hero run away...")
            break
        
        else:
            print("Wrong command!❌")
            continue
        
        if dragon.hp > 0:
            print(f"🐲 {dragon.name} move...")
            alive_humans = []
            alive_humans.append(hero)
            if thief.hp > 0:
                alive_humans.append(thief)
            victim = random.choice(alive_humans)
            dragon.attack(victim) 
            
if __name__ == "__main__":
    main()
