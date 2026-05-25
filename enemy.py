class Enemy:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player

    def update(self):
        px, py = self.player.get_position()
        dx = self.x - px
        dy = self.y - py

        if abs(dx) <= abs(dy):
            self.y += 1 if dy < 0 else -1
        else:
            self.x += 1 if dx < 0 else -1

    def get_position(self):
        return [self.x, self.y]
