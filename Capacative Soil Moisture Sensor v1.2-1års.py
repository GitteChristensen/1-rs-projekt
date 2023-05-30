 

import machine 

from time import sleep 

  

sensor = machine.ADC(machine.Pin(36)) 

  
while True: 

   print(sensor.read()) 

   sleep(0.5) 
