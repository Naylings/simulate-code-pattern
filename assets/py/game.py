import asyncio, pygame

running = False

class Player:
    def __init__(self):
        self.x, self.y, self.w, self.h, self.speed = 40, 170, 24, 24, 3

class Keys:
    """Meniru pygame.key.get_pressed(): keys[pygame.K_w] -> True/False."""
    def __init__(self, names):
        self.names = set(names)
    def __getitem__(self, k):
        return pygame.key.name(k) in self.names

def stop():
    global running
    running = False

async def run(module, get_keys):
    global running
    running = True
    pygame.init()
    screen = pygame.display.set_mode((520, 260))
    p = Player()
    try:
        while running:
            module.handle_input(Keys(get_keys().to_py()), p)
            p.x = max(0, min(496, p.x)); p.y = max(0, min(186, p.y))
            screen.fill((15, 23, 42))
            pygame.draw.rect(screen, (71, 85, 105), (0, 210, 520, 50))
            pygame.draw.rect(screen, (34, 197, 94), (p.x, p.y, p.w, p.h))
            pygame.display.flip()
            await asyncio.sleep(1 / 60)
    finally:
        pygame.quit()