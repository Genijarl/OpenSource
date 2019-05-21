All three source codes (line follower right and left, and drive.py) imports from the nxt library as described in the installation guide. Here we use an open source repository [nxt-python, eelviny](https://github.com/eelviny/nxt-python) who entail the basics of the connection procedure that allow us to connect to the robot.

Each program is exectued in a command terminal like cmd by running the python file.

# Remote control

The remote control program imports Tkinter to bind keys to methods allowing us to steer the robot from the computer keyboard (see installation guide)
It establishes a connection between the computer and the robot brick using PyBluez and initializes the motors and sensor.
Thereafter we define the different methods for run/brake forward, reverse, left and right etc. as well as a honk for fun.

under def drive(go) we connect each method to an assigned key on the keyboard 
ex. 
if key_press.lower() == 'w':
        fast_forward()

If the "w" key is pressed, the robot will run the fast_foward method and so on.

# How it works in practice

The program functions as a remote control car. You can drive as you like within the bluetooth reach (somewhere around 20 meters).
We have made a mobile holder on the front of the robot where you can connect the mobile phone to the PC allowing you to see where you drive. The reaction time (ms) between devices is decent and controllable, but there is some. We guess somewhere around 100-200ms, which is not that much considering the age of the robot and the remote connection.
