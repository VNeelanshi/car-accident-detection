import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
Motor1A = 02
Motor1B = 03
Motor1E = 04

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(17, GPIO.IN) 
pwm = GPIO.PWM(Motor1E,100)


CLOCKWISE = True
ANTICLOCKWISE = False
dir = CLOCKWISE

def clock():
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)

def anticlock():
	GPIO.output(Motor1A,GPIO.LOW) 
        GPIO.output(Motor1B,GPIO.HIGH) 
        GPIO.output(Motor1E,GPIO.HIGH)

def start():
	GPIO.setmode(GPIO.BCM)
	if(dir==CLOCKWISE):
		pwm.start(25)
		GPIO.output(Motor1A,GPIO.LOW) 
        	GPIO.output(Motor1B,GPIO.HIGH)
	else:
		pwm.start(23)
		GPIO.output(Motor1A,GPIO.HIGH)
                GPIO.output(Motor1B,GPIO.LOW)	
        GPIO.output(Motor1E,GPIO.HIGH)

def stop():
	GPIO.output(Motor1E,GPIO.LOW) # to stop the motor
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.HIGH)
	#GPIO.cleanup()

def toggle():
	global dir
	if(dir==CLOCKWISE):
		dir=ANTICLOCKWISE
		GPIO.output(Motor1A,GPIO.LOW)
	       	GPIO.output(Motor1B,GPIO.HIGH)
	else:
		dir=CLOCKWISE
                GPIO.output(Motor1A,GPIO.HIGH)
                GPIO.output(Motor1B,GPIO.LOW)
		

def mad():
	for i in xrange(1,10):
		toggle()
		sleep(0.5)
