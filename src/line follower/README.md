All three source codes (line follower right and left, and drive.py) imports from the nxt library as described in the installation guide. Here we use an open source repository [nxt-python, eelviny](https://github.com/eelviny/nxt-python) who entail the basics of the connection procedure that allow us to connect to the robot.

# Line follower left/right

The right/left line follower first connects to the "brick" which in other words means the computer-module of the robot.
Here we use a bluetooth module called PyBluez (see installation guide) to allow bluetooth communication between devices.
Time limit is set to 30, meaning that the program functions in 30 seconds, this could be set on different parameters. E.g., the robot could be stopped when reaching a specific color or something in the likes of that.

The light sensor is initialized as well as the motors, PORT_4 (light), PORT_B and PORT_C. These are the ports where the sensors and motors are connected to the brick.

light.set_illuminated(True) turns the light sensor on meaning it is ready to collect data.
Thereof we have a print light_value which tells the motor how to interact with the light sensor data. Where and when to brake and turn on the given signals. 

After 30s the robot brakes both wheels and the connection is exited.

# How it works in practice

The robot came with a paper race track; a black oval circle on a white paper canvas. We have both used this canvas as well as drawing our own lines on paper. 
The robot will follow the black line either on the right or the left side of the line. It will follow the line with little fault and will do so for 30 seconds. 

If we look at the print light_value method we can easily understand how it works:

print light_value
    if light_value < 500:
        m_left.brake()
        m_right.run(65)
    else:
        m_right.brake()
        m_left.run(65)
             
This is the left line follower. If the light sensor registrers a light_value excess of 500: the left wheel(motor) will brake and the right wheel will run. Else the right wheel will brake and the left wheel wil run. 
This means that the robot will "wiggle" its way along the black line interval-wise, continously for 30 seconds.


