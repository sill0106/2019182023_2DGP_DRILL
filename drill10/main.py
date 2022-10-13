import pico2d
import play_state
import logo_state
state = logo_state

pico2d.open_canvas()


states = [logo_state, play_state]
for state in states:
    state.enter()  # 초기화
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.05)
    state.exit()  # 종료



pico2d.close_canvas()