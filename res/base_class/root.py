from tkinter import Tk

class Root(Tk):
    def __init__(self):
        super().__init__()

        width = 700
        # min_width = 500
        height = 500
        # min_height = 300

        self.geometry(f"{width}x{height}")
        # self.maxsize(width=height+100, height=height+100)
        # self.minsize(width=height-100, height=height-100)
        self.title("모드 수정")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)