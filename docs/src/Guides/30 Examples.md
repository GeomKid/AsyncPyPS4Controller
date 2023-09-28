# Examples
## `main.py`

```python
import asyncio
from AsynchronousPS4Controller import Controller

controller = Controller(path="/dev/input/js0")

# you can start listening before controller is paired, as long as you pair it within the timeout window
asyncio.run(controller.listen(timeout=30))
```

## `custom_controller.py`
This code shows how you can have your customize what each button press or Joystick movement invokes
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

    async def on_L3_up(self,value:int):
        print(f"Left Joystick has been pushed up by a value of {value}")

    async def on_L3_down(self,value:int):
        print(f"Left Joystick has been pushed down by a value of {value}")

controller = MyController(path="/dev/input/js0")

# you can start listening before controller is paired, as long as you pair it within the timeout window
asyncio.run(controller.listen(timeout=30))
```
## `custom_event_callback.py`

```python
import asyncio
from AsynchronousPS4Controller import Controller

def on_connect():
    print("I just connected")

def on_disconnect():
    print("I just disconnected")

def on_timeout():
    print("Timeout for waiting this controller")

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)


controller = MyController(interface="/dev/input/js0")
asyncio.run(
    controller.listen(timeout=30,connect_callback=on_connect, disconnect_callback=on_disconnect,timeout_callback=on_timeout
    )
)
```

## `dual_controller.py`
```python
import asyncio
from AsynchronousPS4Controller import Controller

class MyController(Controller):

    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    async def on_x_press(self):
        print("Hello")

    async def on_x_release(self):
        print("Goodbye")

class MyController2(Controller):
    def __init__(self, **kwargs):
        super().__init__(self, **kwargs)

    async def on_x_press(self):
            print("2nd Controller X Press")

    async def on_x_release(self):
            print("2nd Controller X Release")

controller1 = MyController(path="/dev/input/js0",re_listen=True)
controller2 = MyController2(path="/dev/input/js1",re_listen=True)

loop = asyncio.get_event_loop()
task_1= loop.create_task(controller1.listen())
task_2= loop.create_task(controller2.listen())
gathered = asyncio.gather(task_1,task_2)
loop.run_until_complete(gathered)
```
