from machine import UART
from time import sleep
import sys
from random import randint
uart = UART(1, 115200) # 1st argument: UART number: Hardware UART #1

# Read
#print(uart.read()) # Read as much as possible using

while True:
    randiddy = randint(0, 99)
    print(f"hello random number is: {str(randiddy)}")
    # Write
    try:
        uart.write(f"hello random number is: {str(randiddy)} \n")
        sleep(1)
    except KeyboardInterrupt:
        print("Exit!")
        sys.exit()
        
        
