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
