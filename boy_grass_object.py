from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self): pass

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(5,50)
        self.frame = 0
        ball_number = random.randint(0, 1)
        if ball_number == 0:
            self.image = load_image('ball21x21.png')
        elif ball_number == 1:
            self.image = load_image('ball41x41.png')

    def update(self):
        self.frame = 0
        if self.y > 70:
            self.y -= self.speed
        else:
            self.y = 70

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
def reset_world():
    global running
    global grass
    global team
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Ball() for i in range(10)]
    world += team

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)


# finalization code

close_canvas()
