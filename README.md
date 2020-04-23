# dbus-inverter-ctrl

This is a service for the Venus OS on the beaglebone
([Venus GX](https://www.victronenergy.com/panel-systems-remote-monitoring/venus-gx)),
though it may be applicable to other platforms as well. It monitors digital input pin1
on the Venus GX and when it detects a falling edge it swithces the inverter on ttyO5
on or off depending on the state it was in.

# Installing

To install the service on your Venus device, copy one of the installers under [Releases](https://github.com/osaether/dbus-inverter-ctrl/releases)
in this repo to your device (I use wget for that). Log into your Venus device with SSH
and install it with opkg:

    opkg install dbus-inverter-ctrl_0.8-r0_cortexa8hf-neon.ipk

To install it on a Raspberri Pi use the file ```dbus-inverter-ctrl_0.8-r0_cortexa7hf-neon-vfpv4.ipk```

# Todo

- [ ] Automatic enumeration of Multiplus/inverters in the system
- [ ] Configurable input pin number
