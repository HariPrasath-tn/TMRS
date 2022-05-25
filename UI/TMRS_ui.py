"""
    Traditional medicine recommendation system main window ui
"""

from tkinter import *
from tkinter import ttk, messagebox

global mainWindow


class HomeUi:
    def __init__(self, window):
        self.home = window
        self.left_up = LabelFrame(self.home, width="749", height="549", bd=4)
        self.left_up.grid(row=0, column=0)
        self.left_down = LabelFrame(self.home, width="749", height="349", bd=4)
        self.left_down.grid(row=1, column=0)
        self.right_up = LabelFrame(self.home, width="749", height="898", bd=4)
        self.right_up.grid(row=0, column=1, rowspan=2)
        self.home.mainloop()


mainWindow = Tk()
mainWindow.title("Traditional medicine recommendation system")
mainWindow.geometry("1500x900")
if __name__ == "__main__":
    home_ui = HomeUi(mainWindow)
