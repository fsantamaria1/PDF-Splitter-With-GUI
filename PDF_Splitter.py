from tkinter import ttk
from tkinter import *

def main_window():
    #Create Window
    root = Tk()
    root.title("PDF Splitter")
    root.resizable(width=False, height=False)
    #Center Window
    root.eval('tk::PlaceWindow . center')

    root.mainloop()

if __name__ == '__main__':
    main_window()
