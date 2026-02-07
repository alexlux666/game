import random
class Item():
    def __init__(self, name: str, kind: str, value: int):
        self.name = name
        self.kind = kind
        self.value = value
    def __str__(self) -> str:
        return f"🧪{self.name} {self.kind}, baff: {self.value}"

class Human():
    """Базовый класс для всех персонажей"""
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
    """Класс Вора (быстрый удар)"""
    def attack(self, enemy):
        print(f"🔪 {self.name} делает быстрый тычок в {enemy.name}!")
        enemy.take_damage(self.damage)

class Hero(Human):
    """Класс Героя (сильный удар)"""
    def __init__(self, uniq_ability: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uniq = uniq_ability

    def attack(self, enemy):
        print(f"⚔️ {self.name} использует {self.uniq} по {enemy.name}!")
        enemy.take_damage(self.damage)

class Dragon(Human):
    """Босс вертолет"""
    def attack(self, enemy):
        print(f"🔥🔥🔥 {self.name} fire {enemy.name}!")
        enemy.take_damage(self.damage)

def main():
    hero = Hero(uniq_ability="Light punch", name="Valera", hp=120, damage=25)
    potion = Item(name="Health Potion", kind="potion", value=50)
    sword = Item(name="Steel Sword", kind="weapon", value=10)

    hero.add_item(sword)
    hero.add_item(potion)
    for i in hero.inventory:
        print(f"Inventory:{i}")
    print()
    hero.use_item()
    hero.use_item()
    print()
    print(hero)
    
if __name__ == "__main__":
    main()