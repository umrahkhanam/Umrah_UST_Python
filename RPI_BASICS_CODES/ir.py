import RPi.GPIO as GPIO
import time
sensor = 3
led=5
buz=11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buz,GPIO.OUT)
while True:
    if GPIO.input(sensor):
        GPIO.output(led,GPIO.LOW)
        GPIO.output(buz,GPIO.LOW)
    else:
        GPIO.output(led,GPIO.HIGH)
        GPIO.output(buz,GPIO.HIGH)
        
    
