import tkinter

def baseLabel(event):
    global baseFrame
    lb=tkinter.Label(baseFrame,text="谢谢点击")
    lb.pack()

baseFrame=tkinter.Tk()
menubar=tkinter.Menu(baseFrame)
for item in ['File','Edit','View']:
    menubar.add_command(label=item)
baseFrame['menu']=menubar

lb=tkinter.Label(baseFrame,text="模拟按钮")
lb.bind("<Button-1>",baseLabel)
lb.pack()

baseFrame.mainloop()