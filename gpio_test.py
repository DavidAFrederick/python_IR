from gpiozero import LED
from time import sleep

# GPIO 17 corresponds to BCM numbering
led = LED(17)

while True:
    led.on()
    print(f"GPIO On")
    sleep(1)
    led.off()
    print(f"GPIO Off")
    sleep(1)


#  export GPIOZERO_PIN_FACTORY=native
