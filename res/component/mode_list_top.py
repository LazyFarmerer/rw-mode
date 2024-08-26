from tkinter import Frame, Label, Radiobutton, StringVar

from ..base_class.observer import Subscriber
from ..base_class.mode_type import ModeType

class ModeListTop(Frame, Subscriber):
    def __init__(self, master, radio_var: StringVar, *args, **kwargs) -> None:
        Frame.__init__(self, master, *args, **kwargs)
        Subscriber.__init__(self)

        label = Label(self, text="모드 목록")
        label.grid(row=0, column=0, padx=0, pady=10)

        local_radio = Radiobutton(self, text="로컬", value=ModeType.local.name, variable=radio_var, command=self.notify)
        local_radio.grid(row=1, column=0, padx=0, pady=0)

        steem_radio = Radiobutton(self, text="창작마당", value=ModeType.steem.name, variable=radio_var, command=self.notify)
        steem_radio.grid(row=1, column=1, padx=0, pady=0)
