import pyautogui as pat
import keyboard

def read_key(times=10):
    key_list=[]
    for i in range(times):
        event = keyboard.read_event()
        if event.event_type == 'down':
            key_list.append(event.name)
    return key_list

def pressed_key(key_list):
    for i in key_list:
        pat.press(i)

l=read_key()

