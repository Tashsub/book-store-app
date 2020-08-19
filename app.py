#written by: Tashinga 

from tkinter import *
from tkinter import filedialog
import backend
from PIL import ImageTk, Image
import os
from tkinter.filedialog import asksaveasfile 
import shutil

#command functions
def view():
    a11.delete(0,END)
    for item in backend.view_all():
       a11.insert(END, item) 

def search_q():
    a11.delete(0, END)
    title= title_entry.get()
    author= author_entry.get()
    isbn= isbn_entry.get()
    year= year_entry.get()
    results = backend.search_entry(title, author, isbn, year)
    for item in results:
        a11.insert(END, item)

def add():
    a11.delete(0, END)
    title= title_entry.get()
    author= author_entry.get()
    isbn= isbn_entry.get()
    year= year_entry.get()
    backend.insert_book(title, year, author, isbn)
    a11.insert(END,(title, year, author, isbn))


def get_seleted_row(event):
    global row
    index = a11.curselection()[0]
    print("The index is", index)
    row = a11.get(index)
    print("The row is ", row)
    #each time a user clicks on a row it will be displayed
    #in the fields
    unique_id = row[0]
    title=row[1]
    year=row[2]
    author=row[3]
    isbn=row[4]

    a2.delete(0,END)
    a4.delete(0, END)
    a6.delete(0,END)
    a8.delete(0,END)
    a2.insert(END,title)
    a4.insert(END, year)
    a6.insert(END, author)
    a8.insert(END, isbn)
    return row

def delete_selected():
    print(row[0])
    unique_id = int(row[0])
    backend.delete_entry(unique_id)
    view()

def update_selected():
    unique_id =row[0]
    title= title_entry.get()
    year = year_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    backend.update_entry(title,year,author,isbn,unique_id)
    view()

def upload_file(event=None):
    filename = filedialog.askopenfilename()
    source = filename
    print('Selected:', filename)
    input = filename

def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 
  

window=Tk()

#title field
a1 = Label(window, text = "Title")
a1.grid(row=0, column=0)
title_entry = StringVar()
a2=Entry(window, textvariable=title_entry)
a2.grid(row=0, column=1)

#year field
a3 =  Label(window, text = "Year")
a3.grid(row=1, column=0)
year_entry=StringVar()
a4 = Entry(window, textvariable=year_entry)
a4.grid(row=1, column=1 )

#author field 
a5 = Label(window, text = "Author")
a5.grid(row=0, column=2)
author_entry = StringVar()
a6=Entry(window, textvariable=author_entry)
a6.grid(row=0, column=3)

#ISBN field
a7 = Label(window, text = "ISBN")
a7.grid(row=1, column=2)
isbn_entry=StringVar()
a8 = Entry(window, textvariable=isbn_entry)
a8.grid(row=1, column=3)

#attachments
a9=Label(window, text="Attachments")
a9.grid(row=0, column=4)
a10=Button(window, text="Upload", width=10, command= upload_file)
a10.grid(row=1,column=4)

#list box to display content
a11 = Listbox(window, height=20, width=50)
a11.grid(row=2,column=0,rowspan=10,columnspan=2)

a11.bind('<<ListboxSelect>>', get_seleted_row)


#scrollbar for listbox
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=10)
a11.configure(yscrollcommand=scroll.set)
scroll.configure(command=a11.yview)

#View all
viewall=Button(window, text="View All", width = 30, height = 2, command=view)
viewall.grid(row=2, column=3, columnspan=10)


#Search Entry
search=Button(window, text="Search Entry", width = 30, height = 2, command=search_q)
search.grid(row=3, column=3, columnspan=10) 

#Add entry
add=Button(window, text="Add Entry", width = 30, height = 2, command=add)
add.grid(row=4, column=3, columnspan=10) 

#update
update=Button(window, text="Update Selected", width = 30, height = 2, command=update_selected)
update.grid(row=5, column=3, columnspan=10) 

#Delete
delete=Button(window, text="Delete Selected", width = 30, height = 2, command=delete_selected)
delete.grid(row=6, column=3, columnspan=10) 

#close
close=Button(window, text="Close", width = 30, height = 2, command=window.destroy)
close.grid(row=7, column=3, columnspan=10) 

#image
img = ImageTk.PhotoImage(Image.open("img1.JPG"))
panel = Label(window, image = img)
panel.grid(row=20, column=0, columnspan = 20)



window.mainloop()