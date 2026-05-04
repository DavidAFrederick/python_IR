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

