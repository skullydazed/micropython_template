"""main.py

Hello, World!
"""
import time

from machine import Pin


if __name__ == '__main__':
    led = Pin(25, Pin.OUT)
    led.value(0)

    for i in range(10):
        led.toggle()
        print("BLINK!")
        time.sleep(1)

    print("Blinking complete. Exiting to REPL.")
