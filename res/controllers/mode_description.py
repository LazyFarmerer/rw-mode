from typing import List
from tkinter import Frame, StringVar, Label

from ..base_class.observer import Observer
from ..models.mode import Mode
from ..models.file import File
from ..base_class.mode_type import ModeType
from ..views.mode_description import ModeDescriptionView


class ModeDescriptionController(Frame, Observer):
    def __init__(self, master, *args, **kwargs) -> None:
        Frame.__init__(self, master, *args, **kwargs)
        Observer.__init__(self)

        # 사용될 변수들
        self.memory_mode_type: str = ModeType.local.name # 기억해 뒀다가 변경 있으면 변경, 쓸데없는 새로고침 방지
        self.radio_var = StringVar(value=ModeType.local.name)
        self.mode_list: List[Mode] = File.read_modes(ModeType.local)


        # View 구독
        self._view = ModeDescriptionView(master=self, radio_var=self.radio_var, mode_list=self.mode_list)
        self._view.addObserver(self)
        self._view.pack(expand=True, fill="both")

        self._view.mode_list_main.listbox.bind("<Double-Button-1>", self._select_mode)

    @property
    def view(self):
        return self._view

    def update(self):
        # 변경 없으면 조기리턴, 쓸데없는 업데이트 방지
        if self.memory_mode_type == self.radio_var.get():
            return

        # 변경이 있을 경우 리스트 초기화 하고 다시 넣기
        self.memory_mode_type = self.radio_var.get()
        match self.memory_mode_type:
            case ModeType.local.name:
                print("로컬로 변환")
                self.mode_list.clear()
                self.mode_list = File.read_modes(ModeType.local)
            case ModeType.steem.name:
                print("스팀으로 변환")
                self.mode_list.clear()
                self.mode_list = File.read_modes(ModeType.steem)
            case _:
                raise ValueError("뭐가 들어간거임??")

        size: int = self._view.mode_list_main.listbox.size()
        self._view.mode_list_main.listbox.delete(0, size)
        for index, mode in enumerate(self.mode_list):
            self._view.mode_list_main.listbox.insert(index, mode.name)

    def _select_mode(self, event):
        index = self._view.mode_list_main.listbox.curselection()[0]
        print(self.mode_list[index])