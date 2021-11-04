import keyboard
import mss
import numpy as np
from time import sleep
from pynput import mouse
from pynput.mouse import Controller, Button


# Change this part if necessary (adjust to your resolution)

# Pixel bondaries of the GAME in your screen
left = 730
top = 525
right = 1200
bbox = (left, top, right, top+1)
#
x_bbox = 25  # pixel x coordinate of the first piano key inside the bbox
next = 125  # the difference in x of the first and second piano key
speed_adjust = 0.007 # Change this value according to your hardware
# This will help as the speed of the game increases
#####

mouse = Controller()
clicks = 0
sleep(1)
print('Start!')

points_bbox = [x_bbox + i * next for i in range(4)]  # for 4 piano keys
points_screen = [(left + x_bbox) + i * next for i in range(4)]
points = list(zip(points_bbox, points_screen))

monitor = mss.mss().monitors[1] # game in first monitor
while not keyboard.is_pressed('q'):  # press q to break
    screen = np.array(mss.mss().grab(bbox))
    for p_bbox, p_screen in points:
        if screen[0, p_bbox][0] < 15:
            mouse.position = (p_screen, int(top + clicks * speed_adjust))
            mouse.click(Button.left)
            clicks += 1
