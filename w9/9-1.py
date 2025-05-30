from tkinter import *

window = Tk()

photo1 = PhotoImage(file='C:\\Users\\xokny\\OneDrive\\Desktop\\pythonprogramming\\windowProgramming\\pet-dog.gif')
photo2 = PhotoImage(file='C:\\Users\\xokny\\OneDrive\\Desktop\\pythonprogramming\\windowProgramming\\dog-headpat.gif')

label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()
