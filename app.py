#written by: Tashinga 


from tkinter import *


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
a8.grid(row=1, column=3 )



window.mainloop()