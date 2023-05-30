from machine import Pin, ADC
from time import sleep

bat = ADC(Pin(34))
bat.atten(ADC.ATTN_11DB)
bat.width(ADC.WIDTH_12BIT)

while True:
   bat_val = bat.read()
   m_spaending = bat_val/4095*3.3
   print("Analog maalt vaerdi: ", m_spaending)
   spaending = m_spaending * 5
   print("Input spaending: ", spaending)
   sleep(1)
   
   
