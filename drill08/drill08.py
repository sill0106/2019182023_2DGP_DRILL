from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024



def handle_events():
    global running
    global dirx
    global diry
    global h
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                h = 100
            elif event.key == SDLK_LEFT:
                dirx -= 1
                h = 0
            elif event.key == SDLK_UP:
                diry += 1
                if(h == 300):
                    h = 100
                elif(h == 200):
                    h = 0
            elif event.key == SDLK_DOWN:
                diry -= 1
                if (h == 300):
                    h = 100
                elif (h == 200):
                    h = 0
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
                h = 300
            elif event.key == SDLK_LEFT:
                dirx += 1
                h = 200
            elif event.key == SDLK_UP:
                diry -= 1
                if (h == 100):
                    h = 300
                elif (h == 0):
                    h = 200
            elif event.key == SDLK_DOWN:
                diry += 1
                if (h == 100):
                    h = 300
                elif (h == 0):
                    h = 200

open_canvas(TUK_WIDTH, TUK_HEIGHT)




kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dirx = 0
diry = 0
h = 300
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)



    character.clip_draw(frame * 100, h, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    if (0 < x < TUK_WIDTH):
        x += dirx * 5
    elif(x <= 0):
        x = 1
    elif(TUK_WIDTH <= x):
        x = TUK_WIDTH - 1

    if (0 < y < TUK_HEIGHT):
        y += diry * 5
    elif(y <= 0):
        y = 1
    elif(TUK_HEIGHT <= y):
        y = TUK_HEIGHT - 1





    handle_events()


close_canvas()




