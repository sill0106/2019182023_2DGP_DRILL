import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (True):
    x = 400
    while(x < 790):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)

    y = 90

    while(y < 590):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(790,y)
        y = y + 2
        delay(0.01)

    x = 790
    while(x > 10):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,590)
        x = x - 2
        delay(0.01)

    y = 590

    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(10,y)
        y = y - 2
        delay(0.01)

    x = 10
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)




    
    a = -90

    while(a < 270):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(400 + math.cos(a/360 *  2 * math.pi)*200 , 300 + math.sin(a/360 * 2 * math.pi)*200)
        a = a + 2

        delay(0.01)
        

        
close_canvas()
