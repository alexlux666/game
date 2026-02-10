import random
from models import *

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
