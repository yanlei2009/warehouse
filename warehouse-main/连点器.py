import pyautogui
import time

import keyboard

n=input('循环次数>>>')
times=input('间隔时间>>>')
key=input('启动按键>>>')
stop_key=input('终止按键>>>')
while True:
    if keyboard.is_pressed(key):
        print('start')
        for i in range(int(n)):
            if keyboard.is_pressed(stop_key):
                break
            time.sleep(float(times))
            pyautogui.click(button='left')
        break

print('over')