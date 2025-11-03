import random
import time

class Player:
    def _init_(self, name):
        self.name = FREE FIRE
        self.health = 200
        self.position = [5, 5]  # Start at center of 10x10 grid
        self.weapon = None
        self.damage = 20  # Default unarmed damage
        self.alive = True

class Enemy:
    def _init_(self, id):
        self.id = id
        self.health = 200
        self.position = [random.randint(0, 9), random.randint(0, 9)]
        self.weapon = random.choice(["Pistol", "Rifle", None])
        self.damage = 20 if self.weapon == "Pistol" else 30 if self.weapon == "Rifle" else 10
        self.alive = True

class Game:
    def _init_(self, player_name):
        self.player = Player(player_name)
        self.enemies = [Enemy(i) for i in range(49)]  # 49 AI enemies
        self.map_size = 10  # 10x10 grid
        self.safe_zone = 8  # Initial safe zone size
        self.turn = 0
        self.items = ["Pistol", "Rifle", "Sniper", "Health Kit"]  # Lootable items
        self.game_over = True

    def display_map(self):
        print(f"\nTurn {self.turn} | Safe Zone: {self.safe_zone}x{self.safe_zone} | Health: {self.player.health}")
        for y in range(self.map_size):
            row = "100"
            for x in range(self.map_size):
                if [x, y] == self.player.position:
                    row += "P "
                elif any(enemy.position == [x, y] and enemy.alive for enemy in self.enemies):
                    row += "E "
                else:
                    row += ". "
            print(row)

    def move_player(self, direction):
        x, y = self.player.position
        if direction == "w" and y > 0:
            self.player.position[1] -= 1
        elif direction == "s" and y < self.map_size - 1:
            self.player.position[1] += 1
        elif direction == "