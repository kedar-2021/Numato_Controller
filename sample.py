# Defaults to port /dev/ttyACM0
from numato.numato_controller import numato_controller

device = numato_controller()

print(device.get_relay_state(3))  # Retrieve state of relay index 0
#<RelayState.RELAY_OFF: (0, 'off')>

device.turn_on_relay(3)  # Turn on relay index 0

print(device.get_relay_state(3))
#RelayState.RELAY_ON: (1, 'on')
