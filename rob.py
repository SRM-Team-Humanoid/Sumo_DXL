import pypot.dynamixel
import time
from bluedot import BlueDot
from signal import pause


ports = pypot.dynamixel.get_available_ports()
print(ports)

dxl = pypot.dynamixel.DxlIO(ports[0])

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
    dxl.set_goal_position({1:0,2:0,3:0,4:0, 5:90, 6:-90})
    dxl.set_goal_position({7:45,8:-45})
    c,d=35,25
    a,b=25,25
    for i in range(6):
        dxl.set_moving_speed({1:100,2:100,3:100,4:100})
        dxl.set_goal_position({3:a,4:b})
        time.sleep(0.3)
        a,b=-a,-b
        dxl.set_goal_position({1:c,2:d})
        c,d=-d,-c
        time.sleep(0.3)
    dxl.set_goal_position({1:0,2:0,3:0,4:0})

def right():
    dxl.set_goal_position({5:90, 6:-90, 7:10, 8:-10})
    a,b = -25,-35
    dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})
    c = 55
    dxl.set_goal_position({3:-a, 4:-b})
    time.sleep(1)
    dxl.set_goal_position({1:-b, 2: -a})
    time.sleep(1)
    dxl.set_goal_position({4:0})
    time.sleep(1)
    dxl.set_goal_position({1: 0,2:0, 3: 0})
    time.sleep(1)

def left():
    b,a = 25,35
    dxl.set_goal_position({5:90, 6:-90, 7:18, 8:-18})
    dxl.set_moving_speed({1:70, 2:70, 3:100, 4:100})
    c = -55
    dxl.set_goal_position({3:-a, 4:-b})
    time.sleep(1)
    dxl.set_goal_position({1:-b, 2:-a})
    time.sleep(1)
    dxl.set_goal_position({3:0})
    time.sleep(1)
    dxl.set_goal_position({1:0,2: 0, 4: 0})
    time.sleep(1)


def forward():
    dxl.set_goal_position({1:0,2:0,3:0,4:0, 5:90, 6:-90})
    dxl.set_goal_position({7:45,8:-45})
    c,d=35,25
    a,b=-25,-25
    for i in range(6):
        dxl.set_moving_speed({1:100,2:100,3:100,4:100})
        dxl.set_goal_position({3:a,4:b})
        time.sleep(0.3)
        a,b=-a,-b
        dxl.set_goal_position({1:c,2:d})
        c,d=-d,-c
        time.sleep(0.3)
    dxl.set_goal_position({1:0,2:0,3:0,4:0})

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

if __name__ == '__main__':
    dxl.set_goal_position({1:0,2:0,3:0,4:0, 5: 0, 6: 0})
    bd = BlueDot()
    bd.when_pressed = dpad
    pause()
    # print(dxl.scan(range(20)))
    # forward()
    # left()
    # right()
    # back()
    # prone_back()
