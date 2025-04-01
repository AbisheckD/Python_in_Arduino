from pyfirmata import Arduino, util
import time

board = Arduino('COM7')  # port number

led_pin = 13  # inbuild led

print("Blinking LED on pin 13")

while True:
    board.digital[led_pin].write(1)  # Turn LED ON
    time.sleep(1)  # Wait for 1 second
    board.digital[led_pin].write(0)  # Turn LED OFF
    time.sleep(1)  # Wait for 1 second
