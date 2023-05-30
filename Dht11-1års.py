from machine import Pin

from time import sleep

import dht 

sensor = dht.DHT11(Pin(14))


while True:

  try:

    sensor.measure()

    temp = sensor.temperature()

    hum = sensor.humidity()

    print('Temperature: %3.1f C' %temp)

    print('Humidity: %3.1f %%' %hum)

    sleep(2)

  except OSError as e:

    print('Failed to read sensor.')