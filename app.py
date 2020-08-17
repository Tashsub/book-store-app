#written by: Tashinga 

from tkinter import *
import backend

window=Tk()

#title field
a1 = Label(window, text = "Title")
a1.grid(row=0, column=0)
a2=Entry(window)
a2.grid(row=0, column=1)

#year field
a3 =  Label(window, text = "Year")
a3.grid(row=1, column=0)
a4 = Entry(window)
a4.grid(row=1, column=1 )

#author field 
a5 = Label(window, text = "Author")
a5.grid(row=0, column=2)
a6=Entry(window)
a6.grid(row=0, column=3)

#ISBN field
a7 = Label(window, text = "ISBN")
a7.grid(row=1, column=2)
a8 = Entry(window)
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
viewall=Button(window, text="View All", width = 30, height = 2)
viewall.grid(row=2, column=3, columnspan=10)

#Search Entry
search=Button(window, text="Search Entry", width = 30, height = 2)
search.grid(row=3, column=3, columnspan=10) 

#Add entry
add=Button(window, text="Add Entry", width = 30, height = 2)
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