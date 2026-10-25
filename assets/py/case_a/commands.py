class MoveUpCommand:
    def execute(self, player):
        player.y -= player.speed

class MoveDownCommand:
    def execute(self, player):
        player.y += player.speed

class MoveLeftCommand:
    def execute(self, player):
        player.x -= player.speed

class MoveRightCommand:
    def execute(self, player):
        player.x += player.speed
