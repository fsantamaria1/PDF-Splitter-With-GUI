from tkinter import ttk
from tkinter import *

def donothing():
    print('something')

def main_window():
    #Create Window
    root = Tk()
    root.title("PDF Splitter")
    root.resizable(width=False, height=False)
    #Center Window
    root.eval('tk::PlaceWindow . center')

    #Create menu bar
    menu_bar = Menu(root)

    #Create file menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=donothing)

    #Create options menu
    options_menu = Menu(menu_bar, tearoff=0)
    # Variable used by the checkbutton
    split_by_page = BooleanVar()
    options_menu.add_checkbutton(label='Split by page', onvalue=1, offvalue=0, variable=split_by_page)

    #Add the cascades
    menu_bar.add_cascade(label='File', menu=file_menu)
    menu_bar.add_cascade(label='Options', menu=options_menu)

    root.config(menu=menu_bar)
    root.mainloop()

if __name__ == '__main__':
    main_window()
