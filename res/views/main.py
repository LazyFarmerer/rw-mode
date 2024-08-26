from tkinter.ttk import Notebook

from ..base_class.root import Root
from ..controllers.mode_description import ModeDescriptionController

class Window(Root):
    def __init__(self):
        super().__init__()

        self.book = Notebook(self)
        self.book.pack(expand=True, fill="both")

        mode_description = ModeDescriptionController(self)

        self.book.add(mode_description, text="모드리스트")


        self.mainloop()