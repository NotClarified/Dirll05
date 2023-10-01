from pico2d import *
import random

TUK_X, TUK_Y = 1280, 1024
open_canvas(TUK_X, TUK_Y)

ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

frame = 0
running = True

character_x, character_y = 0, 0
point_x, point_y = 0, 0
#화살표 랜덤 생성
def make_arrow():
    global point_x, point_y
    point_x, point_y = random.randint(0, TUK_X), random.randint(0, TUK_Y)  # 랜덤 포인트 생성
    arrow.clip_draw(0, 0, 50, 52, point_x, point_y) #array의 x,y크기 50, 52픽셀

def character_move():
    if (character_x > point_x):
        character.clip_draw(frame * 100, 10, 100, 80, character_x, character_y)  # left
        if(character_x == point_x):
            character.clip_draw(frame * 100, 310, 100, 80, character_x, character_y)  # left_stop
    elif (character_x < point_x):
        character.clip_draw(frame * 100, 110, 100, 80, character_x, character_y)  # right
        if(character_x == point_x):
            character.clip_draw(frame * 100, 410, 100, 80, character_x, character_y)  # right_stop


#화살표 따라가기
def rand_events():
    global running
    global character_x, character_y, point_x, point_y
    events =get_events()
    make_arrow()
    for events in events:
        for i in range (0, 100+1, 4):
            t = i / 100
            character_x = (1-t) * character_x + t * point_x
            character_y = (1-t) * character_y + t * point_y
            #character_move()
            #update_canvas()


while running:
    clear_canvas()
    ground.draw(TUK_X // 2, TUK_Y // 2)
    rand_events()

    # character.clip_draw(left,bottom,width,height,x,y)
    update_canvas()
    frame = (frame + 1) % 5
    delay(0.4)
