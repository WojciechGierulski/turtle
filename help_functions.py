import math
import os.path
from Exceptions_ch import *
from PIL import Image


def is_number(string):
    """
    returns True if given string can be converted to an int
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def coordinates_calculator(x0, y0, distance, angle):
    """
    calculates turtle's coordinates after travelling given distance
    """
    x1 = int(round(x0 + distance * math.cos(math.radians(angle))))
    y1 = int(round(y0 + distance * math.sin(math.radians(angle)) * -1))    # -1 because image cooordinate system is inverted
    return x1, y1


def format_checker(input, turtle, line=None):
    """
    checks if line has proper format: {command} {argument}
    """
    if ' ' not in input:
        input = input + ' '                 #to be able to use .split(' ')
    input = input.split(' ')
    if len(input) != turtle._input_length:
        message = 'Unknown format' + (f' in line {line}' if line is not None else '')
        raise UnknownFormatError(message)
    else:
        command = input[0]
        argument = input[1]
        return command, argument


def command_checker(command, argument, turtle, line=None):
    """
    check's if command is valid
    """
    if command not in turtle.commands:
        message = 'Unknown command' + (f' in line {line}' if line is not None else '')
        raise UnknownCommandError(message)
    else:
        return True


def argument_checker(command, argument, turtle, line=None):
    """
    returns True if command's argument is valid and False if not
    """
    if turtle.commands[command][1](turtle, argument):       #[entry input][turtle's argument checler]
        return True
    else:
        message = 'Invalid argument' + (f' in line {line}' if line is not None else '')
        raise InvalidArgumentError(message)


def command_executer(input, turtle, gui, line=None):
    """
    executes given command
    """
    command, argument = format_checker(input, turtle, line)
    if command_checker(command, argument, turtle, line):
        if argument_checker(command, argument, turtle, line):
            if len(argument) == 0:
                turtle.commands[command][0](turtle, gui)            #command that does not need argument
            else:
                turtle.commands[command][0](turtle, argument, gui)  #command that do need argument


def if_file_exists(file_path):
    """
    checks if file exists
    """
    if os.path.isfile(file_path):
        return True
    else:
        raise FileDoesNotExistError()


def file_reader(file_path):
    """
    reutrns file's lines
    """
    if if_file_exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return lines


def turtle_image_convert_and_open(path, turtle, scale=0.08):
    """
    returns resized image
    """
    if if_file_exists(path):
        try:
            image = Image.open(path)
        except Exception:
            raise FileOpenError
        width, height = image.size
        k = height/width
        new_width = round(turtle.max_x * scale)
        new_height = round(new_width * k)
        image1 = image.resize((new_width, new_height), Image.ANTIALIAS)
        image2 = image1.rotate(turtle.ang_position, expand=True)
        return image2
