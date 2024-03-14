from typing import Tuple
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class nextofKin(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("900x650")
        self.config(bg ="#161C25")
        self.resizable(False,False)
        self.font1 = ("Arial",20,'bold')
        self.font2 = ("Arial",12,'bold')
        self.font4= ("Arial",60,'bold')
        self.color = "#161C25"

        # Frame 
        # self.frame =  





if __name__ == "__main__":
    app = nextofKin()
    app.mainloop()