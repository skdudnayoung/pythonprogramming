from tkinter import *
from tkinter import messagebox

def showKey(name):
    messagebox.showinfo("키보드 이벤트", f"눌린 키: {name}")

window = Tk()

# Shift + 방향키 이벤트 바인딩
window.bind("<Shift-Up>", lambda e: showKey("Shift + 위쪽 화살표"))
window.bind("<Shift-Down>", lambda e: showKey("Shift + 아래쪽 화살표"))
window.bind("<Shift-Left>", lambda e: showKey("Shift + 왼쪽 화살표"))
window.bind("<Shift-Right>", lambda e: showKey("Shift + 오른쪽 화살표"))

# 일반 키 이벤트 처리
def keyEvent(event):
    # 방향키 및 Shift 키 조합 무시
    if event.keysym in ['Up', 'Down', 'Left', 'Right', 'Shift_L', 'Shift_R']:
        return
    try:
        messagebox.showinfo("키보드 이벤트", "눌린 키: " + event.char)
    except:
        messagebox.showinfo("키보드 이벤트", f"눌린 키코드: {event.keycode}")

window.bind("<Key>", keyEvent)

window.mainloop()
