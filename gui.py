import tkinter
from PIL import ImageTk
from tkinter import messagebox
from turtle import Turtlee
from help_functions import *
from Exceptions_ch import *
import os


class Gui:
    """
    class describing graphic interface, cooperates with Turtlee Object
    """
    def __init__(self):

        if os.environ.get('DISPLAY', '') == '':
            os.environ.__setitem__('DISPLAY', ':0.0')

        self.root = tkinter.Tk()
        self.root.geometry("740x700")
        try:
            self.turtle = Turtlee()
        except (FileDoesNotExistError, FileOpenError) as e:
            print(e.name, e.message)

        self.canvas = tkinter.Canvas(self.root, width=self.turtle.max_x,
                                     height=self.turtle.max_y, bg='white')
        self.interactive_entry = tkinter.Entry(self.root,
                                               justify='center', width=17)
        self.wsad_entry = tkinter.Entry(self.root)

        self.turtle_image = None

    def change_turtle_image(self):
        """
        changes turtle_image attribute
        """
        new_image = self.turtle.image
        self.new_image2 = ImageTk.PhotoImage(new_image) 
        self.turtle_image = self.canvas.create_image(self.turtle.position_x,
                                                     self.turtle.position_y,
                                                     image=self.new_image2,
                                                     anchor=tkinter.CENTER)

    def clear_function(self):
        """
        deletes all lines on a canvas
        """
        self.canvas.delete('all')
        self.change_turtle_image()

    def interactive_function(self, event):
        """
        executed when enter is pressed on interactive_entry
        """
        try:
            command_executer(self.interactive_entry.get(), self.turtle, self)
            self.interactive_entry.delete(0, 'end')
        except (UnknownCommandError, UnknownFormatError, InvalidArgumentError) as e:
            messagebox.showinfo(e.name, e.message)
        except (FileOpenError, FileDoesNotExistError) as e:
            messagebox.showinfo(e.name, e.message)

    def wsad_function(self, event):
        """
        executed when enter is pressed on wsad_entry
        """
        try:
            lines = file_reader(self.wsad_entry.get())
            try:
                for i, line in enumerate(lines):
                    command_executer(line.rstrip(), self.turtle, self, i)
                    self.wsad_entry.delete(0, 'end')
            except (UnknownCommandError, UnknownFormatError, InvalidArgumentError) as e:
                messagebox.showinfo(e.name, e.message)
            except (FileDoesNotExistError, FileOpenError) as e:
                messagebox.showinfo(e.name, e.message)
        except FileDoesNotExistError as e:
            messagebox.showinfo(e.name, e.message)

    def draw(self, x0, y0, x1, y1):
        """
        draws a line on canvas
        """
        self.canvas.create_line(x0, y0, x1, y1)

    def create_objects(self):
        """
        creates objects which are part of interface
        """
        self.interactive_label = tkinter.Label(self.root, text='Command:')
        self.wsad_label = tkinter.Label(self.root, text='File path:')
        self.clear_button = tkinter.Button(self.root,
                                           text='clear', command=self.clear_function)

        self.interactive_entry.bind('<Return>', self.interactive_function)
        self.wsad_entry.bind('<Return>', self.wsad_function)

    def place_objects(self):
        """
        places created objects on interface
        """
        self.canvas.place(x=20, y=20)
        self.clear_button.place(x=650, y=660)
        self.interactive_entry.place(x=108, y=640)
        self.wsad_entry.place(x=400, y=640)
        self.interactive_label.place(x=100, y=625)
        self.wsad_label.place(x=400, y=625)

    def start_gui(self):
        """
        starts the app
        """
        self.root.mainloop()
