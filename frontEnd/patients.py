# creating the log in interface
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
# from Backend.dbManager import patients



class patientsMenu(customtkinter.CTk):
   def __init__(self):
       super().__init__()

       self.title("Patients")
       self.geometry("1266x720")
       self.config(bg ="#161C25")
    #  self.resizable(False,False)
       self.color = "#161C25"

       self.font1 = ("Arial",20,'bold')
       self.font2 = ("Arial",12,'bold')

      #  labling the textboxes
       y_axis = 150
       
       labelnames = ["First Name :", "Last Name :","Gender :", "Phone :","National ID :","Date of Birth :","Home Address :"]


       for lablename in labelnames:
           self.pnameLabel = customtkinter.CTkLabel(self, text=lablename,bg_color="#161C25", font=self.font2)
           self.pnameLabel.place(x=50,y=y_axis)
           y_axis += 50

       self.textbox = []
       y_axis = 150

       # Varibles containing the text
      #  self.value = 
       self.textboxvariables = [StringVar()] * (int(len(labelnames)))
       self.Namesearch = StringVar()






       # Creating textboxes on the interface
       for num in range(len(labelnames)):
           if num == 2:
               self.textbox.append(customtkinter.CTkComboBox(self, bg_color="#161C25", width=200,
                                                      font=self.font2, corner_radius=5))
               self.textbox[num].place(x=150,y=y_axis)
               self.textbox[num].configure(values=["Male", "Female"])
               self.textbox[num].set("Select")
               y_axis += 50
               continue
           
               
           self.textbox.append(customtkinter.CTkEntry(self,bg_color="#161C25", width=200,textvariable=self.textboxvariables[num],
                                                      placeholder_text= "", font=self.font2, corner_radius=5))
           self.textbox[num].place(x=150,y=y_axis)
           y_axis += 50



           
      #  Frame table to show the results that will have been added
       self.frame = customtkinter.CTkFrame(self, width=800, height=300, bg_color="grey")
       self.frame.place(x=400, y=150)

       self.Tree = ttk.Treeview(self.frame, height= 15)
       self.Tree.pack(padx=0,pady=5)





      # buttons
       self.Addbtn = customtkinter.CTkButton(self, text="ADD NEW", bg_color= self.color,font=self.font1,cursor="hand2")
       self.Addbtn.place(x=50,y=500)

       self.Savebtn = customtkinter.CTkButton(self, text="SAVE", bg_color= self.color,font=self.font1,cursor="hand2")
       self.Savebtn.place(x=200,y=500)

       self.Updatebtn = customtkinter.CTkButton(self, text="UPDATE", bg_color= self.color,font=self.font1,cursor="hand2")
       self.Updatebtn.place(x=350,y=500)

       self.Backbtn = customtkinter.CTkButton(self, text="Back", bg_color= self.color,font=self.font1,cursor="hand2")
       self.Backbtn.place(x=50,y=550)

       self.logoutbtn = customtkinter.CTkButton(self, text="Log out", bg_color= self.color,font=self.font1,cursor="hand2")
       self.logoutbtn.place(x=200,y=550)

      #  Buttons next to search bar
       self.Deletebtn = customtkinter.CTkButton(self, text="Delete", height=20,width=60, bg_color= self.color,font=self.font2,cursor="hand2")
       self.Deletebtn.place(x=900,y=100)

       self.Editbtn = customtkinter.CTkButton(self, text="Edit", height=20,width=60, bg_color= self.color,font=self.font2,cursor="hand2")
       self.Editbtn.place(x=835,y=100)


      #  search textbox and search label
       self.lblsearch = customtkinter.CTkLabel(self, bg_color="#161C25", width=200, text="Enter Full name :",
                                                      font=self.font2, corner_radius=5)
       self.lblsearch.place(x=380, y=100)

       self.txtsearch = customtkinter.CTkEntry(self, bg_color="#161C25", width=200, textvariable=self.Namesearch,
                                                      font=self.font2, corner_radius=5)
       self.txtsearch.place(x=550, y=100)



      #  searh button
       self.searchbtn = customtkinter.CTkButton(self, text="Search", height=20,width=60, bg_color= self.color,font=self.font2,cursor="hand2")
       self.searchbtn.place(x=770,y=100)


   def displaylist(self):
      
      
      pass



       



       
    






if __name__ == "__main__":
    papp = patientsMenu()
    papp.mainloop()
    