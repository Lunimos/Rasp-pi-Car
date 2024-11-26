# Rasp-pi-Car
Code for an Raspberrypi that using the arrow keys 

How It Works
GPIO Pin Configuration:

The pins 7, 11, 13, and 15 are configured as outputs to control the buggy's motors.
These pins likely correspond to the inputs on a motor driver (like L298N or L293D), which is responsible for driving the buggy's motors.
Keyboard Controls:

The code uses the curses library to capture keyboard inputs:
Arrow Up (KEY_UP): Activates forward movement by turning on 7 and 13.
Arrow Down (KEY_DOWN): Activates backward movement by turning on 11 and 15.
Arrow Right (KEY_RIGHT): Activates right movement by turning on 7.
Arrow Left (KEY_LEFT): Activates left movement by turning on 13.
Pressing q stops the program.
Motor Control:

The GPIO.output() commands control which motor moves. Depending on your motor driver setup:
A HIGH signal on a specific pin makes the motor spin in one direction.
A LOW signal stops the motor.
Safety:

Before processing new inputs, the code resets all GPIO outputs to False (LOW) to stop the buggy, ensuring only the intended motors are activated.
What You Need for It to Work
Hardware Setup:

Raspberry Pi: Ensure it's powered and set up to run Python scripts.
Motor Driver: Connect the Pi's GPIO pins to a motor driver module (e.g., L298N or L293D). The motor driver will interface between the Pi and the motors.
Buggy Motors: Connect the motors to the motor driver. Ensure they are powered by an external power source (not the Pi).
Pin Mapping:

Double-check that the GPIO pins (7, 11, 13, 15) are correctly connected to the motor driver's input pins.
Power Supply:

The motors need their own power supply (e.g., a battery pack) because the Raspberry Pi's GPIO pins cannot directly power motors.
Dependencies:

The code requires the RPi.GPIO and curses Python libraries. Install them with:
sudo apt-get install python3-curses
pip3 install RPi.GPIO

Keyboard Input:

Run the script in a terminal with a connected keyboard. The curses library requires a terminal interface to capture input.

############-------How to Connect--------############

Remote Connection via SSH (Using PuTTY or Other SSH Clients)
If your Raspberry Pi is connected to your network, you can access it remotely:

Using PuTTY (Windows):

Find the Raspberry Pi's IP address (e.g., using your router or by running hostname -I on the Pi).
Open PuTTY and enter the Pi's IP address in the "Host Name" field.
Connect using your Pi's username (default: pi) and password (default: raspberry unless changed).
Once logged in, navigate to the directory containing the script and run it
############-------------------------------############
