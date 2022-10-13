from pico2d import *

import game_framework
import play_state
running = True
image = None
title_time = 0.0

def enter():
    # fill here
    global image
    image = load_image('title.png')
    pass

def exit():
    # fill here
    global image
    del image
    pass

def handle_events():
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(play_state)
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():

    pass

def pause():
    pass

def resume():
    pass






