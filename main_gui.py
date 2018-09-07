#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

from command_exe import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.command_text = Text(self, width=60, height=15)
        self.command_text.pack(fill=X)
        self.execute_button = Button(self, text='Execute', command=self.on_execute)
        self.execute_button.pack(fill=X)

    def on_execute(self):
        command = self.command_text.get('1.0', END)
        command_exe = CommandExe()
        command_exe.shell(command)


if __name__ == "__main__":
    app = Application()
    app.master.title('ADBKit')
    app.mainloop()
