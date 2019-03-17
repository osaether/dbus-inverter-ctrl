#!/usr/bin/python -u

from functools import partial
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject

def track(conn, value):
    currval = int(conn.get_object("com.victronenergy.vebus.ttyO5",
            "/Mode").GetValue())
    newval = 3 if currval==4 else 4
    if int(value["Value"])==3:
        conn.get_object("com.victronenergy.vebus.ttyO5",
            "/Mode").SetValue(newval)

def main():
    DBusGMainLoop(set_as_default=True)
    conn = dbus.SystemBus()

    conn.add_signal_receiver(partial(track, conn),
            dbus_interface='com.victronenergy.BusItem',
            signal_name='PropertiesChanged',
            path="/State",
            bus_name="com.victronenergy.digitalinput.input01")

    gobject.MainLoop().run()


if __name__ == "__main__":
    main()