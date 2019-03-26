import RPi.GPIO as GPIO #bring in the library
import time #bring in the time library
GPIO.setmode(GPIO.BCM) #setup the pin naming convention
GPIO.setwarnings(False) #give me warnings
GPIO.setup(23,GPIO.OUT) #left button
GPIO.setup(24,GPIO.OUT) #right button
print "SPIN COUNTER CLOCKWISE"
GPIO.output(23,GPIO.HIGH) #power left button
time.sleep(2) #do this for 2 seconds
GPIO.output(23,GPIO.LOW)
time.sleep(2) #wait two seconds
print "SPIN CLOCKWISE"
GPIO.output(24,GPIO.HIGH) #push right botton
time.sleep(2) #rotates 2 seconds
GPIO.output(24,GPIO.LOW)
