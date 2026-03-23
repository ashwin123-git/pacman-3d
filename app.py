# PAC-MAN (Smooth Player + Better Ghost AI + No Overlap)

from ursina import *
import random

app = Ursina()

# Camera
camera.position = (6, 22, 6)
camera.rotation = (90, 0, 0)

# Player (smooth movement)
player = Entity(model='sphere', color=color.yellow, scale=0.6, position=(1,0.5,5))
speed = 3

# Maze
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,0,1,1,0,1,0,1],
    [0,0,0,0,1,0,0,0,1,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1]
]

walls = []
dots = []

for z,row in enumerate(maze):
    for x,val in enumerate(row):
        if val == 1:
            walls.append(Entity(model='cube', color=color.blue, position=(x,0.5,z), collider='box'))
        else:
            dots.append(Entity(model='sphere', color=color.white, scale=0.12, position=(x,0.3,z)))

Entity(model='plane', scale=(30,1,30), color=color.black)

# Ghosts (no overlap)
ghosts = [
    Entity(model='cube', color=color.red, scale=0.4, position=(6,0.5,6)),
    Entity(model='cube', color=color.green, scale=0.4, position=(5,0.5,6)),
    Entity(model='cube', color=color.orange, scale=0.4, position=(7,0.5,6)),
]

ghost_speed = 1.2

score = 0
text = Text(text="0", position=(-0.85,0.45), scale=2)


def is_wall(x, z):
    if x < 0 or z < 0 or z >= len(maze) or x >= len(maze[0]):
        return True
    return maze[int(z)][int(x)] == 1


def ghost_collides(pos, current):
    for g in ghosts:
        if g != current and int(g.x) == int(pos.x) and int(g.z) == int(pos.z):
            return True
    return False


def update():
    global score

    move = Vec3(0,0,0)

    if held_keys['w']: move += Vec3(0,0,1)
    if held_keys['s']: move += Vec3(0,0,-1)
    if held_keys['a']: move += Vec3(-1,0,0)
    if held_keys['d']: move += Vec3(1,0,0)

    if move != Vec3(0,0,0):
        move = move.normalized()
        next_pos = player.position + move * speed * time.dt

        if not is_wall(round(next_pos.x), round(next_pos.z)):
            player.position = next_pos

    # Tunnel
    if player.x < 0: player.x = 12
    if player.x > 12: player.x = 0

    # Eat dots
    for dot in dots[:]:
        if distance(player.position, dot.position) < 0.4:
            destroy(dot)
            dots.remove(dot)
            score += 1
            text.text = str(score)

        # Ghosts (STRONG chase + no overlap)
    for ghost in ghosts:
        direction = player.position - ghost.position

        # Prioritize grid direction (like Pac-Man)
        if abs(direction.x) > abs(direction.z):
            move = Vec3(1 if direction.x > 0 else -1, 0, 0)
        else:
            move = Vec3(0, 0, 1 if direction.z > 0 else -1)

        next_pos = ghost.position + move * ghost_speed * time.dt

        if not is_wall(round(next_pos.x), round(next_pos.z)) and not ghost_collides(next_pos, ghost):
            ghost.position = next_pos
        else:
            # fallback random if blocked
            move = random.choice([Vec3(1,0,0), Vec3(-1,0,0), Vec3(0,0,1), Vec3(0,0,-1)])
            next_pos = ghost.position + move * ghost_speed * time.dt
            if not is_wall(round(next_pos.x), round(next_pos.z)):
                ghost.position = next_pos

        if distance(player.position, ghost.position) < 0.5:
            text.text = "GAME OVER"
            application.pause()

app.run()
