# creating the Diagnosis interface
from typing import Tuple
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class diagnosisCapture(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Patients")
        self.geometry("1266x720")
        self.config(bg ="#161C25")
        self.resizable(False,False)
        self.color = "#161C25"

        self.font1 = ("Arial",20,'bold')
        self.font2 = ("Arial",12,'bold')
        self.font3 = ("Arial",11,'bold')

        self.createDiagnostics()


    def createDiagnostics(self):
        self.frame = customtkinter.CTkFrame(self,bg_color=self.color,width=570,height=300,corner_radius=10)
        self.frame.place(x=40,y=100)

        self.flamelabel = customtkinter.CTkLabel(self,bg_color=self.color,text=' -Diagnosis Deatails-')
        self.flamelabel.place(x=50,y=100)

        labelnames = ['Condition :','illness :','Blooad group :', 'Date Recorded :','Prescription :']

        column = 0
        x = 10
        y = 50
        for label in labelnames:
            if column == 2:
                y += 60
                x = 10
            elif column == 4:
                y += 60
                x = 10
            
            self.lbl = customtkinter.CTkLabel(self.frame,text=label,font =self.font3)
            self.lbl.place(x=x,y=y)
            x += 260
            column += 1

        self.condition = StringVar()
        self.illness = StringVar()
        self.bloodgroup = StringVar()
        self.daterecorded = StringVar()
        self.prescription = StringVar()


        # Creating textboxes
        self.txtcondition = customtkinter.CTkEntry(self.frame, width=160,font=self.font3, bg_color=self.color
                                                   ,textvariable=self.condition)
        self.txtcondition.place(x = 100,y=50)

        self.txtillness = customtkinter.CTkEntry(self.frame, width=160,font=self.font3, bg_color=self.color
                                                 ,textvariable=self.illness)
        self.txtillness.place(x = 370,y=50)

        self.txtbloodgroup = customtkinter.CTkEntry(self.frame, width=160,font=self.font3, bg_color=self.color
                                                    ,textvariable=self.bloodgroup)
        self.txtbloodgroup.place(x = 100,y=110)

        self.txtdaterecorded = customtkinter.CTkEntry(self.frame, width=160,font=self.font3, bg_color=self.color
                                                      ,textvariable=self.daterecorded)
        self.txtdaterecorded.place(x = 370,y=110)
        

        self.txtpresciption = customtkinter.CTkEntry(self.frame, width=160,font=self.font3, bg_color=self.color
                                                     ,textvariable=self.prescription)
        self.txtpresciption.place(x = 100,y=170)

        # Buttons

        self.addBtn = customtkinter.CTkButton(self.frame,text="ADD",width=100,font=self.font2)
        self.addBtn.place(x = 320, y=250)

        self.saveBtn = customtkinter.CTkButton(self.frame,text="SAVE",width=100,font=self.font2)
        self.saveBtn.place(x = 430, y=250)










if __name__ == '__main__':
    app = diagnosisCapture()
    app.mainloop()        