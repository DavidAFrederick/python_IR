import subprocess
from time import sleep

def send_ir(protocol, scancode):
    # Example: ir-ctl -S nec:0xbf10 -d /dev/lirc0
    cmd = ["sudo", "ir-ctl", "-S", f"{protocol}:{scancode}", "-d", "/dev/lirc0"]
    subprocess.run(cmd)

# Usage
while (True):
    send_ir("nec", "0xbf15")
    sleep(2)


# Configuration information from RPI-Zero 131
#
# # Enable IR Receiver on GPIO 17
# dtoverlay=gpio-ir,gpio_pin=17
# # Enable IR Transmitter on GPIO 18
# dtoverlay=gpio-ir-tx,gpio_pin=18
