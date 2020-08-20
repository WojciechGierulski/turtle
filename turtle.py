from help_functions import *
from Exceptions_ch import *
from PIL import Image


class Turtlee():
    """
     class representing Turtle, contains its available moves and his appearance, cooperates with Gui Object
     which should be passed as an argument to every function that affects turtle

    :param state: True if turtle is drawing, False if Turtle is not drawing
    :type state: bool
    :param commands: contains all available commands,
        list[0] is corresponding function,
        list[1] contains function's argument checker
        by default command should look like:{command} {argument}
        leave {argument} empty if function does not need any
    :param _input_length: how many elements does the proper command contain,
     Example: currently 2: {argument} and {command}
    :type _input_length: int
    :type commands: dictionary
    :param position_x: contains x coordinate of turtle
    :type position_x: int
    :param position_y: contains y coordinate of turtle
    :type position_y: int
    :param ang_position: contains angular position of turtle, measured
    :type ang_position: int
    :param max_x: obvious
    :type max_x: int
    :param max_y: obvious
    :type max_y: int
    :param image: turtle's actual image
    :type image: PILLOW Imgage object
    :param path_to_turtle_true: path to image that should be visible if state is True
    :type path_to_turtle_true: str
    :param path_to_turtle_false: path to image that should be visible if state is False
    :type path_to_turtle_false: str
    """
    def __init__(self, x0=350, y0=300, angle=0, max_x=700, max_y=600,
                 state=True, _input_length=2,
                 path_to_turtle_true='turtle_true.png', path_to_turtle_false='turtle_false.png'):
        """
        constructor method, sets default values
        """
        self.position_x = x0
        self.position_y = y0
        self.ang_position = angle
        self.state = state
        self._input_length = _input_length
        self.max_x = max_x
        self.max_y = max_y
        if if_file_exists(path_to_turtle_true):
            self.turtle_true = path_to_turtle_true
        if if_file_exists(path_to_turtle_false):
            self.turtle_false = path_to_turtle_false

        self.image = turtle_image_convert_and_open(self.turtle_true, self)

    def check_coordinates(self, x, y):
        """
        checks if coordinates are in range of max and min value,
        if they are not, sets them to max/min value
        with these settings turtle can slide upon the edge of canvas
        """
        if x > self.max_x:
            x = self.max_x
        if x < 0:
            x = 0
        if y > self.max_y:
            y = self.max_y
        if y < 0:
            y = 0
        return x, y

    def pick(self, gui):
        """
        sets state to False
        """
        self.state = False
        self.image = turtle_image_convert_and_open(self.turtle_false, self)
        gui.change_turtle_image()                                               #on gui's canvas

    def drop(self, gui):
        """
        sets state to True
        """
        self.state = True
        self.image = turtle_image_convert_and_open(self.turtle_true, self)
        gui.change_turtle_image()                                               #on gui's canvas

    def forward(self, distance, gui):
        """
        changes coordinates of turtle, draws the line on given canvas,
        changes turtle's image position
        """
        x0 = self.position_x
        y0 = self.position_y
        ang0 = self.ang_position
        distance = int(distance)
        x1, y1 = coordinates_calculator(x0, y0,
                                        distance, ang0)
        x1, y1 = self.check_coordinates(x1, y1)
        if self.state is True:
            gui.canvas.create_line(x0, y0, x1, y1)
        self.position_x = x1
        self.position_y = y1
        gui.change_turtle_image()                                           #on gui's canvas


    def rotate(self, angle, gui, full_cycle=360):
        """
        rotates Turtle anti-clockwise by the given angle,
        rotates turtle's image
        """
        angle = int(angle)
        self.ang_position += angle
        self.ang_position = self.ang_position % full_cycle
        self.image = turtle_image_convert_and_open(self.turtle_true if self.state is True else self.turtle_false,
                                                   self)
        gui.change_turtle_image()                                          #on gui's canvas
        

    def forward_checker(self, argument):
        """
        True if forward's argument is valid
        """
        if is_number(argument):
            return True
        else:
            return False

    def rotate_checker(self, argument):
        """
        True if rotate's argument is valid
        """
        if is_number(argument):
            return True
        else:
            return False

    def pick_checker(self, argument):
        """
        True if pick's argument is valid
        """
        if argument == '':
            return True
        else:
            return False

    def drop_checker(self, argument):
        """
        True if drop's argument is valid
        """
        if argument == '':
            return True
        else:
            return False

    commands = {"pick": [pick, pick_checker], "drop": [drop, drop_checker],         #{command wrtitten in gui's entry}: [{function}, {argument_checker}]
                "forward": [forward, forward_checker],
                "rotate": [rotate, rotate_checker]}
