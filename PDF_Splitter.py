from tkinter import ttk
from tkinter import *
from tkinter import filedialog

def donothing():
    pass

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

    #Create labels, buttons, textboxes,etc
    file_selection_label = Label(root, relief=FLAT, text="Selected File:")
    file_path_label = Label(root, relief=GROOVE, text="N/A")
    page_selection_label = Label(root, relief=FLAT, text="Page Selection:")
    dash_label = Label(root, text="-")
    first_page_combobox = ttk.Combobox(root, state="readonly", values=["..."], width=10)
    last_page_combobox = ttk.Combobox(root, state="readonly", values=["..."], width=10)
    save_file = Button(root, text="Save", command=donothing)
    cancel = Button(root, text="Cancel", command=donothing)

    first_page_combobox.current(0)
    last_page_combobox.current(0)

    # Position entry + buttons
    file_selection_label.grid(row=0, column=0, columnspan=3, padx=15, pady=(15, 0), sticky=W+E+N+S)
    file_path_label.grid(row=1, column=0, columnspan=3, padx=15, pady=(0, 10), sticky=W+E+N+S)
    page_selection_label.grid(row=2, column=0, columnspan=3, padx=15, pady=(10, 5), sticky=W+E+N+S)
    first_page_combobox.grid(row=3, column=0, padx=15, sticky=W+E+N+S)
    dash_label.grid(row=3, column=1, padx=15, sticky=W+E+N+S)
    last_page_combobox.grid(row=3, column=2, padx=15, sticky=W+E+N+S)

    # save_file.grid(row=3, column=0, padx=15, pady=(15, 15), columnspan=3, sticky=W+E+N+S)
    save_file.grid(row=4, column=0, padx=15, pady=(20, 15), columnspan=1, sticky=W+E+N+S)
    cancel.grid(row=4, column=2, columnspan=1, padx=15, pady=(20, 15), sticky=W+E+N+S)


    root.mainloop()

if __name__ == '__main__':
    main_window()
