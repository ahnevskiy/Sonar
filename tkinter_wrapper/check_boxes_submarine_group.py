from tkinter import *
from tkinter_wrapper.check_box import MyCheckBox



def disable(self):
    self.object.configure(state="disabled")
    self.buf_state = self.object["state"]
    state = True
    for chb in self.group:
        if chb.state.get() is not True:
            state = False
    if state:
        btn.object.configure(state="active")
        btn.buf_state = btn.object["state"]


def reset(self):
    for j in range(c):
        check_boxes[j].state.set(False)
        check_boxes[j].object.configure(state="enabled")
        print(check_boxes[j].buf_state)
        check_boxes[j].buf_state = check_boxes[j].object["state"]
        print(check_boxes[j].buf_state)
    self.object.configure(state="disabled")
    self.buf_state = self.object["state"]

c = 3

window = Tk()
window.title("[Настольный симулятор] Субмарина")
window.iconbitmap("gui/sonar.ico")
# window.geometry('400x250')
window.maxsize(width=1500, height=700)
window.minsize(width=1500, height=700)

lf = MyLabaledContainer(parent=window,
                        label="Субмарина",
                        x=10,
                        y=10,
                        width=c*16+60,
                        height=50)

check_boxes = []

for i in range(c):
    check_boxes.append(MyCheckBox(group=check_boxes, x=i*16, parent=lf, command=disable))

lf.add_objects(objects=check_boxes)

btn = MyButton(parent=lf.container, x=c*16, y=-2, text="Готов!", command=reset)
lf.add_objects(objects=[btn])


btn2 = Button(window, text="Отключить", command=lf.disable_all, bg="green")
btn2.place(x=10, y=65)


btn4 = Button(window, text="Восстановить", command=lf.restore_state_all, bg="red")
btn4.place(x=100, y=65)

window.mainloop()
