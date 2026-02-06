import random

class Human:
    """Базовый класс для всех персонажей"""
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage

    def __str__(self) -> str:
        return f"👤 {self.name} | HP: {self.hp} | DMG: {self.damage}"

    def take_damage(self, value: int):
        """Получение урона. Не может быть меньше 0."""
        self.hp -= value
        if self.hp < 0:
            self.hp = 0
        return self.hp

class Thief(Human):
    """Класс Вора (быстрый удар)"""
    def attack(self, enemy):
        print(f"🔪 {self.name} делает быстрый тычок в {enemy.name}!")
        enemy.take_damage(self.damage)

class Hero(Human):
    """Класс Героя (сильный удар)"""
    def __init__(self, uniq_ability: str, *args, **kwargs):
        # uniq_ability забираем себе, остальное (name, hp, damage) отдаем родителю
        super().__init__(*args, **kwargs)
        self.uniq = uniq_ability

    def attack(self, enemy):
        print(f"⚔️ {self.name} использует {self.uniq} по {enemy.name}!")
        enemy.take_damage(self.damage)

class Dragon(Human):
    """Босс вертолет"""
    def attack(self, enemy):
        print(f"🔥🔥🔥 {self.name} сжигает {enemy.name}!")
        enemy.take_damage(self.damage)

def main():
    # 1. Спавн персонажей
    dragon = Dragon(name="Smaug", hp=300, damage=25)
    thief = Thief(name="Горчун", hp=100, damage=15)
    
    # ВОТ ТУТ БЫЛА ОШИБКА (исправил uniq на uniq_ability)
    hero = Hero(uniq_ability="Удар Света", name="Валера", hp=120, damage=25)

    print("--- НАЧАЛО БИТВЫ ---")
    print(dragon)
    print(thief)
    print(hero)
    print("-" * 30)

    # 2. Бесконечный цикл боя
    round_number = 1
    while True:
        print(f"\n--- Раунд {round_number} ---")
        
        # --- ЛОГИКА ЖИВЫХ ---
        alive_heroes = []
        if thief.hp > 0:
            alive_heroes.append(thief)
        if hero.hp > 0:
            alive_heroes.append(hero)

        # --- ПРОВЕРКА ПОРАЖЕНИЯ ---
        if not alive_heroes:
            print(f"\n☠️ Все герои пали. {dragon.name} победил!")
            break

        # --- ХОД ДРАКОНА ---
        target = random.choice(alive_heroes)
        dragon.attack(target)

        # --- ХОД ГЕРОЕВ ---
        if thief.hp > 0:
            thief.attack(dragon)
        else:
            print(f"💀 {thief.name} лежит без сознания...")

        if hero.hp > 0:
            hero.attack(dragon)
        else:
            print(f"💀 {hero.name} лежит без сознания...")

        # --- ИНФО О БОССЕ ---
        print(f"HP Дракона: {dragon.hp}")

        # --- ПРОВЕРКА ПОБЕДЫ ---
        if dragon.hp <= 0:
            print(f"\n🏆 УРА! {dragon.name} повержен! Победа!")
            break
            
        round_number += 1

if __name__ == "__main__":
    main()