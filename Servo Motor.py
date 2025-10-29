# Servo motor = 180 degrees
# 20ms = PWM
#1ms On + 19ms Off = -90 degrees
#2ms On + 18ms Off = +90 degrees
#1.5ms On + 18.5ms Off = 0 degrees

# freq = 1 / T = 1 / 20ms = 50Hz

import machine
import time

servo = machine.Pin(16,machine.Pin.OUT)

pwm = machine.PWM(servo)

pwm.freq(50)

while True:
    #pwm.duty_u16(4915)  # 0 degrees
    #pwm.duty_u16(1639)  # -90 degrees
    #pwm.duty_u16(8192)  # +90 degrees
    for i in range(1639,8192,1):
        pwm.duty_u16(i)
        time.sleep(0.001)
    for i in range(8192,1639,-1):
        pwm.duty_u16(i)
        time.sleep(0.001)