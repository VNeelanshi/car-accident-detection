import os, RPi.GPIO as GPIO
import motorFunctions as mf
import time
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(17, GPIO.IN)         #Read output from PIR motion sensor
counter = 0
name = "image"
while True:
       i=GPIO.input(17)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             time.sleep(0.1)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             #GPIO.output(35, 1)  #Turn ON LED
	     for j in range(0,8):
	     	print "Image  "	,j
		if j==1:
			mf.toggle();
		if j==4:
			mf.toggle();
		if j==7:
			mf.toggle();		
		mf.start();			
             	time.sleep(0.4)
             	mf.stop();
		time.sleep(0.5)
             	if(os.fork()==0):
                 	os.execvp("fswebcam",["fswebcam",name+str(j)]);
             	os.wait();
             	time.sleep(0.3);
	     break;
