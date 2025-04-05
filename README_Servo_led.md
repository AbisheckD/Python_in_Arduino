Servo Motor Control using Python with pyFirmata
Overview
This project demonstrates how to control a servo motor and blink an LED using Python and the pyFirmata library on an Arduino Mega 2560. The servo rotates from 0° to 180° and back, while simultaneously blinking the onboard LED on pin 13.

Repository
🔗 GitHub Repo: Python_in_Arduino
🔗 Servo Code File: Servo_Led_blink.py

Prerequisites
Make sure you have the following components:

Arduino Mega 2560 (or compatible board)

Servo Motor

LED (optional; pin 13 LED is onboard)

USB cable to connect Arduino to PC

Python 3.10.0 (Recommended)

Arduino IDE for firmware upload

pyFirmata library installed in Python

Installation & Setup
Step 1: Upload StandardFirmata to Arduino
Open the Arduino IDE

Go to File → Examples → Firmata → StandardFirmata

Select the Arduino Mega 2560 board and correct COM port

Upload the StandardFirmata sketch to your board

Step 2: Install pyFirmata
Install the library using pip in your terminal:

bash
Copy
Edit
pip install pyfirmata
Running the Servo Motor Code
Clone this repository:
bash
Copy
Edit
git clone https://github.com/AbisheckD/Python_in_Arduino.git
cd Python_in_Arduino
Run the Python script:
bash
Copy
Edit
python servo_motor.py
Code Explanation
The servo_motor.py script contains:

python
Copy
Edit
from pyfirmata import Arduino, util
import time

board = Arduino('COM7')  # Change COM port as per your setup
led_pin = 13  # LED pin
servo_pin = 6  # PWM-capable pin for servo

servo = board.get_pin(f'd:{servo_pin}:s')  # Attach servo to pin 6

while True:
    print("Servo motor control")
    for angle in range(0, 181, 10):  # 0° to 180°
        servo.write(angle)
        time.sleep(0.5)

    for angle in range(180, -1, -10):  # 180° back to 0°
        servo.write(angle)
        time.sleep(0.5)

    print("Blinking LED on pin 13")
    board.digital[led_pin].write(1)  # LED ON
    time.sleep(1)
    board.digital[led_pin].write(0)  # LED OFF
    time.sleep(1)
How it Works:
Arduino('COM7'): Connects Python to your Arduino board on COM7.

get_pin(f'd:{servo_pin}:s'): Sets up digital PWM pin 6 for servo control.

servo.write(angle): Rotates the servo to a specific angle.

The LED blinks after every complete sweep of the servo.

Customization
Change servo_pin = 6 to any other PWM-capable digital pin (like 9, 10, 11).

Adjust time.sleep(0.5) to make the servo move faster or slower.

You can remove the LED section if only the servo is needed.

Troubleshooting
Incorrect COM port? Use the right port (COMx) as shown in the Arduino IDE.

Servo not moving? Ensure it's powered correctly (5V and GND from Arduino).

Library error? Confirm pyfirmata is installed:

bash
Copy
Edit
pip list | grep pyfirmata
License
This project is open-source and available under the MIT License.

Contributing
Pull requests and issues are welcome. Fork the repo and help improve it!
