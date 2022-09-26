from pico2d import *
open_canvas()
character = load_image('pngwing.com.png')

x = 0

frame = 0
line = 2480 - 155
while (True):
    clear_canvas()
    character.clip_draw(frame * 171, line, 171, 155, 400, 300)
    update_canvas()
    frame = (frame + 1) % 9
    delay(0.05)
    get_events()

    if(frame == 0):
        line = line - 155

    if(line == 0):
        line = 2480 - 155
    


close_canvas()
