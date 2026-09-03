from usb_relay_diustou import USB_RELAY

if __name__ == "__main__":
    relay = USB_RELAY()
    relay.relay_on()  # Turn on the relay
    input("Press Enter to turn off the relay...")
    relay.relay_off()  # Turn off the relay