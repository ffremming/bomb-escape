from colorama import Fore, Back, Style


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obstacle = False
        self.neighbors = []
        self.anchor = False
        self.ground = False
        self.coin = False

    def clear_obstacle(self):
        if not self.ground:
            self.obstacle = False

    def is_obstacle(self):
        return self.obstacle

    def make_anchor(self):
        self.anchor = True
        self.obstacle = False
        self.ground = True

    def is_anchor(self):
        return self.anchor

    def make_obstacle(self):
        self.obstacle = True

    def make_ground(self):
        self.ground = True
        self.obstacle = True

    def is_ground(self):
        return self.ground

    def is_coin(self):
        return self.coin

    def make_coin(self):
        self.coin = True
        self.ground = False
        self.obstacle = False

    def remove_coin(self):
        self.coin = False

    def get_symbol(self, player, enemy):
        if self.is_coin():
            return f"{Fore.YELLOW}0{Style.RESET_ALL}"
        if self.get_position() == player.get_position():
            return f"{Fore.GREEN}O{Style.RESET_ALL}"
        if self.get_position() == enemy.get_position():
            return f"{Fore.RED}§{Style.RESET_ALL}"
        if self.ground:
            return f"{Back.WHITE}#{Style.RESET_ALL}"
        if self.obstacle:
            return f"{Back.WHITE}¤{Style.RESET_ALL}"
        return "."

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_neighbors(self):
        return self.neighbors

    def get_position(self):
        return [self.x, self.y]
