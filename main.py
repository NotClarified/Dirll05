from pico2d import *

TUK_X, TUK_Y = 1280, 1024
open_canvas(TUK_X, TUK_Y)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
stop_character = load_image('character.png')

frame = 0
running = True
while running:
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)
    character.clip_draw(frame * 215 + 350, 560, 100, 115, TUK_X/2, TUK_Y/2)
    # character.clip_draw(left,bottom,width,height,x,y)
    update_canvas()
    frame = (frame + 1) % 5
    delay(0.4)
