from typing import List
from tkinter import Frame, Scrollbar, Listbox

from ..models.mode import Mode
from ..base_class.observer import Subscriber

class ModeListMain(Frame, Subscriber):
    def __init__(self, master, mode_list: List[Mode], *args, **kwargs) -> None:
        Frame.__init__(self, master, *args, **kwargs)
        Subscriber.__init__(self)

        scrollbar = Scrollbar(self)
        scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self, yscrollcommand=scrollbar.set, width=0, height=0)
        for i, mode in enumerate(mode_list):
            self.listbox.insert(i, f"{mode.name}")

        scrollbar["command"]=self.listbox.yview
        self.listbox.pack(side="left", anchor="nw", expand=True, fill="both")
