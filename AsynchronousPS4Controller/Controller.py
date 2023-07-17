import asyncio
import os
import struct
from typing import Callable

import aiofiles
from .Mapping import PS4Mapping

max_PS4_value = 32767
__all__ = ["Controller"]


class BaseController:
    """
    Base Controller class for Controllers
    """

    def __init__(self):
        return

    async def on_x_press(self):
        """
        Function that is runned when x button is pressed
        """
        print("on_x_press")

    async def on_x_release(self):
        """
        Function that is runned when x button is released
        """
        print("on_x_release")

    async def on_triangle_press(self):
        """
        Function that is runned when triangle button is pressed
        """
        print("on_triangle_press")

    async def on_triangle_release(self):
        """
        Function that is runned when triangle button is released
        """
        print("on_triangle_release")

    async def on_circle_press(self):
        """
        Function that is runned when circle button is pressed
        """
        print("on_circle_press")

    async def on_circle_release(self):
        """
        Function that is runned when circle button is released
        """
        print("on_circle_release")

    async def on_square_press(self):
        """
        Function that is runned when square button is pressed
        """
        print("on_square_press")

    async def on_square_release(self):
        """
        Function that is runned when square button is released
        """
        print("on_square_release")

    async def on_L1_press(self):
        """
        Function that is runned when L1 button is pressed
        """
        print("on_L1_press")

    async def on_L1_release(self):
        """
        Function that is runned when L1 button is released
        """
        print("on_L1_release")

    async def on_L2_press(self, value):
        """
        Function that is runned when L2 button is released

        Args:
            value: The analog value of how hard the button is pressed.
        """
        print(f"on_L2_press: {value}")

    async def on_L2_release(self):
        """
        Function that is runned when L2 button is released
        """
        print("on_L2_release")

    async def on_R1_press(self):
        """
        Function that is runned when R1 button is pressed
        """
        print("on_R1_press")

    async def on_R1_release(self):
        """
        Function that is runned when R1 button is released
        """
        print("on_R1_release")

    async def on_R2_press(self, value):
        """
        Function that is runned when R2 button is released

        Args:
            value: The analog value of how hard the button is pressed.
        """
        print(f"on_R2_press: {value}")

    async def on_R2_release(self):
        """
        Function that is runned when R2 button is released
        """
        print("on_R2_release")

    async def on_up_arrow_press(self):
        """
        Function that is runned when Up button is pressed
        """
        print("on_up_arrow_press")

    async def on_down_arrow_press(self):
        """
        Function that is runned when Down button is pressed
        """
        print("on_down_arrow_press")

    async def on_up_down_arrow_release(self):
        """
        Function that is runned when Up or Down arrow button is released
        """
        print("on_up_down_arrow_release")

    async def on_left_arrow_press(self):
        """
        Function that is runned when Left arrow button is pressed
        """
        print("on_left_arrow_press")

    async def on_right_arrow_press(self):
        """
        Function that is runned when Right button is pressed
        """
        print("on_right_arrow_press")

    async def on_left_right_arrow_release(self):
        """
        Function that is runned when button is released
        """
        print("on_left_right_arrow_release")

    async def on_L3_up(self, value):
        """
        Function that is runned when Left Joystick (L3) is pushed up

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_L3_up: {value}")

    async def on_L3_down(self, value):
        """
        Function that is runned when Left Joystick (L3) is pushed down

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_L3_down: {value}")

    async def on_L3_left(self, value):
        """
        Function that is runned when Left Joystick (L3) is pushed left

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_L3_left: {value}")

    async def on_L3_right(self, value):
        """
        Function that is runned when Left Joystick (L3) is pushed right

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_L3_right: {value}")

    async def on_L3_y_at_rest(self):
        """
        Function that is runned when Left Joystick (L3) returns to the y-axis
        """
        print("on_L3_y_at_rest")

    async def on_L3_x_at_rest(self):
        """
        Function that is runned when Left Joystick (L3) returns to the x-axis
        """
        print("on_L3_x_at_rest")

    async def on_L3_press(self):
        """
        Function that is runned when Left Joystick (L3) button is pressed
        """
        print("on_L3_press")

    async def on_L3_release(self):
        """
        Function that is runned when Left Joystick (L3) button is released
        """
        print("on_L3_release")

    async def on_R3_up(self, value):
        """
        Function that is runned when Right Joystick (R3) is pushed up

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_R3_up: {value}")

    async def on_R3_down(self, value):
        """
        Function that is runned when Right Joystick (R3) is pushed down

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_R3_down: {value}")

    async def on_R3_left(self, value):
        """
        Function that is runned when Right Joystick (R3) is pushed left

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_R3_left: {value}")

    async def on_R3_right(self, value):
        """
        Function that is runned when Right Joystick (R3) is pushed right

        Args:
            value: The analog value of joystick that is pushed away from origin
        """
        print(f"on_R3_right: {value}")

    async def on_R3_y_at_rest(self):
        """
        Function that is runned when Right Joystick (R3) returns to the y-axis
        """
        print("on_R3_y_at_rest")

    async def on_R3_x_at_rest(self):
        """
        Function that is runned when Right Joystick (R3) returns to the x-axis
        """
        print("on_R3_x_at_rest")

    async def on_R3_press(self):
        """
        Function that is runned when Right Joystick (R3) button is pressed
        """
        print("on_R3_press")

    async def on_R3_release(self):
        """
        Function that is runned when Right Joystick (R3) button is released
        """
        print("on_R3_release")

    async def on_options_press(self):
        """
        Function that is runned when Options button is pressed
        """
        print("on_options_press")

    async def on_options_release(self):
        """
        Function that is runned when Options button is released
        """
        print("on_options_release")

    async def on_share_press(self):
        """
        Function that is runned when share button is pressed
        """
        print("on_share_press")

    async def on_share_release(self):
        """
        Function that is runned when share button is released
        """
        print("on_share_release")

    async def on_playstation_button_press(self):
        """
        Function that is runned when playstation button is pressed
        """
        print("on_playstation_button_press")

    async def on_playstation_button_release(self):
        """
        Function that is runned when playstation button is released
        """
        print("on_playstation_button_release")


class Controller(BaseController):
    def __init__(
        self,
        path: str,
        debug=False,
        re_listen: bool = False,
    ):
        """
        Initiate controller instance that is capable of listening to all events on specified input path

        Args:
            path: The path of where your PS4 is connected to (IE `/dev/input/js0`)
            debug: Enable Debug mode to print out some info
            re_listen: Will the joystick relisten after disconnect
        """
        BaseController.__init__(self)
        self.is_connected: bool = False
        self.path = path
        self.debug = debug
        self.re_listen = re_listen
        self.event_mapping = PS4Mapping
        self.event_format = "3Bh2b"
        self.event_size = struct.calcsize(self.event_format)
        self._file = None

    async def connnection_check(
        self,
        timeout: int = 30,
        connect_callback: Callable = None,
        timeout_callback: Callable = None,
    ):
        """
        Function to check for connection
        Exits with exit code 1 when timeout unless `self.re_listen = True`
        Args:
            timeout: The time you want to wait for connection
            connect_callback: User defined function to be runned when PS4 is connected
            timeout_callback: User defined function to be runned when connection timeout
        """

        def on_connect_callback():
            self.is_connected = True
            if connect_callback is not None:
                connect_callback()

        def on_timeout_callback():
            print(f"Timeout({timeout} sec). Interface not available.")
            if timeout_callback is not None:
                timeout_callback()

        print(f"Waiting for path: {self.path} to become available . . .")
        seconds_past = 0
        while seconds_past < timeout:
            if os.path.exists(self.path):
                print(f"Successfully bound to: {self.path}.")
                on_connect_callback()
                return
            seconds_past += 1
            await asyncio.sleep(1)
        on_timeout_callback()
        if not self.re_listen:
            exit(1)

    async def listen(
        self,
        timeout=30,
        connect_callback=None,
        disconnect_callback=None,
        timeout_callback: Callable = None,
        re_listen: bool = False,
    ):
        """
        Start listening for events on a given `self.path`
        Exits with exit code 1 when timeout unless `self.re_listen = True`

        Args:
            timeout: The time you want to wait for connection.This allows you to start listening and connect your controller after running the script.
            connect_callback: User defined function to be runned when PS4 is connected
            disconnect_callback: User defined function to be runned when PS4 when connection is lost
            timeout_callback: User defined function to be runned when connection timeout
            re_listen: Will the joystick relisten after disconnect
        """
        self.re_listen = self.re_listen or re_listen

        def on_disconnect_callback():
            self.is_connected = False
            if disconnect_callback is not None:
                disconnect_callback()

        def unpack():
            __event = struct.unpack(self.event_format, event)
            return (__event[:3], __event[3], __event[4], __event[5])

        await self.connnection_check(
            timeout=timeout, connect_callback=connect_callback, timeout_callback=timeout_callback
        )
        if self.re_listen:
            await self.re_connect()
        try:
            self._file = await aiofiles.open(self.path, "rb")
            event = await self.read_events()
            while event:
                (header, value, button_type, button_id) = unpack()
                self.__handle_event(
                    button_id=button_id,
                    button_type=button_type,
                    value=value,
                    header=header,
                )
                await asyncio.sleep(0.01)
                event = await self.read_events()
        except KeyboardInterrupt:
            print("\nExiting (Ctrl + C)")
            on_disconnect_callback()

    async def re_connect(
        self,
        connect_callback=None,
    ):
        """
        Reconnect to the `self.path` given
        Args:
            connect_callback: User defined function to be runned when PS4 is connected
        """

        def on_connect_callback():
            self.is_connected = True
            if connect_callback is not None:
                connect_callback()

        print(f"Reconnecting to {self.path}")
        while self.re_listen:
            if os.path.exists(self.path):
                print(f"Successfully reconnected to: {self.path}.")
                on_connect_callback()
                self._file = await aiofiles.open(self.path, "rb")
                return
            await asyncio.sleep(0.5)

    def __handle_event(self, button_id, button_type, value, header):
        """
        Handles the event of buttons

        Args:
            button_id: ID of the button
            button_type: Type of button
            value: Analog value of button
            header: The extra bytes of teh packet from joystick
        """
        event = self.event_mapping(
            button_id=button_id,
            button_type=button_type,
            value=value,
            header=header,
            debug=self.debug,
        )
        loop = asyncio.get_event_loop()
        if event.R3_event():
            if event.R3_y_at_rest():
                loop.create_task(self.on_R3_y_at_rest())
            if event.R3_x_at_rest():
                loop.create_task(self.on_R3_x_at_rest())
            if event.R3_right():
                loop.create_task(self.on_R3_right(event.value))
            if event.R3_left():
                loop.create_task(self.on_R3_left(event.value))
            if event.R3_up():
                loop.create_task(self.on_R3_up(event.value))
            if event.R3_down():
                loop.create_task(self.on_R3_down(event.value))
        if event.L3_event():
            if event.L3_y_at_rest():
                loop.create_task(self.on_L3_y_at_rest())
            if event.L3_x_at_rest():
                loop.create_task(self.on_L3_x_at_rest())
            if event.L3_up():
                loop.create_task(self.on_L3_up(event.value))
            if event.L3_down():
                loop.create_task(self.on_L3_down(event.value))
            if event.L3_left():
                loop.create_task(self.on_L3_left(event.value))
            if event.L3_right():
                loop.create_task(self.on_L3_right(event.value))
        if event.circle_pressed():
            loop.create_task(self.on_circle_press())
        if event.circle_released():
            loop.create_task(self.on_circle_release())
        if event.x_pressed():
            loop.create_task(self.on_x_press())
        if event.x_released():
            loop.create_task(self.on_x_release())
        if event.triangle_pressed():
            loop.create_task(self.on_triangle_press())
        if event.triangle_released():
            loop.create_task(self.on_triangle_release())
        if event.square_pressed():
            loop.create_task(self.on_square_press())
        if event.square_released():
            loop.create_task(self.on_square_release())
        if event.L1_pressed():
            loop.create_task(self.on_L1_press())
        if event.L1_released():
            loop.create_task(self.on_L1_release())
        if event.L2_pressed():
            loop.create_task(self.on_L2_press(event.value))
        if event.L2_released():
            loop.create_task(self.on_L2_release())
        if event.R1_pressed():
            loop.create_task(self.on_R1_press())
        if event.R1_released():
            loop.create_task(self.on_R1_release())
        if event.R2_pressed():
            loop.create_task(self.on_R2_press(event.value))
        if event.R2_released():
            loop.create_task(self.on_R2_release())
        if event.options_pressed():
            loop.create_task(self.on_options_press())
        if event.options_released():
            loop.create_task(self.on_options_release())
        if event.left_right_arrow_released():
            loop.create_task(self.on_left_right_arrow_release())
        if event.up_down_arrow_released():
            loop.create_task(self.on_up_down_arrow_release())
        if event.left_arrow_pressed():
            loop.create_task(self.on_left_arrow_press())
        if event.right_arrow_pressed():
            loop.create_task(self.on_right_arrow_press())
        if event.up_arrow_pressed():
            loop.create_task(self.on_up_arrow_press())
        if event.down_arrow_pressed():
            loop.create_task(self.on_down_arrow_press())
        if event.playstation_button_pressed():
            loop.create_task(self.on_playstation_button_press())
        if event.playstation_button_released():
            loop.create_task(self.on_playstation_button_release())
        if event.share_pressed():
            loop.create_task(self.on_share_press())
        if event.share_released():
            loop.create_task(self.on_share_release())
        if event.R3_pressed():
            loop.create_task(self.on_R3_press())
        if event.R3_released():
            loop.create_task(self.on_R3_release())
        if event.L3_pressed():
            loop.create_task(self.on_L3_press())
        if event.L3_released():
            loop.create_task(self.on_L3_release())

    async def read_events(self):
        """
        The loop function to read for events
        """
        try:
            return await self._file.read(self.event_size)
        except IOError:
            print("Interface lost. Device disconnected?")
            if self.re_listen:
                await self.re_connect()
                return await self.read_events()
            exit(1)
