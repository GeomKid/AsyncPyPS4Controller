# Hardware Connection

=== "BlueTooth Connection"
    === "First time Connection"
        1. Hold the Share Button.
        2. Hold the Playstation Button, the LED will blink rapidly.
        4. Open bluetooth Settings and add Device.
        5. When the device is connected the LED will remain turned on.
    === "Reconnect from last Usage"
        1. Hold the PlayStation Button
        2. The LED wil blink at a slower pace than first time connection
        3. When the device is connected the LED will remain turned on.
=== "Wired Connection"
    1. Use a USB to Micro USB to connect the PS4 to your device.
    2. The LED on the Controller will light up.

Check which interface it has been connected at `/dev/input` via `ls /dev/input/ | grep js` command in command line.

When you connect a new device, there should be a entry and it usually starts at `js0`. The more controllers/joysticks are connected the more `jsN` interfaces you will see.
???+ note
    Usually `js0`, `js1`, `js2` will have a Blue ,Red, Green LED respectively
