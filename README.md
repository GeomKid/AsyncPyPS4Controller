<div align="center">

   # AsynchronousPS4Controller
   <br>

   ![](https://img.shields.io/pypi/v/AsynchronousPS4Controller.svg?label=Version&logo=pypi)
   ![](https://img.shields.io/badge/Python-3.9+-1081c1?logo=python)
   [![](https://img.shields.io/pypi/dm/AsynchronousPS4Controller.svg?logo=python&label=Downloads)](https://pypi.org/project/AsynchronousPS4Controller/)

   [![License](https://img.shields.io/badge/License-GPL-blue)](https://github.com/GeomKid/AsyncPyPS4Controller/blob/master/LICENSE)
   [![](https://img.shields.io/badge/Docs-latest-x?logo=readthedocs)](https://geomkid.github.io/AsyncPyPS4Controller/)

</div>

# About
A package to suit your non-blocking PS4 interface

# Installation
Depend on your preference you can install this package using either one of these commands
```
python -m pip install AsynchronousPS4Controller
python3 -m pip install AsynchronousPS4Controller
pip install AsynchronousPS4Controller
pip3 install AsynchronousPS4Controller
```

# Usage
1. Connect your controller to Bluetooth.
For the first time connecting, Hold the share button, then hold the PlayStation Button. The lights on the controller will blink rapidly. Open your bluetooth settings to add the device.
2. Check which interfaces you have available at `/dev/input` via `ls /dev/input/ | grep js` command.
The terminal will list all input paths that starts with `js`.
When you connect a new device, there should be a entry and it usually starts at `js0`. The more controllers/joysticks are connected the more `jsN` interfaces you will see.
So if you have only one controller/joystick connected, you should only see 1 interface: `/dev/input/js0`,
take a note of it as we will need it in next step.
3. Copy the code below into a Python file, lets say `main.py`
    ```python
        import asyncio
        from AsynchronousPS4Controller import Controller

        controller = Controller(path="/dev/input/js0")

        # you can start listening before controller is paired, as long as you pair it within the timeout window
        asyncio.run(controller.listen(timeout=30))
    ```
4. Now run that file like so `python main.py` and use your controller.
You will see output on your screen based on the input to your controller.
You can bind your own logic to each one of those events.
Lets say you want print "Hello world" on X press and "Goodbye world" on X release then the code would look like this:
```python
import asyncio
from AsynchronousPS4Controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    async def on_x_press(self):
        print("Hello world")

    async def on_x_release(self):
        print("Goodbye world")


controller = MyController(path="/dev/input/js0")

# you can start listening before controller is paired, as long as you pair it within the timeout window
asyncio.run(controller.listen(timeout=30))
```

# Registering Callbacks
It is possible to bound callbacks to the `listen` function.
Three call back functions can be registered: `on_connect` , `on_disconnect` and `on_timeout`
Here is an example how to do it.
```python
import asyncio
from AsynchronousPS4Controller import Controller

def connect():
    # any code you want to run during initial connection with the controller
    pass

def disconnect():
    # any code you want to run during loss of connection with the controller or keyboard interrupt
    pass

def timeout():
    # any code you want to run during timeout of controller before exit with code 1
    pass

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


controller = MyController(interface="/dev/input/js0")
asyncio.run(controller.listen(timeout=30,connect_callback=connect, disconnect_callback=disconnect,timeout_callback=timeout))
```

# Known limitations at this time
- Mouse pad events and clicks are not detected (This is due to it works through `/dev/input/mouseN` or `/dev/input/mice` and uses a different way to unpack)
- Sensor information (accelerometers and/or gyro) is not detected (This is due to it works through `/dev/input/eventN` and uses a different way to unpack)
