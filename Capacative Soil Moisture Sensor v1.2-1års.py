import machine
import time

# Set up ADC pin for analog input
adc_pin = machine.ADC(machine.Pin(34))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    # Read the analog value from the sensor
    sensor_value = adc_pin.read()

    # Map the sensor value to a moisture level (adjust according to your sensor and calibration)
    moisture_level = map_value(sensor_value, 0, 4095, 0, 100)

    # Print the moisture level
    print("Moisture Level: {:.2f}%".format(moisture_level))

    # Wait for some time before reading again
    time.sleep(1)
while True:
    # Read the analog value from the sensor
    sensor_value = adc_pin.read()

    # Map the sensor value to a moisture level (adjust according to your sensor and calibration)
    moisture_level = map(sensor_value, 0, 4095, 0, 100)

    # Print the moisture level
    print("Moisture Level: {:.2f}%".format(moisture_level))

    # Wait for some time before reading again
    sleep(1)
