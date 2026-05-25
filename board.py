import random

from cell import Cell
from player import Player
from enemy import Enemy


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self._build_grid()
        self._link_neighbors()
        self.player = Player(15, 10)
        self.enemy = Enemy(30, 10, self.player)
        self._scatter_obstacles()
        self.score = 0

    def _build_grid(self):
        grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                cell = Cell(x, y)
                if random.randint(0, 12) == 0:
                    cell.make_anchor()
                elif random.randint(0, 50) == 0:
                    cell.make_coin()
                row.append(cell)
            grid.append(row)
        return grid

    def _scatter_obstacles(self):
        for row in self.grid:
            for cell in row:
                if not cell.is_anchor():
                    continue
                for neighbor in cell.get_neighbors():
                    if random.randint(0, 10) == 2 and not neighbor.is_coin():
                        neighbor.make_ground()
                        for inner in neighbor.get_neighbors():
                            if not neighbor.is_coin():
                                inner.make_obstacle()

    def _link_neighbors(self):
        for y in range(self.height):
            for x in range(self.width):
                self._attach_neighbors(x, y)

    def _attach_neighbors(self, x, y):
        cell = self.get_cell(x, y)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                neighbor = self.get_cell(x + dx, y + dy)
                if neighbor is not None:
                    cell.add_neighbor(neighbor)

    def get_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def draw(self):
        print(f"Score: {self.score}")
        for row in self.grid:
            for cell in row:
                print(cell.get_symbol(self.player, self.enemy), end=" ")
            print("\n")

    def move_player(self, direction):
        x, y = self.player.get_position()
        target = {
            "up": (x, y - 1),
            "down": (x, y + 1),
            "right": (x + 1, y),
            "left": (x - 1, y),
        }[direction]
        cell = self.get_cell(*target)
        if cell is not None and not cell.is_obstacle():
            getattr(self.player, direction)()

    def throw_grenade(self, direction):
        x, y = self.player.get_position()
        offsets = {"up": (0, -3), "down": (0, 3), "right": (3, 0), "left": (-3, 0)}
        dx, dy = offsets[direction]
        target = self.get_cell(x + dx, y + dy)
        if target is None:
            return
        target.clear_obstacle()
        for n in target.get_neighbors():
            n.clear_obstacle()

    def bomb(self):
        x, y = self.player.get_position()
        center = self.get_cell(x, y)
        if center is None:
            return
        for n in center.get_neighbors():
            n.clear_obstacle()
            for nn in n.get_neighbors():
                nn.clear_obstacle()

    def get_enemy(self):
        return self.enemy

    def get_player(self):
        return self.player

    def collect_coins(self):
        for row in self.grid:
            for cell in row:
                if cell.is_coin() and cell.get_position() == self.player.get_position():
                    self.score += 1
                    cell.remove_coin()
