import pygame
from commands import MoveUpCommand, MoveDownCommand, MoveLeftCommand, MoveRightCommand

class InputHandler:
    def __init__(self):
        self.button_map = {
            pygame.K_UP: MoveUpCommand(),
            pygame.K_DOWN: MoveDownCommand(),
            pygame.K_LEFT: MoveLeftCommand(),
            pygame.K_RIGHT: MoveRightCommand(),
            # TODO: tambahkan W, A, S, D di sini
        }

    def handle(self, keys, player):
        for key, command in self.button_map.items():
            if keys[key]:
                command.execute(player)

handler = InputHandler()

def handle_input(keys, player):  # bagian ini jangan diubah
    handler.handle(keys, player)
