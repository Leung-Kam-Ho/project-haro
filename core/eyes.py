from usb_relay_diustou import USB_RELAY
from sim

if __name__ == "__main__":
    relay = USB_RELAY()
    while True:
        relay.relay_on()  # Turn on the relay
        input("Press Enter to turn off the relay...")
        relay.relay_off()  # Turn off the relay
        input("Press Enter to turn on the relay...")