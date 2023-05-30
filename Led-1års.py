import machine
import time

# Set up GPIO pin for the LED
led_pin = machine.Pin(17, machine.Pin.OUT)

while True:
    # Turn on the LED
    led_pin.on()
    print("LED IS ON")
    time.sleep(5)

    # Turn off the LED
    led_pin.off()
    print("LED IS OFF")
    time.sleep(10)
