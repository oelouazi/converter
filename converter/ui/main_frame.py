import os
from tkinter import Frame, Menu, BOTH
from tkinter.filedialog import askopenfilename

from converter.task.image_convert_task import ImageConvertTask
from converter.task.task_manager import TaskManager
from converter.ui.component.task_component import TaskComponent


class MainFrame(Frame):
    """
    Represents the main frame implementation.
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.__setup_menu()
        self.__task_manager = TaskManager()
        self.pack(fill=BOTH, padx=10, pady=10, expand=True)

    def __setup_menu(self):
        """
        Setup menu bar in current frame.
        """
        menu = Menu(self)
        menu.add_command(label='File', command=self.__ask)
        menu.add_command(label='Run', command=self.__run)
        self.master.config(menu=menu)

    def __ask(self):
        """
        Open a dialog to select a file to process.
        """
        input_path = askopenfilename(title="Add an image file", filetypes=[
            ('PNG files', '.png'),
            ('BMP files', '.bmp'),
            ('TIF files', '.tif'),
            ('GIF files', '.gif'),
            ('TGA files', '.tga')
        ])
        ext = 'jpg'
        if input_path:
            f, e = os.path.splitext(input_path)
            output_path = f'{f}.{ext}'
            task = self.__task_manager.add_task(ImageConvertTask(input_path, output_path))
            TaskComponent(self, task=task)

    def __run(self):
        """
        Run all image file convertion.
        """
        self.__task_manager.start()
