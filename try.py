from ps3 import *

p = ps3()
s = 150
flag = 0
run = 1

while True:
    p.update()
    if p.up:
        print "up"
    elif p.left:		#If LEFT is pressed turn left
        print "l"
    elif p.right:		#If RIGHT is pressed move right
        print "r"
    elif p.down:		#If DOWN is pressed go back
        print "down"

    time.sleep(0.01)
