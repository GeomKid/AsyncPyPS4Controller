# Custom Controller Callbacks

This library is usually used by overwriting the button and Joystick callbacks
???+ note
    The joysticks are called L3 and R3 based on PS4 own convention.

???+ note
    Analog Button Events are those Joystick moving, L2 press, R2 press events.

## Setup
Overwriting usually uses the concept of inheritance.
For example, this is a valid way of setting up:

```python
import asyncio
from AsynchronousPS4Controller import Controller

class MyController(Controller):
     def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
```
## Overwriting Digital Button Events
You probably want your program to do more than that.
For example, you want your program to print `Hello world` and `Goodbye World` when the `X` button is pressed and released respectively. The code look like this:
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
asyncio.run(controller.listen(timeout=30))
```
???+ note
    The Joysticks are Buttons. You can press them and invoke some certain events.
For Example, you are making an object move in your UI with the direction keys you can make it work like this:
```python
import asyncio
from AsynchronousPS4Controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    async def on_up_arrow_press(self):
        # Some function of your UI to move up
        UI_move_up()

    async def on_up_down_arrow_release(self):
        # Some function of your UI to stop moving
        UI_stop_move()


    async def on_down_arrow_press(self):
        # Some function of your UI to move down
        UI_move_down()

controller = MyController(path="/dev/input/js0")
asyncio.run(controller.listen(timeout=30))
```
???+ note
    The arrow buttons comes in pairs when it is untriggered it is unable to be differentiated. So the callbacks are `on_up_down_arrow_release` and `on_left_right_arrow_release` respectively.
### List of Digital Button Events
- `on_x_press`
- `on_x_release`
- `on_triangle_press`
- `on_triangle_release`
- `on_circle_press`
- `on_circle_release`
- `on_square_press`
- `on_square_release`
- `on_L1_press`
- `on_L1_release`
- `on_L2_release`
- `on_R1_press`
- `on_R1_release`
- `on_R2_release`
- `on_up_arrow_press`
- `on_up_down_arrow_release`
- `on_down_arrow_press`
- `on_left_arrow_press`
- `on_left_right_arrow_release`
- `on_right_arrow_press`
- `on_L3_x_at_rest`
- `on_L3_y_at_rest`
- `on_L3_press`
- `on_L3_release`
- `on_R3_x_at_rest`
- `on_R3_y_at_rest`
- `on_R3_press`
- `on_R3_release`
- `on_options_press`
- `on_options_release`
- `on_share_press`
- `on_share_release`
- `on_playstation_button_press`
- `on_playstation_button_release`
## Overwriting Analog Events
Overwriting Analog events is similar to how Digital Button Events. They just need an extra argument. For example:
```python
import asyncio
from AsynchronousPS4Controller import Controller

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    async def on_L3_up(self,value:int):
        print(f"Left Joystick has been pushed up by a value of {value}")

    async def on_L3_down(self,value:int):
        print(f"Left Joystick has been pushed down by a value of {value}")

controller = MyController(path="/dev/input/js0")
asyncio.run(controller.listen(timeout=30))
```

### List of analog events
- `on_L2_press`
- `on_R2_press`
- `on_L3_up`
- `on_L3_down`
- `on_L3_left`
- `on_L3_right`
- `on_R3_up`
- `on_R3_down`
- `on_R3_left`
- `on_R3_right`
