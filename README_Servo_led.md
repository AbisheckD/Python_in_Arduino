# Servo Motor Control in Arduino Mega 2560 using Python with pyFirmata

## Overview
This project demonstrates how to control an Arduino Mega 2560 board using Python with the pyFirmata library. The example showcases basic servo motor control, where a servo connected to an Arduino board sweeps between 0° and 180° at a specified interval.

## Prerequisites
Before running this project, ensure you have the following:

- **Arduino Mega 2560 Board**
- **Servo Motor**
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

board = Arduino('COM7')  # Change COM port as per your setup
servo = board.get_pin('d:6:s')  # Servo on pin 6

while True:
    for angle in range(0, 181, 10):
        servo.write(angle)
        time.sleep(0.5)
    for angle in range(180, -1, -10):
        servo.write(angle)
        time.sleep(0.5)
```

### Explanation:
- `Arduino('COM7')`: Connects to the Arduino board on the specified COM port.
- `board.get_pin('d:6:s')`: Initializes digital pin 6 as a servo control pin.
- `servo.write(angle)`: Rotates the servo to the specified angle.
- `time.sleep(0.5)`: Pauses for 0.5 seconds between angle updates.
- The loop sweeps the servo from 0° to 180° and back repeatedly.

## Customization
- Change `'d:6:s'` to another PWM-capable pin if needed.
- Modify the `range()` values to adjust sweep angle.
- Adjust `time.sleep(0.5)` to speed up or slow down the sweep.

## Troubleshooting
- **Arduino Not Detected?** Check the COM port and replace `'COM7'` with the correct port (e.g., `/dev/ttyUSB0` on Linux/Mac).
- **Ensure StandardFirmata is uploaded** to the Arduino.
- **Verify pyFirmata installation** using:
  ```sh
  pip list | grep pyfirmata
  ```

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to fork this repository, create pull requests, or report issues. Contributions are welcome!
