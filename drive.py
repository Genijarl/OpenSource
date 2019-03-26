#!/usr/bin/env python

import nxt.locator
from nxt.motor import *

import Tkinter as tk

import sys

import time

b = nxt.locator.find_one_brick()
m_left = Motor(b, PORT_B)
m_right = Motor(b, PORT_C)
both = nxt.SynchronizedMotors(m_left, m_right, 0)
rightboth = nxt.SynchronizedMotors(m_left, m_right, 100)
leftboth = nxt.SynchronizedMotors(m_right, m_left, 100)


def forward(b):
    both.turn(100, 360, False)

def reverse(b):
    both.turn(-100, 360, False)

def left(b):
    leftboth.turn(100, 90, False)

def right(b):
    rightboth.turn(100, 90, False)

def drive(go):
    print 'Drive command: ', go.char
    key_press = go.char
    sleep_time = 0.050
    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        left(sleep_time)
    elif key_press.lower() == 'd':
        right(sleep_time)

command = tk.Tk()
command.bind('<KeyPress>', drive)
command.mainloop()
