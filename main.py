from tkinter import *

TIMER = 2


class Typist:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typist")
        self.window.config(padx=20, pady=20)
        self.text_box = Text()
        self.text_box.pack()
        self.text_box.bind("<KeyRelease>", self.reset_timer)
        self.time_left = TIMER
        self.timer = None

    def reset_timer(self, event):
        if self.timer is not None:
            self.window.after_cancel(self.timer)
            self.time_left = TIMER
            self.countdown()
        else:
            self.countdown()

    def countdown(self):
        if self.time_left == 0:
            self.erase()
        else:
            print(self.time_left)
            self.time_left -= 1
            self.timer = self.window.after(1000, self.countdown)

    def erase(self):
        self.text_box.delete('1.0', END)


typist = Typist()

typist.window.mainloop()
