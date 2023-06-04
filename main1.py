from machine import Pin
import time
from time import sleep
#dht11
import dht
#ADC
import machine
#UART
from machine import UART
import sys

sensor = dht.DHT11(Pin(14))
sensorADC = machine.ADC(machine.Pin(36))

led =Pin(17, Pin.OUT)
timeLastToggle = 0

#UART
uart = UART(1, 115200)

while True:

  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    sleep(2)
    
    print(sensorADC.read())
    sleep(0.5)
    
    if time.ticks_diff(time.ticks_ms(), timeLastToggle) > 100:
        led.value(not led.value())
        timeLastToggle = time.ticks_ms()

  except OSError as e:
    print('Failed to read sensor.')
  print("hello")
  try:
    uart.write("hello")
    sleep(1)
  except KeyboardInterrupt:
    print("Exit!")
    sys.exit()
