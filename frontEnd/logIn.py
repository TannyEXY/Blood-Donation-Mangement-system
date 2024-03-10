# creating the database and the system tables to be used by the program
from Backend.databaseCreater import initialiseDatabase
initialiseDatabase()

# creating the log in interface
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mainMenu
from Backend.dbManager import loginDB


class login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("500x350")
        self.config(bg ="#161C25")
        self.resizable(False,False)
        self.userDB = loginDB()

        self.font1 = ("Arial",20,'bold')
        self.font2 = ("Arial",50,'bold')
        self.font3 = ("Times New Roman",16,'bold')
        self.attempts = 3

        self.username = StringVar()
        self.password = StringVar()


        self.logo = customtkinter.CTkLabel(self,font=self.font2,text="Log In",bg_color="#161C25")
        self.logo.place(x=180,y=50)

        self.usernamelabel = customtkinter.CTkLabel(self,font=self.font1,text="Username : ",bg_color="#161C25")
        self.usernamelabel.place(x=80,y=150)

        self.passwordlabel = customtkinter.CTkLabel(self,font=self.font1,text="Password : ",bg_color="#161C25")
        self.passwordlabel.place(x=80,y=200)

        self.usernameText = customtkinter.CTkEntry(self, width=250, height=30, corner_radius=12,textvariable=self.username)
        self.usernameText.place(x= 230, y=150)

        self.passwordText = customtkinter.CTkEntry(self, width=250, height=30, corner_radius=12,show ="*"
                                                   ,textvariable=self.password)
        self.passwordText.place(x= 230, y=200)


        self.loginbtn = customtkinter.CTkButton(self,text="log in",font=self.font3, width=100,border_color="#fff",
                                                corner_radius=15,command=self.checkpassword)
        self.loginbtn.place(x=360,y= 250)

        self.closebtn = customtkinter.CTkButton(self,text="Close",font=self.font3, width=100,border_color="#fff",
                                                corner_radius=15,command=self.close)
                                                
        self.closebtn.place(x=240,y= 250)


    def checkpassword(self):
        username = self.username.get()
        password = self.password.get()
        data = self.userDB.getLogInDeatails(username,password)
        if len(data) > 0:
            self.destroy()
            from mainMenu import main_Menu
            self.app = main_Menu()
            self.app.mainloop()
        else:
            self.attempts -= 1
            if self.attempts == 0:
                self.destroy()
            else:
                messagebox.showwarning("Donation Management System",f"Incorrect password or username! {self.attempts} attempts left of 3.\nThe program will close after 3 failed attempts.")
        
        # pass

    def close(self):
        respose = messagebox.askyesno("Donations System", "Are you sure you wish to exit?")
        if respose == True:
            self.destroy()


if __name__ == "__main__":

    app = login()
    app.mainloop()