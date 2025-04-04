# LED Blinking using PyFirmata and Arduino Mega 2560

## Overview
This project demonstrates how to blink the built-in LED on an Arduino Mega 2560 board using Python and PyFirmata.

## Requirements
- Arduino Mega 2560
- PyFirmata Library
- Python 3.10.0 (or compatible version)
- Arduino IDE
- USB Cable for connection

## Steps to Run the LED Blink Program

### Step 1: Install PyFirmata on Arduino
1. Open **Arduino IDE**.
2. Go to **File** -> **Examples** -> **PyFirmata** -> **StandardFirmata**.
3. Upload the **StandardFirmata** sketch to the Arduino Mega 2560.

### Step 2: Install Python and PyFirmata Library
1. Install Python 3.10.0 if not already installed.
2. Open **VS Code**.
3. Change the Python interpreter to Python 3.10.0 using `Ctrl + Shift + P` -> **Python: Select Interpreter**.
4. Install PyFirmata using the terminal:
   ```sh
   pip install pyfirmata
   ```

### Step 3: Run the LED Blinking Code
1. Open a new Python file (e.g., `led_blink.py`).
2. Add the following code:
   ```python
   from pyfirmata import Arduino, util
   import time

   board = Arduino('COM7')  # Change COM port if necessary

   led_pin = 13  # Built-in LED pin

   print("Blinking LED on pin 13")

   while True:
       board.digital[led_pin].write(1)  # Turn LED ON
       time.sleep(1)  # Wait for 1 second
       board.digital[led_pin].write(0)  # Turn LED OFF
       time.sleep(1)  # Wait for 1 second
   ```
3. Save the file.
4. Run the script in the VS Code terminal:
   ```sh
   python led_blink.py
   ```

## Explanation of the Code
- **Importing PyFirmata and time module**: Required for communication with Arduino and adding delays.
- **Connecting to Arduino**: `board = Arduino('COM7')` establishes a connection.
- **Defining the LED pin**: `led_pin = 13` assigns the built-in LED.
- **Loop to blink LED**: The `while True` loop continuously turns the LED on and off with a 1-second delay.

## Expected Output
The built-in LED on pin 13 of the Arduino Mega 2560 will blink every second.

## Notes
- Ensure the correct COM port is set in the code.
- Close the Arduino Serial Monitor before running the Python script, as it may interfere with serial communication.

---
Now, your GitHub profile will have a structured and easy-to-follow README for LED blinking using PyFirmata! 🚀

