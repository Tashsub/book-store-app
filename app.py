#written by: Tashinga 

from tkinter import *
import backend

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
    a11.insert(END,results)

def add():
    a11.delete(0, END)
    title= title_entry.get()
    author= author_entry.get()
    isbn= isbn_entry.get()
    year= year_entry.get()
    backend.insert_book(title, year, author, isbn)
    a11.insert(END,(title, author, isbn, year))

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
a10=Button(window, text="Upload", width=10)
a10.grid(row=1,column=4)

#list box to display content
a11 = Listbox(window, height=20, width=50)
a11.grid(row=2,column=0,rowspan=10,columnspan=2)


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
update=Button(window, text="Update Selected", width = 30, height = 2)
update.grid(row=5, column=3, columnspan=10) 

#Delete
delete=Button(window, text="Delete Selected", width = 30, height = 2)
delete.grid(row=6, column=3, columnspan=10) 

#close
close=Button(window, text="Close", width = 30, height = 2)
close.grid(row=7, column=3, columnspan=10) 

window.mainloop()