from pico2d import *
import random

TUK_X, TUK_Y = 1280, 1024
arrow_x, arrow_y = 50, 52
open_canvas(TUK_X, TUK_Y)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

frame = 0
running = True

def make_arrow():
    point_x, point_y = random.randint(0, TUK_X), random.randint(0, TUK_Y)  # 랜덤 포인트 생성
    arrow.clip_draw(0, 0, arrow_x, arrow_y, point_x, point_y)
def rand_events():
    global running
    events =get_events()
    for events in events:
        pass



while running:
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)
    make_arrow()
    rand_events()
    #character.clip_draw(frame * 100, 10, 100, 80, TUK_X/2 , TUK_Y/2) # left
    #character.clip_draw(frame * 100, 110, 100, 80, TUK_X/2, TUK_Y/2) # right
    # character.clip_draw(left,bottom,width,height,x,y)
    update_canvas()
    frame = (frame + 1) % 5
    delay(0.4)
