#!/usr/bin/env python
'''Written by the group Team Machine'''

from nxt.locator import *

from nxt.motor import *

import Tkinter as tk

import time

b = find_one_brick()
m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)
m_vertical = Motor(b, PORT_A)


# Motor value must be a number between -128 and 127
def fast_forward():
    m_right.run(127)
    m_left.run(127)

def slow_forward():
    m_right.run(60)
    m_left.run(60)

def reverse():
    m_right.run(-70)
    m_left.run(-70)

def slow_left():
    m_right.run(60)
    m_left.brake()

def slow_right():
    m_left.run(60)
    m_right.brake()

def fast_left():
    m_right.run(127)
    m_left.run(60)

def fast_right():
    m_left.run(127)
    m_right.run(60)

def stop():
    m_right.brake()
    m_left.brake()

def honk():
    b.play_tone_and_wait(523, 500)


def drive(go):
    print 'Drive command: ', go.char
    key_press = go.char
    if key_press.lower() == 'w':
        fast_forward()
    elif key_press.lower() == 's':
        reverse()
    elif key_press.lower() == 'a':
        fast_left()
    elif key_press.lower() == 'd':
        fast_right()
    elif key_press.lower() == 'q':
        slow_left()
    elif key_press.lower() == 'e':
        slow_right()
    elif key_press.lower() == 'b':
        stop()
    elif key_press.lower() == 'x':
        slow_forward()
    elif key_press.lower() == 'h':
        honk()

command = tk.Tk()
command.bind('<KeyPress>', drive)
command.mainloop()
