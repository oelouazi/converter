from threading import RLock
from tkinter import HORIZONTAL, Label, X, Frame, LEFT
from tkinter.ttk import Progressbar


class TaskComponent(Frame):
    """
    Represents a task renderable component.
    """

    def __init__(self, master, task):
        """
        Create a new task component.
        :param master: parent component.
        :param task: task attached.
        """
        super().__init__(master)
        self.__lock = RLock()
        self.__task = task
        self.__task.on_update(self.on_update)
        self.__setup_components()
        self.pack(fill=X, pady=(0, 10))

    def on_update(self):
        """
        Method to run each update.
        """
        with self.__lock:
            self.__progressbar['value'] = self.__task.progress()
            self.__state_label['text'] = f'pourcentage: {self.__task.progress()}%'

    def __setup_components(self):
        """
        Setup all components.
        """
        # Setup description label
        self.__description_label = Label(self, text=self.__task.input_path(), anchor="w", justify=LEFT)
        self.__description_label.pack(fill=X)

        # Setup progressbar
        self.__progressbar = Progressbar(self, orient=HORIZONTAL, length=100, mode='determinate')
        self.__progressbar.pack(fill=X)

        # Setup state label.
        self.__state_label = Label(self, anchor="w", justify=LEFT)
        self.__state_label.pack(fill=X)

        # Trigger update
        self.on_update()
