
import subprocess
from time import sleep

count = 0

def send_ir(protocol, scancode, filename=""):

    if filename == "":
        # Example: ir-ctl -S nec:0xbf10 -d /dev/lirc0
        cmd = ["sudo", "ir-ctl", "-S", f"{protocol}:{scancode}", "-d", "/dev/lirc0"]
        # print (f"Using command: {filename}")
    else:
        # Example: ir-ctl -d /dev/lirc0 --send=samsung_power_off.key
        #          ir-ctl -d /dev/lirc0 --send=samsung_power_on.key
        # cmd = ["sudo", "ir-ctl", "--send=", f"{filename}", "-d", "/dev/lirc0"]
        cmd = ["sudo", "ir-ctl", "--send="f"{filename}", "-d", "/dev/lirc0"]
        # print (f"Using file: {filename}   {cmd}")

        #  Capture using:   ir-ctl -d /dev/lirc1 --receive=samsung_power_on.key

    subprocess.run(cmd)

# Usage

while (True):
    count = count + 1
    send_ir("nec", "0x0044")   # Fireplace
    # send_ir("AA", "0x0000", "samsung_power_off.key")   # LED ON = IR_SMALLD_SAMSUNG  0xA3 0x5B 
    sleep (1)
    # send_ir("AA", "0x0000", "samsung_power_on.key")   # LED ON = IR_SMALLD_SAMSUNG  0xA3 0x5B 
    print (f"count: {count}")
    sleep (2)

#     send_ir("nec", "0x0044")
# print ("2")
# send_ir("nec", "0x0044")
# print ("3")
# #    sleep(2)


# Configuration information from RPI-Zero 131
#
# # Enable IR Receiver on GPIO 17
# dtoverlay=gpio-ir,gpio_pin=17
# # Enable IR Transmitter on GPIO 18
# dtoverlay=gpio-ir-tx,gpio_pin=18


# Supported Protocols in ir-ctlnec: Standard NEC protocol.necx: Extended NEC protocol.nec32: 32-bit NEC protocol.rc5: Philips RC5 protocol.rc5x_20: 20-bit extended RC5.rc5_sz: RC5 StreamZap variant.rc6_0: Philips RC6 Mode 0.rc6_6a_20: 20-bit RC6.rc6_6a_24: 24-bit RC6.rc6_6a_32: 32-bit RC6.rc6_mce: Microsoft Media Center Edition protocol.sony12: 12-bit Sony protocol.sony15: 15-bit Sony protocol.sony20: 20-bit Sony protocol.jvc: JVC protocol.sanyo: Sanyo protocol.sharp: Sharp protocol.imon: iMON protocol.rc_mm_12: RCMM 12-bit.rc_mm_24: RCMM 24-bit.rc_mm_32: RCMM 32-bit.


# Controlling Samsung with a file
# ir-ctl -d /dev/lirc0 --send=samsung_power_off.key
# ir-ctl -d /dev/lirc0 --send=samsung_power_on.key

# env) a@RPI3a:~/python_IR $ sudo ir-keytable -p all -t
# Protocols changed to unknown other lirc rc-5 rc-5-sz jvc sony nec sanyo mce_kbd rc-6 sharp xmp cec imon rc-mm 
# Loaded BPF protocol xbox-dvd
# Testing events. Please, press CTRL-C to abort.
# 1394.244059: lirc protocol(nec32): scancode = 0xb0a37e35
# 1394.244096: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1394.244096: event type EV_SYN(0x00).
# 1395.092054: lirc protocol(nec32): scancode = 0xb0a37e35
# 1395.092099: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1395.092099: event type EV_SYN(0x00).
# 1396.968043: lirc protocol(nec32): scancode = 0xb0a37e35
# 1396.968098: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1396.968098: event type EV_SYN(0x00).
# 1397.056051: lirc protocol(nec32): scancode = 0xb0a37e35
# 1397.056096: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1397.056096: event type EV_SYN(0x00).
# 1397.236044: lirc protocol(nec32): scancode = 0xb0a37e35
# 1397.236086: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1397.236086: event type EV_SYN(0x00).
# 1397.324062: lirc protocol(nec32): scancode = 0xb0a37e35
# 1397.324098: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1397.324098: event type EV_SYN(0x00).
# 1397.684046: lirc protocol(nec32): scancode = 0xb0a37e35
# 1397.684101: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1397.684101: event type EV_SYN(0x00).
# 1397.776043: lirc protocol(nec32): scancode = 0xb0a37e35
# 1397.776093: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1397.776093: event type EV_SYN(0x00).
# 1397.880050: lirc protocol(nec32): scancode = 0xb0a37e35
# 1397.880098: event type EV_MSC(0x04): scancode = 0xb0a37e35
# 1397.880098: event type EV_SYN(0x00).
# 1400.432036: lirc protocol(nec32): scancode = 0x80a396c5
# 1400.432067: event type EV_MSC(0x04): scancode = 0x80a396c5
# 1400.432067: event type EV_SYN(0x00).
# 1400.516117: lirc protocol(nec32): scancode = 0x80a396c5
# 1400.516143: event type EV_MSC(0x04): scancode = 0x80a396c5
# 1400.516143: event type EV_SYN(0x00).
# 1400.860038: lirc protocol(nec32): scancode = 0x80a396c5
# 1400.860068: event type EV_MSC(0x04): scancode = 0x80a396c5
# 1400.860068: event type EV_SYN(0x00).
# 1401.032056: lirc protocol(nec32): scancode = 0x80a396c5
# 1401.032099: event type EV_MSC(0x04): scancode = 0x80a396c5
# 1401.032099: event type EV_SYN(0x00).
# 1401.372042: lirc protocol(nec32): scancode = 0x80a396c5
# 1401.372080: event type EV_MSC(0x04): scancode = 0x80a396c5
# 1401.372080: event type EV_SYN(0x00).
# 1401.560043: lirc protocol(nec32): scancode = 0x80a396c5
# 1401.560077: event type EV_MSC(0x04): scancode = 0x80a396c5
# 1401.560077: event type EV_SYN(0x00).
# ^C
# (venv) a@RPI3a:~/python_IR $ 