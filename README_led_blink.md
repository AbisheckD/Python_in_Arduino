# Arduino Blinking LED using Python with pyFirmata

## Overview
This project demonstrates how to control an Arduino Mega 2560 board using Python with the pyFirmata library. The example showcases the basic blinking LED program, where an LED connected to an Arduino board blinks at a specified interval.

## Prerequisites
Before running this project, ensure you have the following:

- **Arduino Mega 2560 Board**
- **LED** (if using an external LED) or built-in LED on Pin 13
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

## Running the Blinking LED Code

### Clone this repository:
```sh
git clone https://github.com/abisheck-d/Arduino-LED-Blink-Python.git
cd Arduino-LED-Blink-Python
```

### Run the Python script:
```sh
python led_blink.py
```

## Code Explanation
The `led_blink.py` script contains:

```python
from pyfirmata import Arduino, util
import time

board = Arduino('COM7')  # Change COM port as per your setup
led_pin = 13  # Digital pin for LED

print("Blinking LED on pin 13")

while True:
    board.digital[led_pin].write(1)  # Turn LED ON
    time.sleep(1)  # Wait for 1 second
    board.digital[led_pin].write(0)  # Turn LED OFF
    time.sleep(1)  # Wait for 1 second
```

### Explanation:
- `Arduino('COM7')`: Connects to the Arduino board on the specified COM port.
- `board.digital[led_pin].write(1)`: Turns the LED ON.
- `time.sleep(1)`: Waits for 1 second.
- `board.digital[led_pin].write(0)`: Turns the LED OFF.
- The loop continues to blink the LED every 1 second.

## Customization
- Change `led_pin = 13` to use a different digital pin.
- Modify `time.sleep(1)` values to change the blink speed.

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

