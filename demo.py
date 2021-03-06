#!/usr/bin/python
# coding: utf-8


import sys
import signal
import RPi.GPIO as GPIO

from lib.ea_dog import DOG

def handler(sig, frame):
    print 'You pressed Ctrl+C, I\'m cleaning up GPIO...'
    GPIO.cleanup()
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, GPIO.cleanup)
    lcd = DOG(16, 18, 22, 26, 24)

    for i in range(8):
        data = 1
        for j in range(4):
            lcd.set_pos(i, 0)
            lcd.send_data_seq([data]*128)
            data += pow(4, j+1)
    for i in range(64):
        for j in range(8):
            lcd.set_pos(j, i*2)
            lcd.send_data_seq([ 0xFF, 0x00 ])
    lcd.clear_lcd()

    print 'Demo finished!'

    GPIO.cleanup()
