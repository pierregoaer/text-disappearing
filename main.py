from tkinter import *
import pyperclip

TIMER = 2


class Typist:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typist")
        self.window.config(padx=20, pady=20)

        self.label = Label(text="Choose you duration in seconds:")
        self.label.pack()

        self.speed_slider = Scale(from_=1, to=120, orient='horizontal', command=self.get_timer)
        self.speed_slider.set(20)
        self.speed_slider.pack()

        self.text_box = Text()
        self.text_box.pack(pady=20)
        self.text_box.bind("<KeyRelease>", self.reset_timer)

        self.copy_button = Button(text="Copy to clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

        self.TIMER = 2
        self.time_left = self.TIMER
        self.timer = None

    def get_timer(self, event):
        self.TIMER = self.speed_slider.get()
        self.time_left = self.TIMER

    def reset_timer(self, event):
        if self.timer is not None:
            self.window.after_cancel(self.timer)
            self.time_left = self.TIMER
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

    def copy_to_clipboard(self):
        text_to_copy = self.text_box.get("1.0", END)
        pyperclip.copy(text_to_copy)
        self.erase()


typist = Typist()

typist.window.mainloop()
