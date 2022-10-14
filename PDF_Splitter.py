from tkinter import ttk
from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def create_pdf(input_pdf, new_file_path, first_page, last_page):
    pdf_writer = PdfFileWriter()
    for page in range(first_page, last_page):
        pdf_writer.addPage(input_pdf.getPage(page))
    with open(new_file_path, 'wb') as pdf_file:
        pdf_writer.write(pdf_file)

# Breaks down a path into three parts (path, filename, and extension)
def path_parser(path_with_file_name_and_extension):
    complete_path = path_with_file_name_and_extension
    path_only = os.path.dirname(complete_path)
    file_name_with_extension = os.path.basename(complete_path)
    filename, extension = os.path.splitext(file_name_with_extension)
    return path_only, filename, extension
def open_file():
    # Get file path
    file_path = filedialog.askopenfilename(initialdir = "~",
                                    title = "Choose PDF File",
                                    filetypes = [("PDF Files", "*.pdf")])
    if file_path is not None:
        file_path_label['text'] = file_path
        total_pages = PdfFileReader(open(file_path, "rb"), strict=False).numPages
        pages = [ i  for i in range(1, total_pages+1) ]
        #Add page numbers to ComboBoxes
        first_page_combobox.config(values=pages)
        last_page_combobox.config(values=pages)
        first_page_combobox.current(0)
        last_page_combobox.current(0)

def create_file():
    first_page = first_page_combobox.get()
    last_page = last_page_combobox.get()

    if (first_page != "..."):
        #First page has to be one number lower
        first_page = int(first_page) - 1
        last_page = int(last_page)

        if (first_page <= last_page):
            destination_path = filedialog.asksaveasfilename(initialdir = "~", 
                                      title = "Save File", 
                                      filetypes = [("PDF", "*.pdf")],
                                      defaultextension=".pdf")
        #Read original file
        pdf_reader = PdfFileReader(open(file_path_label['text'], "rb"), strict=False)
        #Create new pdf
        #Multiple
        if split_by_page.get():
            path_only, file_name, extension = path_parser(destination_path)
            for page in range(first_page, last_page):
                path_file_and_name = path_only + "/" + file_name
                complete_path = path_file_and_name + "_" + str(page+1) + extension
                create_pdf(pdf_reader, complete_path, page, page+1)
        #Single file
        else:
            create_pdf(pdf_reader, destination_path, first_page, last_page)
        #Message box to notify user that the file has been created
        messagebox.showinfo(title="Completed", message="File created successfully")

def cancel():
    file_path_label['text'] = "N/A"
    first_page_combobox.config(values=["..."])
    last_page_combobox.config(values=["..."])
    first_page_combobox.current(0)
    last_page_combobox.current(0)

def main_window():
    #Create Window
    root = Tk()
    root.title("PDF Splitter")
    
    root.resizable(width=False, height=False)
    #Center Window
    root.eval('tk::PlaceWindow . center')

    # photo = PhotoImage(file='split.png')
    root.wm_iconbitmap('split.ico')
    #Create menu bar
    menu_bar = Menu(root)

    #Create file menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Open", command=open_file)

    #Create options menu
    options_menu = Menu(menu_bar, tearoff=0)
    # Variable used by the checkbutton
    global split_by_page
    split_by_page = BooleanVar()
    options_menu.add_checkbutton(label='Split by page', onvalue=1, offvalue=0, variable=split_by_page)

    #Add the cascades
    menu_bar.add_cascade(label='File', menu=file_menu)
    menu_bar.add_cascade(label='Options', menu=options_menu)

    root.config(menu=menu_bar)

    #Create labels, buttons, textboxes,etc
    file_selection_label = Label(root, relief=FLAT, text="Selected File:")
    global file_path_label
    file_path_label = Label(root, relief=GROOVE, text="N/A")
    page_selection_label = Label(root, relief=FLAT, text="Page Selection:")
    dash_label = Label(root, text="-")
    global first_page_combobox
    first_page_combobox = ttk.Combobox(root, state="readonly", values=["..."], width=10)
    global last_page_combobox
    last_page_combobox = ttk.Combobox(root, state="readonly", values=["..."], width=10)
    save_button = Button(root, text="Save", command=create_file)
    cancel_button = Button(root, text="Cancel", command=cancel)

    first_page_combobox.current(0)
    last_page_combobox.current(0)

    # Position entry + buttons
    file_selection_label.grid(row=0, column=0, columnspan=3, padx=15, pady=(15, 0), sticky=W+E+N+S)
    file_path_label.grid(row=1, column=0, columnspan=3, padx=15, pady=(0, 10), sticky=W+E+N+S)
    page_selection_label.grid(row=2, column=0, columnspan=3, padx=15, pady=(10, 5), sticky=W+E+N+S)
    first_page_combobox.grid(row=3, column=0, padx=15, sticky=W+E+N+S)
    dash_label.grid(row=3, column=1, padx=15, sticky=W+E+N+S)
    last_page_combobox.grid(row=3, column=2, padx=15, sticky=W+E+N+S)

    save_button.grid(row=4, column=0, padx=15, pady=(20, 15), columnspan=1, sticky=W+E+N+S)
    cancel_button.grid(row=4, column=2, columnspan=1, padx=15, pady=(20, 15), sticky=W+E+N+S)


    root.mainloop()

if __name__ == '__main__':
    main_window()
