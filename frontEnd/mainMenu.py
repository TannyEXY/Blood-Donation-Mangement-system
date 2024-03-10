from typing import Tuple
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class main_Menu(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.title("Main Menu")
            self.geometry("900x550")
            self.config(bg ="#161C25")
            self.resizable(False,False)
            self.font1 = ("Arial",20,'bold')
            self.font2 = ("Arial",12,'bold')

            #Creating the Buttons that will navigate the system
            self.donationMenu = customtkinter.CTkButton(self,font=self.font1,text_color='#fff',text='Donations',
                                                hover_color="#FF5002",bg_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.donationMenu.place(x=200,y=130)

            self.patientMenu = customtkinter.CTkButton(self,font=self.font1,text_color='#fff',text='Patients',command=self.patients,
                                                hover_color="#FF5002",bg_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.patientMenu.place(x=500,y=130)

            self.reportsMenu = customtkinter.CTkButton(self,font=self.font1,text_color='#fff',text='Reports',
                                                hover_color="#FF5002",bg_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.reportsMenu.place(x=200,y=250)

            self.bloodrecordsMenu = customtkinter.CTkButton(self,font=self.font1,text_color='#fff',text='Blood Records',
                                                    hover_color="#FF5002",bg_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.bloodrecordsMenu.place(x=500,y=250)

            self.logOut= customtkinter.CTkButton(self,font=self.font1,text_color='#fff',text='Log out',hover_color="#FF5002",
                                            bg_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80,command=self.logout)
            self.logOut.place(x=350,y=370)

            self.userMenu= customtkinter.CTkButton(self,font=self.font1,text_color='#fff',text='Users',hover_color="#FF5002",
                                            bg_color='#161c25',cursor="hand2",corner_radius=50,width=100,height=80, command=self.userReg)
            self.userMenu.place(x=380,y=10)



        #Creating the funtionalities of the Buttons
        def logout(self):
            response = messagebox.askyesno("Blood Donation System", "Are you sure, you want to log out?")
            if response == True:
                self.destroy()
                from logIn import login
                app= login()
                app.mainloop()
        

        def userReg(self):
             self.destroy()
             from userRegistration import Registration
             app = Registration()
             app.mainloop()

        def patients(self):
             self.destroy()
             from patients import patientsMenu
             app = patientsMenu()
             app.mainloop() 


#running the menu
if __name__ == "__main__":
    app = main_Menu()
    app.mainloop()    