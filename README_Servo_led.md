# Arduino Servo Motor and LED Control using Python with pyFirmata

## Overview
This project demonstrates how to control both a servo motor and an LED on an Arduino Mega 2560 board using Python with the pyFirmata library. The servo motor sweeps between 0° and 180°, and the LED blinks at regular intervals.

## Prerequisites
Before running this project, ensure you have the following:

- **Arduino Mega 2560 Board**
- **Servo Motor**
- **LED** (optional, or use the built-in one on Pin 13)
- **USB Cable**
- **Computer with Python installed** (Python 3.10.0 recommended)
- **Arduino IDE** to upload the Firmata firmware
- **pyFirmata library** installed in Python

## Installation & Setup

### Step 1: Upload StandardFirmata to Arduino
1. Open the **Arduino IDE**.
2. Go to **File → Examples → Firmata → StandardFirmata**.
3. Select your **board type** and the correct **COM port**.
4. Upload the **StandardFirmata** sketch to the Arduino.

### Step 2: Install pyFirmata
To communicate with Arduino using Python, install the pyFirmata library:

```sh
pip install pyfirmata
```

## Running the Servo Motor Code

### Clone this repository:
```sh
git clone https://github.com/AbisheckD/Python_in_Arduino.git
cd Python_in_Arduino
```

### Run the Python script:
```sh
python servo_motor.py
```

## Code Explanation
The `servo_motor.py` script contains:

```python
from pyfirmata import Arduino, util
import time

board = Arduino('COM7')  # Change COM port 
led_pin = 13 # digital pin

servo_pin = 6 # analog pin
servo = board.get_pin(f'd:{servo_pin}:s')  # Attach servo

while True:
    print("Servo motor control")
    for angle in range(0, 181, 10):  # Move from 0° to 180°
        servo.write(angle)
        time.sleep(0.5)
    
    for angle in range(180, -1, -10):  # Move from 180° to 0°
        servo.write(angle)
        time.sleep(0.5)
            
    print("Blinking LED on pin 13")
    board.digital[led_pin].write(1)  # Turn LED ON
    time.sleep(1)  # Wait for 1 second
    board.digital[led_pin].write(0)  # Turn LED OFF
    time.sleep(1)  # Wait for 1 second
```

### Explanation:
- `Arduino('COM7')`: Connects to the Arduino board on COM7. Change it according to your system.
- `get_pin(f'd:{servo_pin}:s')`: Sets pin 6 as a servo pin.
- The servo sweeps from 0° to 180° and back.
- Pin 13 is used to blink an LED on and off.
- All actions repeat in an infinite loop.

## Customization
- Change `servo_pin = 6` to another PWM-capable pin.
- Modify `time.sleep()` to adjust speed for servo and LED blinking.
- Use a different `led_pin` if needed.

## Troubleshooting
- **Arduino Not Detected?** Check your COM port and update `'COM7'` accordingly.
- **Ensure StandardFirmata is uploaded** to your Arduino.
- **Verify pyFirmata installation**:
  ```sh
  pip list | grep pyfirmata
  ```

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to fork this repository, create pull requests, or report issues. Contributions are welcome!
