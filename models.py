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
    def __init__(self, name: str, hp: int, damage: int,):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.inventory = []
        self.lvl = 1 
        self.xp = 0

    def __str__(self) -> str:
        return f"👤 {self.name} | HP: {self.hp} | DMG: {self.damage}"

    def lvl_up(self, value: int):
        self.xp + value
        print(f"{self.name} + {value}XP")
        if self.xp >= 100:
            self.xp -= 100  
            self.lvl += 1   
            self.hp += 20   
            self.damage += 10 
            print(f"🆙 LVL UP! {self.name} has lvl: {self.lvl}")
            print(f"❤️ Max HP: {self.hp}")
            print(f"⚔️ Damage: {self.damage}")

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
        luck = random.randint(1, 100)
        if luck <= 10:
            print(f"🚫 {self.name} missed")
        elif luck >= 90:
            crit_damage = self.damage * 2
            print(f"CRITICAL! {self.name} hit {enemy.name} with double damage!")
            enemy.take_damage(crit_damage)
        else:
            print(f"🔪 {self.name} use fast attack on {enemy.name}!")
            enemy.take_damage(self.damage)

class Hero(Human):
    """Hero Class (uniq ability)"""
    def __init__(self, uniq_ability: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uniq = uniq_ability

    def attack(self, enemy):
        luck = random.randint(1, 100)
        if luck <= 10:
            print(f"🚫 {self.name} missed")
        elif luck >= 90:
            crit_damage = self.damage * 2
            print(f"CRITICAL! {self.name} hit {enemy.name} with double damage!")
            enemy.take_damage(crit_damage)
        else:
            print(f"⚔️ {self.name} use {self.uniq} on {enemy.name}!")
            enemy.take_damage(self.damage)

class Dragon(Human):
    """Boss Dragon"""
    def attack(self, enemy):
        luck = random.randint(1, 100)
        if luck <= 10:
            print(f"🚫 {self.name} missed")
        elif luck >= 90:
            crit_damage = self.damage * 2
            print(f"CRITICAL! {self.name} hit {enemy.name} with double damage!")
            enemy.take_damage(crit_damage)
        else:
            print(f"🔥🔥🔥 {self.name} fire {enemy.name}!")
            enemy.take_damage(self.damage)
