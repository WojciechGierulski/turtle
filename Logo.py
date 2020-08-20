from gui import Gui
from PIL import Image, ImageTk
import tkinter


if __name__ == '__main__':

    gui1 = Gui()                #creates Gui object

    gui1.create_objects()       #creates object's like buttons
    gui1.place_objects()        #places created objects
    gui1.change_turtle_image()  #sets turtle image      
    gui1.start_gui()            #runs application