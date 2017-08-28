import os
import pyxhook
import time
#import pythoncom
import pyglet
from pyglet.window import key
from pykeyboard import PyKeyboard

k = PyKeyboard()
#window = pyglet.window.Window()
keys = key.KeyStateHandler()
#window.push_handlers(keys)

capsDown = False
ctrlFlag = False
shftFlag = False
zeroFlag = False

def OnKeyPress(event):
    global k
    global capsDown
    global ctrlFlag
    global shftFlag
    global zeroFlag
    #print 'keypress'
    #print event.Ascii

    if event.Ascii == 96:
        #print 'The grave key was pressed.'
        escape = True
        os._exit(0)
    
    if event.Ascii == 0:# or (event.Ascii == 229):
        #print 'CAPS'
        capsDown = True

    if (event.Ascii == 227) == capsDown == True:
        #print 'LCTRL flag on'
        ctrlFlag = True
    if (event.Ascii == 225) == capsDown == ctrlFlag == True:
        #print 'shift flag on'
        shftFlag = True
    if (event.Ascii == 48) == capsDown == shftFlag == ctrlFlag == True:
        #print '0 flag on'
	zeroFlag = True
        #pyglet.app.exit()


#@window.event.Ascii
def OnKeyRelease(symbol):
    global capsDown
    global ctrlFlag
    global shftFlag
    global zeroFlag

    #print symbol.Ascii

#Currently CAPS lock key is deactivated so it returns an Ascii of 0
#CAPSLOCK ASCII CODE WHEN NOT DEACTIVATED == 229:
    if symbol.Ascii == 0:
	if ctrlFlag == shftFlag == zeroFlag == True:
	    k.type_string('password')
            k.press_key(k.enter_key)
            k.release_key(k.enter_key)

        capsDown = False
	ctrlFlag = False
	shftFlag = False
	zeroFlag = False

#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
new_hook.KeyUp=OnKeyRelease
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()

#pyglet.app.run()
