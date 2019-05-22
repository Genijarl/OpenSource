#!/usr/bin/env python
# simple command to e.g., test succesfull bluetooth connection
# performs a simple 180 degree spin

import nxt.locator
from nxt.motor import *

def spin_around(b):
    m_left = Motor(b, PORT_B)
    m_left.turn(100, 360)
    m_right = Motor(b, PORT_C)
    m_right.turn(-100, 360)

b = nxt.locator.find_one_brick()
spin_around(b)

