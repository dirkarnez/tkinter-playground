
from tkinter import *
from tkinter.ttk import *

class Win:
    def __init__(self):
        self.root = self.__win()
        self.tk_button_l4s5v0vc = self.__tk_button_l4s5v0vc()
        self.tk_label_l4s5v4fi = self.__tk_label_l4s5v4fi()
        self.tk_input_l4s5v85b = self.__tk_input_l4s5v85b()
        self.tk_radio_button_l4s5vcuf = self.__tk_radio_button_l4s5vcuf()
        self.tk_select_box_l4s5vjk7 = self.__tk_select_box_l4s5vjk7()
        self.tk_list_box_l4s5vpz2 = self.__tk_list_box_l4s5vpz2()
        self.tk_select_box_l4s5vsgl = self.__tk_select_box_l4s5vsgl()
        self.tk_radio_button_l4s5w1z2 = self.__tk_radio_button_l4s5w1z2()

    def __win(self):
        root = Tk()
        root.title("我是标题")
        # 设置大小 居中展示
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False, height=False)
        return root

    def show(self):
        self.root.mainloop()

    def __tk_button_l4s5v0vc(self):
        btn = Button(self.root, text="按钮")
        btn.place(x=20, y=20, width=50, height=24)
        return btn

    def __tk_label_l4s5v4fi(self):
        label = Label(self.root,text="标签")
        label.place(x=80, y=20, width=50, height=24)
        return label

    def __tk_input_l4s5v85b(self):
        ipt = Entry(self.root)
        ipt.place(x=150, y=20, width=150, height=24)
        return ipt

    def __tk_radio_button_l4s5vcuf(self):
        rb = Radiobutton(self.root,text="单选框")
        rb.place(x=20, y=60, width=80, height=24)
        return rb

    def __tk_select_box_l4s5vjk7(self):
        cb = Combobox(self.root, state="readonly")
        cb['values'] = ("下拉选择框", "Python", "Tkinter Helper")
        cb.place(x=230, y=70, width=150, height=24)
        return cb

    def __tk_list_box_l4s5vpz2(self):
        lb = Listbox(self.root)
        lb.insert(END, "列表框")
        lb.insert(END, "Python")
        lb.insert(END, "Tkinter Helper")
        lb.place(x=50, y=130, width=150, height=100)
        return lb

    def __tk_select_box_l4s5vsgl(self):
        cb = Combobox(self.root, state="readonly")
        cb['values'] = ("下拉选择框", "Python", "Tkinter Helper")
        cb.place(x=240, y=110, width=150, height=24)
        return cb

    def __tk_radio_button_l4s5w1z2(self):
        rb = Radiobutton(self.root,text="单选框")
        rb.place(x=120, y=70, width=80, height=24)
        return rb

if __name__ == "__main__":
    win = Win()
    # TODO 绑定点击事件或其他逻辑处理
    win.show()