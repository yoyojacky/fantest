import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 1000)
pwm.start(0)
try:
    while True:
        for duty in range(0,101,1):
            pwm.ChangeDutyCycle(duty)
            sleep(0.1)
            print(duty)
        sleep(0.5)

        for duty in range(100, -1, -1):
            pwm.ChangeDutyCycle(duty)
            sleep(0.1)
            print(duty)
        sleep(0.5)
except KeyboardInterrupt:
    pwm.stop()
GPIO.cleanup(12)
