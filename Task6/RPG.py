
import random
import json
import os

class Character:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        damage = max(0, self.atk - target.defense)
        target.hp -= damage
        print(f"{self.name} hits {target.name} for {damage} damage!")

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10, 5)
        self.inventory = []

class Enemy(Character):
    def __init__(self):
        super().__init__("Goblin", 30, 8, 2)

def fight(player, enemy):
    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
    if player.is_alive():
        print("You defeated the enemy!")
    else:
        print("You died. Game over.")
        exit()

def explore(player):
    print("You explore a new area...")
    event = random.choice(["enemy", "item", "nothing"])
    if event == "enemy":
        print("An enemy appears!")
        fight(player, Enemy())
    elif event == "item":
        print("You found a potion!")
        player.inventory.append("potion")
    else:
        print("Nothing here.")

def save(player):
    data = {"hp": player.hp, "inventory": player.inventory}
    with open("save.json", "w") as f:
        json.dump(data, f)
    print("Game saved.")

def load(name):
    if not os.path.exists("save.json"):
        return Player(name)
    with open("save.json") as f:
        data = json.load(f)
    p = Player(name)
    p.hp = data["hp"]
    p.inventory = data["inventory"]
    print("Game loaded.")
    return p

def main():
    name = input("Enter your name: ")
    player = load(name)

    while True:
        print(f"\n{player.name} [HP: {player.hp}]")
        print("1. Explore  2. Inventory  3. Save  4. Quit")
        choice = input("Choose: ")
        if choice == "1":
            explore(player)
        elif choice == "2":
            print("Inventory:", player.inventory)
        elif choice == "3":
            save(player)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
