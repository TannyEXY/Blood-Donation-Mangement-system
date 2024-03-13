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
            self.geometry("900x650")
            self.config(bg ="#161C25")
            self.resizable(False,False)
            self.font1 = ("Arial",20,'bold')
            self.font2 = ("Arial",12,'bold')
            self.font4= ("Arial",60,'bold')
            self.color = "#161C25"


            self.tempUsername = ''



            # Frames
            self.frame1 = customtkinter.CTkFrame(self,bg_color=self.color,width=700,height=480,corner_radius=200)
            self.frame1.place(x=105,y=-380)

            self.frame = customtkinter.CTkFrame(self,bg_color=self.color,width=700,height=480,corner_radius=200)
            self.frame.place(x=105,y=130)

            # label
            self.lbl = customtkinter.CTkLabel(self.frame1,text='Main Menu',font=self.font4, text_color='#161c25')
            self.lbl.place(x=200,y=390)

            #Creating the Buttons that will navigate the system
            self.donationMenu = customtkinter.CTkButton(self.frame,font=self.font1,text_color='#fff',text='Donations',command=self.donation,
                                                hover_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.donationMenu.place(x=100,y=130)

            self.patientMenu = customtkinter.CTkButton(self.frame,font=self.font1,text_color='#fff',text='Patients',command=self.patients,
                                                hover_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.patientMenu.place(x=400,y=130)

            self.reportsMenu = customtkinter.CTkButton(self.frame,font=self.font1,text_color='#fff',text='Reports',command=self.Reports,
                                                hover_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.reportsMenu.place(x=100,y=250)

            self.bloodrecordsMenu = customtkinter.CTkButton(self.frame,font=self.font1,text_color='#fff',text='Blood Records',
                                                            command=self.bloodRecords, hover_color='#161c25',cursor="hand2",corner_radius=15,width=200,height=80)
            self.bloodrecordsMenu.place(x=400,y=250)

            self.logOut= customtkinter.CTkButton(self.frame,font=self.font1,text_color='#fff',text='Log out',hover_color='#161c25',
                                            cursor="hand2",corner_radius=15,width=200,height=80,command=self.logout)
            self.logOut.place(x=250,y=370)

            self.userMenu= customtkinter.CTkButton(self.frame,font=self.font1,text_color='#fff',text='Users',hover_color='#161c25',
                                            cursor="hand2",corner_radius=50,width=100,height=50, command=self.userReg)
            self.userMenu.place(x=300,y=35)

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
             app.tempUsername = self.tempUsername
             app.mainloop()


        def patients(self):
             self.destroy()
             from patients import patientsMenu
             app = patientsMenu()
             app.mainloop()



        def bloodRecords(self):
            self.destroy()
            from bloodbank import bloodbank
            app = bloodbank()
            app.mainloop()

        def donation(self):
             self.destroy()
             from donation import donation
             app = donation()
             app.mainloop()
        
        def Reports(self):
             messagebox.showinfo('Blood Donation System', 'Design for this menu has not yet been planned.')


#running the menu
if __name__ == "__main__":
    app = main_Menu()
    app.mainloop()    