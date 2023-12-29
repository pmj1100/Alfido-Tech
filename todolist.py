from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('700x500+300+200')

        self.label = Label(self.root, text='To-Do list', font='ariel, 25 bold', width=10, bd=5, bg='green', fg='black')
        self.label.pack(side='top', fill=BOTH)

        self.label2 = Label(self.root, text='Add Task', font='ariel, 19 bold', width=10, bd=5, bg='green', fg='black')
        self.label2.place(x=40, y=55)

        self.label3 = Label(self.root, text='Tasks', font='ariel, 19 bold', width=10, bd=5, bg='green', fg='black')
        self.label3.place(x=300, y=55)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font='ariel, 20 italic bold')
        self.main_text.place(x=280, y=100)

        self.main = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.main.place(x=20, y=120)

        def add():
            content = self.main.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
            self.main.delete(1.0, END)

        def delete():
            delete_ = self.main_text.curselection()
            if delete_:
                self.main_text.delete(delete_[0])
                with open('data.txt', 'r+') as f:
                    new_f = f.readlines()
                    f.seek(0)
                    for line in new_f:
                        if str(delete_[0]) not in line:
                            f.write(line)
                    f.truncate()

        with open('data.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)

        self.button = Button(self.root, text="Add", font='sarif 20 bold italic', width=10, bd=5, bg='green', fg='black',
                             command=add)
        self.button.place(x=30, y=200)

        self.button2 = Button(self.root, text="Delete", font='sarif 20 bold italic', width=10, bd=5, bg='green',
                              fg='black', command=delete)
        self.button2.place(x=30, y=280)

def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()



