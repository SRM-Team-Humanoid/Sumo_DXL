import pypot.dynamixel
import time
from bluedot import BlueDot
from signal import pause
from ps3 import *

ports = pypot.dynamixel.get_available_ports()
print(ports)

dxl = pypot.dynamixel.DxlIO(ports[0])

hand = 65
shoulder = 90
dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})
def prone_back():
    dxl.set_moving_speed({1:50, 2:50, 3:50, 4:50, 5:50, 6:50, 7:50, 8:50})
    dxl.set_goal_position({1:0, 2:0, 3:90, 4:-90, 5:0, 6:0,7: 90, 8:-90})
    time.sleep(5)
    dxl.set_goal_position({7:0, 8:0, 3:-30, 4:30})
    time.sleep(2)
    dxl.set_goal_position({3:0, 4:0})
    time.sleep(2)
    dxl.set_goal_position({1:0, 2:0, 5:0, 6:0, 7:45, 8:-45})

def back():
    global hand
    dxl.set_goal_position({1:0,2:0,3:0,4:0, 5:shoulder, 6:-shoulder,7: hand, 8:-hand})
    c,d=35,25
    a,b=25,25
    for i in range(4):
        dxl.set_moving_speed({1:100,2:100,3:100,4:100})
        dxl.set_goal_position({3:a,4:b})
        time.sleep(0.3)
        a,b=-a,-b
        dxl.set_goal_position({1:c,2:d})
        c,d=-d,-c
        time.sleep(0.3)
    dxl.set_goal_position({1:0,2:0,3:0,4:0})

def right():
    dxl.set_goal_position({5:shoulder, 6:-shoulder, 7:hand, 8:-hand})
    a,b = -25,-35
    dxl.set_moving_speed({1:120, 2:120, 3:150, 4:150})
    c,d = -25,-35
    dxl.set_goal_position({1:-d, 2: -c})
    time.sleep(0.7)
    dxl.set_goal_position({3:a, 4:b})
    time.sleep(0.7)
    dxl.set_goal_position({1: 0,2:0, 3: 0})
    time.sleep(0.7)
    dxl.set_goal_position({4:0})
    time.sleep(0.7)

def left():
    b,a = 25,35
    dxl.set_goal_position({5:shoulder, 6:-shoulder, 7:hand, 8:-hand})
    dxl.set_moving_speed({1:120, 2:120, 3:150, 4:150})
    d,c = 25,35
    dxl.set_goal_position({1:-d, 2:-c})
    time.sleep(0.7)
    dxl.set_goal_position({3:a, 4:b})
    time.sleep(0.7)
    dxl.set_goal_position({1:0,2: 0, 4: 0})
    time.sleep(0.7)
    dxl.set_goal_position({3:0})
    time.sleep(0.7)


def forward():
    global hand
    dxl.set_goal_position({1:0,2:0,3:0,4:0, 5:shoulder, 6:-shoulder, 7:hand, 8:-hand})
    c,d=35,25
    a,b=-25,-25
    for i in range(4):
        dxl.set_moving_speed({1:150,2:150,3:150,4:150})
        dxl.set_goal_position({3:a,4:b})
        time.sleep(0.3)
        a,b=-a,-b
        dxl.set_goal_position({1:c,2:d})
        c,d=-d,-c
        time.sleep(0.3)
    dxl.set_goal_position({1:0,2:0,3:0,4:0})
def balance():
    dxl.set_goal_position({1:-0.73, 2:3.67, 3:47.36, 4:-45.01, 5:90, 6:-90, 7:hand, 8:-hand})
def hand_turn_in():
    global hand
    dxl.set_moving_speed({7:1000, 8:1000})
    if hand > -20:
        hand -= 5
    dxl.set_goal_position({7:hand, 8:-hand})
def hand_turn_out():
    global hand
    dxl.set_moving_speed({7:1000,8:1000})
    if hand < 65:
        hand += 5
    dxl.set_goal_position({7:hand, 8:-hand})
def shoulder_up():
    global shoulder
    if shoulder < 115:
        shoulder += 5
    dxl.set_goal_position({5:shoulder, 6:-shoulder})
def shoulder_down():
    global shoulder
    if shoulder > 60:
        shoulder -= 5
    dxl.set_goal_position({5:shoulder, 6:-shoulder})
def dpad(pos):
    if pos.top:
        forward()
    elif pos.bottom:
        back()
    elif pos.left:
        left()
    elif pos.right:
        right()
    elif pos.middle:
        prone_back()
# bd = BlueDot()
# bd.when_pressed = dpad
# pause()
#-1.03, 3.96, 47.36, -45.6, 89.3, -90.18, -21.85, 21.55

if __name__ == '__main__':
    dxl.set_goal_position({1:0,2:0,3:0,4:0, 5: 40, 6: -40, 7: 0, 8:0})
    print dxl.get_present_position((1,2,3,4,5,6,7,8,))
    # bd = BlueDot()
    # bd.when_pressed = dpad
    # pause()
    p = ps3()
    while True:
        p.update()
        if p.up:
            forward()
        elif p.down:
            back()
        elif p.left:
            left()
        elif p.right:
            right()
        elif p.triangle:
            balance()
        elif p.l1:
            hand_turn_in()
        elif p.r1:
            hand_turn_out()
        elif p.l2:
            shoulder_up()
        elif p.r2:
            shoulder_down()
        time.sleep(0.2)
    # print(dxl.scan(range(20)))
    # forward()
    # left()
    # right()
    # back()
    # prone_back()
