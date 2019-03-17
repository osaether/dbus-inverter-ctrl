# dbus-inverter-ctrl

This is a service for the Venus OS on the beaglebone
([Venus GX](https://www.victronenergy.com/panel-systems-remote-monitoring/venus-gx)),
though it may be applicable to other platforms as well. It montors digital input pin1
on the Venus GX and when it detects a falling edge it swithces the inverter on tty05
on or off depending on the state it was in.

# Running

Normally the service will be started by a daemontools run script. However, to run
it manually on, use this command:

    python dbus-inverter-ctrl.py
