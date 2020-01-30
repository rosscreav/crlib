

import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
##Keys
#letters
dict={'alt':Key.alt, 'ctrl':Key.ctrl, 'win':Key.cmd, 'f4':Key.f4, 'esc':Key.esc, 'enter':Key.enter, 'tab':Key.tab, 'shift':Key.shift, 'up':Key.up, 'down':Key.down, 'right':Key.right, 'left':Key.left}
held=[]


def press_key(key):
    if len(key)==1:
        keyboard.press(key)
        time.sleep(0.1)
        keyboard.release(key)
        time.sleep(0.2)
    elif key in dict:
        keyboard.press(dict[key])
        time.sleep(0.1)
        keyboard.release(dict[key])
        time.sleep(0.2)
    else:
        raise Exception(key+': is not a valid input')

def type(string):
    keyboard.type(string)
    
def hold(key):
    if len(key)==1:
        keyboard.press(key)
        time.sleep(0.1)
        held.append(key)
    elif key in dict:
        keyboard.press(dict[key])
        time.sleep(0.1)
        held.append(key)
    else:
        raise Exception(key+': is not a valid input')

def release(key):
    if key in held:
        if len(key)==1:
            keyboard.release(key)
            time.sleep(0.1)
            held.remove(key)
        elif key in dict:
            keyboard.release(dict[key])
            time.sleep(0.1)
            held.remove(key)

def search(string):
    hold('win')
    press_key('s')
    release('win')
    time.sleep(0.2)
    type(string)
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    