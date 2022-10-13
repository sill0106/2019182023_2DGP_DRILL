from pico2d import *
import game_framework
import title_state
import play_state

running = True
image = None
# fill here

def enter():
    # fill here
    global image
    image = load_image('add_delete_boy.png')
    pass

def exit():
    # fill here
    global image
    del image
    pass

def update():
    # fill here

    pass

def draw():
    # fill here
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_n:
                    play_state.boy.boys = play_state.boy.boys + 1
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    if play_state.boy.boys == 1:
                        game_framework.pop_state()
                    else:
                        play_state.boy.boys = play_state.boy.boys - 1
                        game_framework.pop_state()





