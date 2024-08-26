from typing import List
from tkinter import Frame, StringVar

from ..base_class.observer import Subscriber, Observer
from ..models.mode import Mode
from ..component.mode_list_top import ModeListTop
from ..component.mode_list_main import ModeListMain

class ModeDescriptionView(Frame, Subscriber, Observer):
    def __init__(self, master, radio_var: StringVar, mode_list: List[Mode], *args, **kwargs) -> None:
        Frame.__init__(self, master, *args, **kwargs)
        Subscriber.__init__(self)

        self.mode_list_top = ModeListTop(self, radio_var)
        self.mode_list_top.addObserver(self)
        self.mode_list_top.pack(anchor="nw")

        self.mode_list_main = ModeListMain(self, mode_list)
        self.mode_list_main.addObserver(self)
        self.mode_list_main.pack(expand=True, fill="both")

    def update(self):
        # 여기서 하기에 따라 ModeListTop 이나 ModeListMain 에 정보 전달 가능
        self.notify()
