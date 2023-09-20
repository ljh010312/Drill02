from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
c = 270
r = 210
while (1):
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)

    while ( y < 550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y + 2
        delay(0.01)

    while (x > 1):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x - 2
        delay(0.01)

    while ( y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y - 2
        delay(0.01)

    while ( x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x + 2
        delay(0.01)     
    while ( c > -90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = 400 +  r * math.cos(c / 360 * 2 * math.pi)
        y = 300 +  r * math.sin(c/ 360 * 2 * math.pi)
        c = c - 1
        delay(0.01)     

    c = 270

close_canvas()
