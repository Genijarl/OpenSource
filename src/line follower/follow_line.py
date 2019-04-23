'''Written by Team Machine'''

from nxt.locator import *

from nxt.motor import *

from nxt.sensor import *

from time import *

# Connection between NXT and computer via PyBluez

b = find_one_brick()

# Time limit

duration = 45

# Light sensor used to identify colors

light = Light(b, PORT_4)
print 'Light value: ', light.get_sample()

m_right = Motor(b, PORT_C)
m_left = Motor(b, PORT_B)

light.set_illuminated(True)

start = time()

# The motor's and sensor will work for the time set as duration

while time() - start < duration:
    print time()-start

    # Light sensor collects data

    light_value = light.get_sample()

    # How the motor interact with the values from the light sensor

    print light_value
    if light_value < 500:
        m_left.run(0)
        m_right.run(65)
    else:
        m_right.run(0)
        m_left.run(65)

# What happens when duration is completed
m_left.brake()
m_right.brake()

exit()
