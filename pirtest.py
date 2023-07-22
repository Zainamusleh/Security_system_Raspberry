from gpiozero import MotionSensor
from gpiozero import LED
from gpiozero import Buzzer
from time import sleep
pir = MotionSensor(4)
led = LED(3)
buzzer= Buzzer(14)

while True:
    if pir.wait_for_motion():
        print("moved")
        led.on()
        buzzer.on()
        
    
    if pir.wait_for_no_motion():
        print("No motion")
        led.off()
        buzzer.off()