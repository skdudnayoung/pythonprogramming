from tkinter import *

fnameList = [
    "dog-7011_256.gif", "dog-headpat.gif", "drive-away-1640_256.gif",
    "emu-14760_256.gif", "hamster-14608_256.gif", "pet-dog.gif",
    "pig-418_256.gif", "robot-4212_256.gif", "running-3129_256.gif"
]
photoList = [None] * 9
num = 0

# 절대 경로 설정
base_path = "C:/Users/xokny/OneDrive/Desktop/pythonprogramming/windowProgramming/"

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0

    photo = PhotoImage(file=base_path + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8

    photo = PhotoImage(file=base_path + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

# 첫 이미지 표시
photo = PhotoImage(file=base_path + fnameList[num])
pLabel = Label(window, image=photo)
pLabel.image = photo
pLabel.pack()

# 이전/다음 버튼 추가
btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)
btnPrev.pack(side=LEFT, padx=10, pady=10)
btnNext.pack(side=RIGHT, padx=10, pady=10)

window.mainloop()
