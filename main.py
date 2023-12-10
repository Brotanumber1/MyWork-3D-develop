import pygame as pg


pg.init()
w, h = 1440, 720
screen = pg.display.set_mode((w, h))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)

    
    pg.draw.rect(screen, 'grey', (w/4, h/4, w-w/4, h-h/4))
    pg.display.update()
    screen.fill('black')