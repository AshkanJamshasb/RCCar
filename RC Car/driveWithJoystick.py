import time
import RPi.GPIO as GPIO
import XboxController

xCon = XboxController.XboxController(
    controllerCallBack = None,
    joystickNo =0,
    deadzone = 0.25,
    scale = 1,
    invertYAxis = True)

mode = GPIO.getmode()

rMotorForward = 38
rMotorBackward = 37
lMotorForward = 35
lMotorBackward = 36

rVal = 0.0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(rMotorForward, GPIO.OUT)
GPIO.setup(rMotorBackward, GPIO.OUT)
GPIO.setup(lMotorForward, GPIO.OUT)
GPIO.setup(lMotorBackward, GPIO.OUT)

rForwardPWM = GPIO.PWM(rMotorForward, 100)
rBackwardPWM = GPIO.PWM(rMotorBackward, 100)
lForwardPWM = GPIO.PWM(lMotorForward, 100)
lBackwardPWM = GPIO.PWM(lMotorBackward, 100)
rForwardPWM.start(0)
rBackwardPWM.start(0)
lForwardPWM.start(0)
lBackwardPWM.start(0)


xCon.start()

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def tankDrive(leftStick, rightStick):
    #print 'lStick: ', leftStick, ' rStick: ', rightStick
    if(rightStick >= 0):
        if(rightStick >= 1):
            rVal = 100
        else:
            rVal = map(rightStick, 0.25, 1.00, 25, 100)
        rForwardPWM.ChangeDutyCycle(rVal)
        rBackwardPWM.ChangeDutyCycle(0)
    else:
        rVal = map(abs(rightStick), 0.25, 1.00, 25, 100)
        rForwardPWM.ChangeDutyCycle(0)
        rBackwardPWM.ChangeDutyCycle(rVal)
        
    if(leftStick >= 0):
        if(leftStick >= 1):
            lVal = 100
        else:
            lVal = map(leftStick, 0.25, 1.00, 25, 100)
        lForwardPWM.ChangeDutyCycle(lVal)
        lBackwardPWM.ChangeDutyCycle(0)
    else:
        lVal = map(abs(leftStick), 0.25, 1.00, 25, 100)
        lForwardPWM.ChangeDutyCycle(0)
        lBackwardPWM.ChangeDutyCycle(lVal)
    #print 'lVal: ', lVal, ' rVal: ', rVal

"""
def drive(joystick):
    if(joystick <= 1.001 and joystick >= -1.00):
        if(joystick >= 0):
            if(joystick > 1):
                rVal = 100
            else:
                rVal = map(joystick, 0.25, 1.00, 25, 100)
            rForwardPWM.ChangeDutyCycle(rVal)
            rBackwardPWM.ChangeDutyCycle(0)
            lForwardPWM.ChangeDutyCycle(rVal)
            lBackwardPWM.ChangeDutyCycle(0)
            #print 'Joystick: ', joystick, 'Forward: ', rVal
        else:
            rVal = map(abs(joystick), 0.25, 1.00, 25, 100)
            rForwardPWM.ChangeDutyCycle(0)
            rBackwardPWM.ChangeDutyCycle(rVal)
            lForwardPWM.ChangeDutyCycle(0)
            lBackwardPWM.ChangeDutyCycle(rVal)
            #print 'Joystick: ', joystick, 'Reverse: ', rVal        
    else:
        print 'Error :: Joystick: ', joystick

"""

"""
def turn(joystick):
    if(joystick <= 1.001 and joystick >= -1.00):
        if(joystick <= 0):
            if(joystick < -1):
                rVal = 100
            else:
                rVal = map(abs(joystick), 0.25, 1.00, 25, 100)
            rForwardPWM.ChangeDutyCycle(rVal)
            #rBackwardPWM.ChangeDutyCycle(0)
            #lForwardPWM.ChangeDutyCycle(0)
            lBackwardPWM.ChangeDutyCycle(rVal)
            #print 'Joystick: ', joystick, 'Forward: ', rVal
        else:
            rVal = map(abs(joystick), 0.25, 1.00, 25, 100)
            #rForwardPWM.ChangeDutyCycle(0)
            rBackwardPWM.ChangeDutyCycle(rVal)
            lForwardPWM.ChangeDutyCycle(rVal)
            #lBackwardPWM.ChangeDutyCycle(rVal)
            #print 'Joystick: ', joystick, 'Reverse: ', rVal        
    else:
        print 'Error :: Joystick: ', joystick

"""
        
try:
    while (1):
        #drive(xCon.LTHUMBY)
        #turn(xCon.LTHUMBX)
        #print(xCon.RTHUMBY)
        tankDrive(xCon.LTHUMBY, xCon.RTHUMBY)
except KeyboardInterrupt:
    pass
xCon.stop()
rForwardPWM.stop
rBackwardPWM.stop
