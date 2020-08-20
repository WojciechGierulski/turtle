from turtle import Turtlee
from gui import Gui
from help_functions import *
import math
from Exceptions_ch import *
import pytest


def test_turtle(distance3=-100, distance1=100, distance2=500000, ang1=730):

    turtle2 = Turtlee(x0=300, y0=300, angle=30)
    gui2 = Gui()
    turtle2.forward(distance1, gui2)
    assert turtle2.position_x == round(300 + math.sqrt(3) * 50)
    assert turtle2.position_y == 250

    turtle2.position_x = 0
    turtle2.position_y = 0
    turtle2.ang_position = 0
    turtle2.forward(distance2, gui2)
    assert turtle2.position_x == turtle2.max_x
    assert turtle2.position_y == 0

    turtle2.position_x = 300
    turtle2.position_y = 0
    turtle2.ang_position = 0
    turtle2.forward(distance3, gui2)
    assert turtle2.position_x == 200
    assert turtle2.position_y == 0

    turtle2.rotate(ang1, gui2)
    assert turtle2.ang_position == 10


def test_formaterror():
    with pytest.raises(UnknownFormatError):
        turtle = Turtlee()
        format_checker("das  dasdsa  ", turtle)


def test_commanderror():
    with pytest.raises(UnknownCommandError):
        turtle = Turtlee()
        command_checker('gora', 30, turtle)


def test_argumenterror():
    with pytest.raises(InvalidArgumentError):
        turtle = Turtlee()
        argument_checker('naprzod', 'haha', turtle)


def test_turtleimage():
    with pytest.raises(FileDoesNotExistError):
        turtle = Turtlee(path_to_turtle_false='nic')


def test_format():
    turtle = Turtlee()
    komenda1, argument1 = format_checker('naprzod 50', turtle)
    komenda2, argument2 = format_checker('podnies', turtle)
    assert komenda1 == 'naprzod'
    assert argument1 == '50'
    assert komenda2 == 'podnies'
    assert argument2 == ''


def test_argument():
    turtle = Turtlee()
    x = argument_checker('naprzod', '50', turtle)
    assert x is True


def test_command():
    turtle = Turtlee()
    x = command_checker('naprzod', '50', turtle)
    assert x is True
