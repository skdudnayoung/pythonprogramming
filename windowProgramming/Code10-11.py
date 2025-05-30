from tkinter import *

btnList = [None] * 9
fnameList = [
    "dog-7011_256.gif", "dog-headpat.gif", "drive-away-1640_256.gif",
    "emu-14760_256.gif", "hamster-14608_256.gif", "pet-dog.gif",
    "pig-418_256.gif", "robot-4212_256.gif", "running-3129_256.gif"
]
photoList = [None] * 9

window = Tk()
window.geometry("210x210")  

xPos, yPos = 0, 0
num = 0

base_path = "C:/Users/xokny/OneDrive/Desktop/pythonprogramming/windowProgramming/"

for i in range(9):
    full_path = base_path + fnameList[i]
    photoList[i] = PhotoImage(file=full_path)
    btnList[i] = Button(window, image=photoList[i])

for i in range(3):
    for k in range(3):
        btnList[num].place(x=xPos, y=yPos)
        xPos += 70
        num += 1
    xPos = 0
    yPos += 70

window.mainloop()
