
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mainMenu
from Backend.dbManager import loginDB

class Registration(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("600x380")
        self.config(bg ="#161C25")
        self.resizable(False,False)
        self.userDB = loginDB()

        self.font1 = ("Arial",20,'bold')
        self.font2 = ("Arial",40,'bold')
        self.font5 = ("Arial",14,'bold')
        self.font3 = ("Times New Roman",16,'bold')
        self.attempts = 3

        self.username = StringVar()
        self.password = StringVar()
        self.cpassword = StringVar()

        self.tempUsername = ''


        self.logo = customtkinter.CTkLabel(self,font=self.font2,text="User Registration",bg_color="#161C25")
        self.logo.place(x=120,y=50)

        self.usernamelabel = customtkinter.CTkLabel(self,font=self.font1,text="Username : ",bg_color="#161C25")
        self.usernamelabel.place(x=80,y=150)

        self.passwordlabel = customtkinter.CTkLabel(self,font=self.font1,text="Password : ",bg_color="#161C25")
        self.passwordlabel.place(x=80,y=200)

        self.usernameText = customtkinter.CTkEntry(self, width=250, height=30, corner_radius=12,
                                                   textvariable=self.username)
        self.usernameText.place(x= 230, y=150)

        self.passwordText = customtkinter.CTkEntry(self, width=250, height=30, corner_radius=12,
                                                   textvariable=self.password,show = "*")
        self.passwordText.place(x= 230, y=200)

        self.cpasswordText = customtkinter.CTkEntry(self, width=250, height=30, corner_radius=12,
                                                    textvariable=self.cpassword,show = "*")
        self.cpasswordText.place(x= 230, y=250)

        self.cpasswordlabel = customtkinter.CTkLabel(self,font=self.font5,text="Confirm Password : ",bg_color="#161C25")
        self.cpasswordlabel.place(x=80,y=250)     


        self.loginbtn = customtkinter.CTkButton(self,text="Register",font=self.font3, width=100,border_color="#fff",
                                                corner_radius=15, command=self.save)
        self.loginbtn.place(x=360,y= 320)

        self.closebtn = customtkinter.CTkButton(self,text="Back",font=self.font3, width=100,border_color="#fff",
                                                corner_radius=15,command=self.close)
                                                
        self.closebtn.place(x=240,y= 320)

        self.resultlabel = customtkinter.CTkLabel(self,font=self.font5,bg_color="#161C25", text="")
        self.resultlabel.place(x=1,y=1)

        print(self.tempUsername)


    def createMessageLabel(self, message, x1=100, y1=280, colour="red"):
        self.resultlabel = customtkinter.CTkLabel(self,font=self.font5,text=f"{message}",bg_color="#161C25",text_color=colour)
        self.resultlabel.place(x=x1,y=y1)

    def save(self):
        self.resultlabel.destroy()
        username = self.username.get()
        password = self.password.get()
        cpassword = self.cpassword.get()
       
        if cpassword != password:
            self.createMessageLabel("Passwords do not match! Please try again.")
        else:
            try:
                self.userDB.saveDeatails(username,password)
                self.createMessageLabel(message="Record Saved.",colour="green",x1=320,y1=280)
                
            except Exception as message:
                self.resultlabel = customtkinter.CTkLabel(self,font=self.font5,text=f"{message}",bg_color="#161C25",
                                                  text_color="green")
                self.resultlabel.place(x=100,y=280)
                

    def close(self):
        respose = messagebox.askyesno("Donations System", "Are you sure you wish to go back?")
        print(self.tempUsername)
        if respose == 1:
            self.destroy()
            from mainMenu import main_Menu
            app = main_Menu()
            app.mainloop()



if __name__ == "__main__":
    app = Registration()
    app.mainloop()