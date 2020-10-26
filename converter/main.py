from tkinter import *

from ttkthemes import ThemedStyle

from converter.ui.main_frame import MainFrame


def main():
    """An image file converter"""
    # Create a root frame
    root = Tk()
    root.title('Converter')

    # Change style to be more elegant
    style = ThemedStyle(root)
    style.set_theme("breeze")

    # Setup main frame
    frame = MainFrame(master=root)
    frame.mainloop()


if __name__ == '__main__':
    main()
