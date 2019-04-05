#!/usr/bin/env python
'''Written by the group Team Machine'''

from nxt.locator import *

from nxt.motor import *

import Tkinter as tk

import sys

import time

b = find_one_brick()
m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)


# Motor's must be a number between -128 and 127
def forward():
    m_right.run(127)
    m_left.run(127)

def reverse():
    m_right.run(-70)
    m_left.run(-70)

def left():
    m_right.run(127)
    m_left.run(60)

def right():
    m_left.run(127)
    m_right.run(60)

def stop():
    m_right.brake()
    m_left.brake()

def honk():
    b.play_tone_and_wait(523, 500)

def close():
    print 'Bye!'
    exit()

def drive(go):
    print 'Drive command: ', go.char
    key_press = go.char
    if key_press.lower() == 'w':
        forward()
    elif key_press.lower() == 's':
        reverse()
    elif key_press.lower() == 'a':
        left()
    elif key_press.lower() == 'd':
        right()
    elif key_press.lower() == 'q':
        stop()
    elif key_press.lower() == 'h':
        honk()
    elif key_press.lower() == 'l':
        close()

command = tk.Tk()
command.bind('<KeyPress>', drive)
command.mainloop()
