__all__ = ["PS4Mapping"]


class PS4Mapping:
    def __init__(self, button_id, button_type, value, header, debug=False):
        """
        For 3Bh2b format, all the data that can distinguish buttons in in the header tuple

        Args:
            button_id: Just a placeholder in the signature
            button_type: Just a placeholder in the signature
            value:  Just a placeholder in the signature
            header: The
            debug: Whether the controller in debug mode
        """
        self.button_id = button_id
        self.button_type = button_type
        self.value = value
        self.header = header
        if debug:
            print(
                f"button_id: {self.button_id} button_type: {self.button_type} value: {self.value} header: {self.header}"
            )

    """Left joystick """

    def L3_event(self):
        """
        Checks if Left Left have any events
        """
        return self.button_type == 2 and self.button_id in [1, 0]

    def L3_y_at_rest(self):
        """
        Checks if Left Left reurns to y-axis
        """
        return self.button_id in [1] and self.value == 0

    def L3_x_at_rest(self):
        """
        Checks if Left Left reurns to x-axis
        """
        return self.button_id in [0] and self.value == 0

    def L3_up(self):
        """
        Checks if the Left joystick is pushed to the up
        """
        return self.button_id == 1 and self.value < 0

    def L3_down(self):
        """
        Checks if the Left joystick is pushed to the down
        """
        return self.button_id == 1 and self.value > 0

    def L3_left(self):
        """
        Checks if the Left joystick is pushed to the left
        """
        return self.button_id == 0 and self.value < 0

    def L3_right(self):
        """
        Checks if the Left joystick is pushed to the right
        """
        return self.button_id == 0 and self.value > 0

    def L3_pressed(self):
        """
        Checks if the Left joystick button is pressed
        """
        return self.button_id == 11 and self.button_type == 1 and self.value == 1

    def L3_released(self):
        """
        Checks if the Left joystick button is released
        """
        return self.button_id == 11 and self.button_type == 1 and self.value == 0

    """Right joystick"""

    def R3_event(self):
        """
        Checks if Right Joystick have any events
        """
        return self.button_type == 2 and self.button_id in [4, 3]

    def R3_y_at_rest(self):
        """
        Checks if Right Joystick reurns to y-axis
        """
        return self.button_id in [4] and self.value == 0

    def R3_x_at_rest(self):
        """
        Checks if Right Joystick reurns to x-axis
        """
        return self.button_id in [3] and self.value == 0

    def R3_up(self):
        """
        Checks if Right left joystick is pushed to the up
        """
        return self.button_id == 4 and self.value < 0

    def R3_down(self):
        """
        Checks if Right left joystick is pushed to the down
        """
        return self.button_id == 4 and self.value > 0

    def R3_left(self):
        """
        Checks if Right left joystick is pushed to the left
        """
        return self.button_id == 3 and self.value < 0

    def R3_right(self):
        """
        Checks if Right left joystick is pushed to the right
        """
        return self.button_id == 3 and self.value > 0

    def R3_pressed(self):
        """
        Checks if Right left joystick button is pressed
        """
        return self.button_id == 12 and self.button_type == 1 and self.value == 1

    def R3_released(self):
        """
        Checks if Right left joystick button is released
        """
        return self.button_id == 12 and self.button_type == 1 and self.value == 0

    """Symbol Buttons"""

    def circle_pressed(self):
        """
        Checks if circle have just been pressed
        """
        return self.button_id == 1 and self.button_type == 1 and self.value == 1

    def circle_released(self):
        """
        Checks if circle have just released
        """
        return self.button_id == 1 and self.button_type == 1 and self.value == 0

    def x_pressed(self):
        """
        Checks if x have just been pressed
        """
        return self.button_id == 0 and self.button_type == 1 and self.value == 1

    def x_released(self):
        """
        Checks if x have just been released
        """
        return self.button_id == 0 and self.button_type == 1 and self.value == 0

    def triangle_pressed(self):
        """
        Checks if triangle have just been pressed
        """
        return self.button_id == 2 and self.button_type == 1 and self.value == 1

    def triangle_released(self):
        """
        Checks if triangle have just been released
        """
        return self.button_id == 2 and self.button_type == 1 and self.value == 0

    def square_pressed(self):
        """
        Checks if square have just been pressed
        """
        return self.button_id == 3 and self.button_type == 1 and self.value == 1

    def square_released(self):
        """
        Checks if square have just been released
        """
        return self.button_id == 3 and self.button_type == 1 and self.value == 0

    def options_pressed(self):
        """
        Checks if options have just been pressed
        """
        return self.button_id == 9 and self.button_type == 1 and self.value == 1

    def options_released(self):
        """
        Checks if options have just been released
        """
        return self.button_id == 9 and self.button_type == 1 and self.value == 0

    def share_pressed(self):
        """
        Checks if share button have just been pressed
        """
        return self.button_id == 8 and self.button_type == 1 and self.value == 1

    def share_released(self):
        """
        Checks if share button have just been released
        """
        return self.button_id == 8 and self.button_type == 1 and self.value == 0

    def L1_pressed(self):
        """
        Checks if L1 have just been pressed
        """
        return self.button_id == 4 and self.button_type == 1 and self.value == 1

    def L1_released(self):
        """
        Checks if L1 have just been released
        """
        return self.button_id == 4 and self.button_type == 1 and self.value == 0

    def R1_pressed(self):
        """
        Checks if R1 have just been pressed
        """
        return self.button_id == 5 and self.button_type == 1 and self.value == 1

    def R1_released(self):
        """
        Checks if R1 have just been released
        """
        return self.button_id == 5 and self.button_type == 1 and self.value == 0

    def L2_pressed(self):
        """
        Checks if L2 have just been pressed
        """
        return self.button_id == 2 and self.button_type == 2 and (32767 >= self.value >= -32766)

    def L2_released(self):
        """
        Checks if L2 have just been released
        """
        return self.button_id == 2 and self.button_type == 2 and self.value == -32767

    def R2_pressed(self):
        """
        Checks if R2 have just been pressed
        """
        return self.button_id == 5 and self.button_type == 2 and (32767 >= self.value >= -32766)

    def R2_released(self):
        """
        Checks if R2 have just been released
        """
        return self.button_id == 5 and self.button_type == 2 and self.value == -32767

    def up_arrow_pressed(self):
        """
        Checks if up arrow have just been pressed
        """
        return self.button_id == 7 and self.button_type == 2 and self.value == -32767

    def down_arrow_pressed(self):
        """
        Checks if down arrow have just been pressed
        """
        return self.button_id == 7 and self.button_type == 2 and self.value == 32767

    def up_down_arrow_released(self):
        """
        Checks if up or down arrow released
        Up or Down arrow buttons on release are not distinguishable
        """
        return self.button_id == 7 and self.button_type == 2 and self.value == 0

    def left_arrow_pressed(self):
        """
        Checks if left arrow have just been pressed
        """
        return self.button_id == 6 and self.button_type == 2 and self.value == -32767

    def right_arrow_pressed(self):
        """
        Checks if right arrow have just been pressed
        """
        return self.button_id == 6 and self.button_type == 2 and self.value == 32767

    def left_right_arrow_released(self):
        """
        Checks if left_right_arrow_released
        Left or Right arrow buttons on release are not distinguishable
        """
        return self.button_id == 6 and self.button_type == 2 and self.value == 0

    def playstation_button_pressed(self):
        """
        Checks if playstation button have just been pressed
        """
        return self.button_id == 10 and self.button_type == 1 and self.value == 1

    def playstation_button_released(self):
        """
        Checks if playstation button have just been released
        """
        return self.button_id == 10 and self.button_type == 1 and self.value == 0
