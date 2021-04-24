from pygame import *


img_back = (200,225, 225)
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
window.fill(img_back)

run = True
FPS = 60
clock = time.Clock()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
    
