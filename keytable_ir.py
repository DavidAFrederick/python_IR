import evdev
from evdev import InputDevice, categorize, ecodes

##################################################
# sudo apt-get install ir-keytable -y
#
# Test the Hardware: Run sudo ir-keytable -p all -t
#
# ir-ctl -f -d /dev/lirc0
# ir-ctl -f -d /dev/lirc1
##################################################

def get_ir_device():
    # List all input devices and find the one named 'gpio_ir_recv'
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if device.name == "gpio_ir_recv":
            return device
    return None

dev = get_ir_device()

if dev:
    print(f"Reading from {dev.name} at {dev.path}...")
    # Blocking loop to wait for IR events
    for event in dev.read_loop():
        # EV_MSC events contain the raw scancode from ir-keytable
        if event.type == ecodes.EV_MSC:
            print(f"Received Scancode: {hex(event.value)}")
        
        # EV_KEY events occur if you have a keymap loaded (mapping scancodes to keys)
        elif event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == key_event.key_down:
                print(f"Key Pressed: {key_event.keycode}")
else:
    print("IR receiver device not found. Check your dtoverlay settings.")





# Configuration information from RPI-Zero 131
#
# # Enable IR Receiver on GPIO 17
# dtoverlay=gpio-ir,gpio_pin=17
# # Enable IR Transmitter on GPIO 18
# dtoverlay=gpio-ir-tx,gpio_pin=18
