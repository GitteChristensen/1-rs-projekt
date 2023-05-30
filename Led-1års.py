from machine import Pin
import time

led = Pin(17, Pin.OUT)

while True:
   led.value(1)
   print("LED IS ON")
   time.sleep(5)
   led.value(0)
   print("LED IS OFF")
   time.sleep(10)