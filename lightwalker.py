from gpiozero import LED
import time

ledPinsNumbers  = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]
leds = []

# Create LED objects reffering to each # in the the PinsNumbers list
def setup():
    for ledPin in ledPinsNumbers:
        led = LED(ledPin)
        led.off()
        leds.append(led)

def loop():
    for led in leds:
        led.on()
        time.sleep(0.1)
        led.off()
    for led in leds[::-1]:
        led.on()
        time.sleep(0.1)
        led.off()



if __name__ == '__main__': # Program entrance
    print('Program is starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Exit program")
        exit()