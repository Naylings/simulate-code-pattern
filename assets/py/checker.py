import json, game

EXPECT = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0),
          'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}

def check(module):
    out = {}
    for name, (dx, dy) in EXPECT.items():
        p = game.Player(); x, y = p.x, p.y
        try:
            module.handle_input(game.Keys({name}), p)
            mx, my = p.x - x, p.y - y
            out[name] = mx * dx + my * dy > 0 and mx * dy == 0 and my * dx == 0
        except Exception:
            out[name] = False
    return json.dumps(out)
