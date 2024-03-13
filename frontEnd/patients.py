# creating the log in interface
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Backend.dbManager import patientsDB, nextkinDB

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
       self.font4= ("Arial",60,'bold')

      #  frames
       self.framePatient = customtkinter.CTkFrame(self, width=345, height=400)
       self.framePatient.place(x=20,y=80)

       self.frameNextofkin = customtkinter.CTkFrame(self, width=345, height=200)
       self.frameNextofkin.place(x=20, y=490)
       
       self.framebtn = customtkinter.CTkFrame(self, width=530, height=130)
       self.framebtn.place(x=380, y=560)

      # Menu tag
       self.lblmeasage = customtkinter.CTkLabel(self,text='Patients',bg_color=self.color, text_color='#161C65',font=self.font4,
                                                 corner_radius=100)
       self.lblmeasage.place(x=400,y=5) 

      #  frame labels
       self.framelbl =customtkinter.CTkLabel(self,text="Patient",font=self.font1,bg_color=self.color)
       self.framelbl.place(x=30,y=80)

       self.framelbl =customtkinter.CTkLabel(self,text="Next of kin",font=self.font1,bg_color=self.color)
       self.framelbl.place(x=30, y=490)



      #  creating a new instance of the patients DB handler
       self.patientsDB_handler = patientsDB()
       self.nextofkinDB_handler = nextkinDB()

      #  labling the textboxes
       y_axis = 50
       nlLabelname = ["First Name :", "Last Name :","Phone :"]
       for lablename in nlLabelname:
           self.nkLabel = customtkinter.CTkLabel(self.frameNextofkin, text=lablename, font=self.font2)
           self.nkLabel.place(x=10,y=y_axis)
           y_axis += 50



       y_axis = 50
       
       labelnames = ["First Name :", "Last Name :","Gender :", "Phone :","National ID :","Date of Birth :","Home Address :"]

       for lablename in labelnames:
           self.pnameLabel = customtkinter.CTkLabel(self.framePatient, text=lablename, font=self.font2)
           self.pnameLabel.place(x=10,y=y_axis)
           y_axis += 50

       self.textbox = []
       y_axis = 50

       # Varibles for the textboxes
       self.txtname = StringVar()
       self.txtlname = StringVar()
       self.txtgender = StringVar()
       self.txtphone = StringVar()
       self.txtnationid = StringVar()
       self.txtdob = StringVar()
       self.txthome = StringVar()

       self.txtnkname = StringVar()
       self.txtnklname = StringVar()
       self.txtnkcontact = StringVar()

       self.nktxtvariables = [self.txtnkname,
                              self.txtnklname,
                              self.txtnkcontact
                              ]
      
       self.nktextbox = [""] * 4
       y_axis = 50

       for num in range(len(self.nktxtvariables)):
           self.nktextbox[num]=customtkinter.CTkEntry(self.frameNextofkin, width=200,textvariable=self.nktxtvariables[num],
                                                      placeholder_text= "", font=self.font2, corner_radius=5)
           self.nktextbox[num].place(x=120,y=y_axis)
           y_axis += 50


       y_axis = 50



       self.nextofkinrecords = []
       self.patientsRecords = []

       self.textboxvariables = [self.txtname,self.txtlname, self.txtgender,self.txtphone,self.txtnationid,self.txtdob,self.txthome]
       self.Namesearch = StringVar()

       self.textbox = [""] * 8


       # Creating textboxes on the interface
       for num in range(len(labelnames)):
           if num == 2:
               self.textbox[num]=customtkinter.CTkComboBox(self.framePatient, width=200,
                                                      font=self.font2, corner_radius=5)
               self.textbox[num].place(x=120,y=y_axis)
               self.textbox[num].configure(values=["Male", "Female"])
               self.textbox[num].set("Select")
               y_axis += 50
               continue
           if num == 5:
               self.textbox[num]=customtkinter.CTkEntry(self.framePatient, width=200,textvariable=self.textboxvariables[num],
                                                       font=self.font2, corner_radius=5)
               self.textbox[num].place(x=120,y=y_axis)
               self.textboxvariables[num].set("yyyy-mm-dd")
               
               
               y_axis += 50
               continue
           
               
           self.textbox[num]=customtkinter.CTkEntry(self.framePatient, width=200,textvariable=self.textboxvariables[num],
                                                      placeholder_text= "", font=self.font2, corner_radius=5)
           self.textbox[num].place(x=120,y=y_axis)
           y_axis += 50




           
      #  Frame tablee
       self.frame = customtkinter.CTkScrollableFrame(self, width=850, height=300, bg_color=self.color, corner_radius=10)
       self.frame.place(x=370, y=150)

       self.Tree = ttk.Treeview(self.frame, height= 19)
      #  defining the Columns name
       self.Tree["show"] = "headings"

       self.Tree["columns"] = ("Reg number","First Name", "Last Name","Gender", "Phone",
                               "National ID","Date of Birth","Home Address")
       

       self.Tree.column("Reg number",width=80, minwidth=50,anchor=tk.CENTER)
       self.Tree.column("First Name",width=150, minwidth=50,anchor=tk.CENTER)
       self.Tree.column("Last Name",width=150, minwidth=50,anchor=tk.CENTER)
       self.Tree.column("Gender",width=100, minwidth=50,anchor=tk.CENTER)
       self.Tree.column("Phone",width=100, minwidth=50,anchor=tk.CENTER)
       self.Tree.column("Date of Birth",width=150, minwidth=50,anchor=tk.CENTER)
       self.Tree.column("National ID",width=150, minwidth=50,anchor=tk.CENTER)
       self.Tree.column("Home Address",width=200, minwidth=50,anchor=tk.CENTER)

      # regnumber, name,lname,gender,phone,nationalid,dob,homeaddress
       self.Tree.heading("Reg number",text="Reg number")
       self.Tree.heading("First Name",text="First Name")
       self.Tree.heading("Last Name",text="Last Name")
       self.Tree.heading("Gender",text="Gender")
       self.Tree.heading("Phone",text="Phone")
       self.Tree.heading("Date of Birth",text="Date of birth")
       self.Tree.heading("National ID",text="National ID")
       self.Tree.heading("Home Address",text="Home Address")
       

       self.Tree.pack(padx=0,pady=5)




      # buttons
       self.Addbtn = customtkinter.CTkButton(self.framebtn, text="ADD NEW", bg_color= self.color,font=self.font2,command=self.AddNewPatient,
                                             cursor="hand2")
       self.Addbtn.place(x=50,y=20)

       self.Savebtn = customtkinter.CTkButton(self.framebtn, text="SAVE", bg_color= self.color,font=self.font2,command=self.saveData,
                                              cursor="hand2")
       self.Savebtn.place(x=200,y=20)

       self.Updatebtn = customtkinter.CTkButton(self.framebtn, text="UPDATE", bg_color= self.color,font=self.font2,command=self.updateData,
                                                cursor="hand2")
       self.Updatebtn.place(x=350,y=20)

       self.Cancelbtn = customtkinter.CTkButton(self.framebtn, text="Cancel", bg_color= self.color,font=self.font2,command=self.cancel,
                                                cursor="hand2")
       self.Cancelbtn.place(x=50,y=70)

       self.logoutbtn = customtkinter.CTkButton(self.framebtn, text="Log out", bg_color= self.color,font=self.font2,command=self.logout,
                                                cursor="hand2")
       self.logoutbtn.place(x=200,y=70)

       self.Backbtn = customtkinter.CTkButton(self.framebtn, text="Back", bg_color= self.color,font=self.font2, command= self.mainMenu
                                              ,cursor="hand2")
       self.Backbtn.place(x=350,y=70)



      #  Buttons next to search bar
       self.Deletebtn = customtkinter.CTkButton(self, text="Delete", height=20,width=60,command=self.deleteRecord,
                                                 bg_color= self.color,font=self.font2,cursor="hand2")
       self.Deletebtn.place(x=900,y=100)

       self.AddKinbtn = customtkinter.CTkButton(self, text="Next of Kin", height=20,width=60,command=self.nextofkin,
                                                 bg_color= self.color,font=self.font2,cursor="hand2")
       self.AddKinbtn.place(x=965,y=100)

       self.diagnosisbtn = customtkinter.CTkButton(self, text="Diagnosis", height=20,width=60,command=self.diagnosis,
                                                   bg_color= self.color,font=self.font2,cursor="hand2")
       self.diagnosisbtn.place(x=1045,y=100)

       self.Editbtn = customtkinter.CTkButton(self, text="Edit", height=20,width=60, bg_color= self.color,command=self.editData,
                                              font=self.font2,cursor="hand2")
       self.Editbtn.place(x=835,y=100)


      #  search textbox and search label
       self.lblsearch = customtkinter.CTkLabel(self, bg_color="#161C25", width=200, text="Enter Full name :",
                                                      font=self.font2, corner_radius=5)
       self.lblsearch.place(x=380, y=100)

       self.txtsearch = customtkinter.CTkEntry(self, bg_color="#161C25", width=200, textvariable=self.Namesearch,
                                                      font=self.font2, corner_radius=5)
       self.txtsearch.place(x=550, y=100)

      #  message labels
       self.lblRecords = customtkinter.CTkLabel(self.framePatient,text_color='red', text="",
                                                      font=self.font2, corner_radius=5)
       self.lblRecords.place(x=120, y=15)

       self.lblRecordsNumber = customtkinter.CTkLabel(self.framePatient,text_color='red', text="",
                                                      font=self.font2, corner_radius=5)
       self.lblRecordsNumber.place(x=95, y=15)



      #  search button
       self.searchbtn = customtkinter.CTkButton(self, text="Search", height=20,width=60,command=self.Search, 
                                                bg_color= self.color,font=self.font2,cursor="hand2")
       self.searchbtn.place(x=770,y=100)

       
       
      #  diplaying the data in the list the moment the app opens
       self.displaylist()


   def nextofkin(self):
      messagebox.showinfo('Blood Donation System', 'Menu Not designed yet!')

   def Search(self):
       name = self.Namesearch.get()
       data = name.split(" ", 2)
      #  print(data)
       records = []
       if len(data) > 1:
           records = self.patientsDB_handler.searchPatient(data[0],data[1])
       else:
           records = self.patientsDB_handler.searchPatient(data[0])
       self.DisplayData(records)

   def displaylist(self):
      # print(self.patientsDB_handler.display())
      records = self.patientsDB_handler.display()
      self.DisplayData(records)

   def DisplayData(self,records):
      self.Tree.destroy()
      self.Tree = ttk.Treeview(self.frame, height= 19)
      #  defining the Columns name
      self.Tree["show"] = "headings"

      self.Tree["columns"] = ("Reg number","First Name", "Last Name","Gender", "Phone",
                               "National ID","Date of Birth","Home Address")
      self.Tree.column("Reg number",width=80, minwidth=50,anchor=tk.CENTER)
      self.Tree.column("First Name",width=150, minwidth=50,anchor=tk.CENTER)
      self.Tree.column("Last Name",width=150, minwidth=50,anchor=tk.CENTER)
      self.Tree.column("Gender",width=100, minwidth=50,anchor=tk.CENTER)
      self.Tree.column("Phone",width=100, minwidth=50,anchor=tk.CENTER)
      self.Tree.column("Date of Birth",width=150, minwidth=50,anchor=tk.CENTER)
      self.Tree.column("National ID",width=150, minwidth=50,anchor=tk.CENTER)
      self.Tree.column("Home Address",width=200, minwidth=50,anchor=tk.CENTER)


      self.Tree.heading("Reg number",text="Reg number")
      self.Tree.heading("First Name",text="First Name")
      self.Tree.heading("Last Name",text="Last Name")
      self.Tree.heading("Gender",text="Gender")
      self.Tree.heading("Phone",text="Phone")
      self.Tree.heading("Date of Birth",text="Date of birth")
      self.Tree.heading("National ID",text="National ID")
      self.Tree.heading("Home Address",text="Home Address")

      self.Tree.pack(padx=0,pady=5)
      
      i = 1
      for row in records:
          self.Tree.insert('',i,text='',values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
          i += 1
      pass
   
   def AddNewPatient(self):  
      values, nkdetails = self.collectData()
      self.clearText()

      self.nextofkinrecords.append(nkdetails)
      self.patientsRecords.append(values)
      print(self.nextofkinrecords)
      self.lblRecordsNumber.configure(text = len(self.patientsRecords), text_color= "red")
      self.displayMessage("Records added and need be saved.",'red')

   def displayMessage(self, message, color):
      if len(self.patientsRecords) == 1:
         self.lblRecords.configure(text=message.replace("Records", "Record"), text_color = color)
      else:
         self.lblRecords.configure(text=message, text_color= color)

   def saveData(self):
       try:
         i = 0      
         # saving all the records on the list
         for record in self.patientsRecords:
            self.patientsDB_handler.savePatient(record)
            self.nextofkinDB_handler.saveKin(self.nextofkinrecords[i])
            print(self.patientsRecords[i], "    ",self.nextofkinrecords[i])
            i +=1

            

         # display message
         self.displayMessage('Records saved.','green')
         self.lblRecordsNumber.configure(text = len(self.patientsRecords), text_color= "green")

         # emptying the patientslist list
         self.patientsRecords = []
         self.nextofkinrecords = []
         self.displaylist()

       except Exception as erro:
         self.lblRecords.configure(text=f'{erro}', text_color='red')

   def deleteRecord(self):

      result = messagebox.askyesno('Blood Donation System','Are you sure you want to delete this record?')
      if result == True:
         data = self.item_selected()
         try:
            self.patientsDB_handler.deletePatient(data[0])
         except Exception as erro:
            self.displayMessage(erro,'red')
         self.displaylist()
         # print(data[0])

   def item_selected(self):
      record = []
      try:
            
         for selected_item in self.Tree.selection():
            item = self.Tree.item(selected_item)
            record = item['values']

      except:
         
         print('no selected values')

      finally:
         return record

   def editData(self):
      data = self.item_selected()
      self.regnumber = data[0]
      num = 0
      checked = False
      for value in data:
         if not checked:
            checked = True
            continue
         else:
            if num != 2:
               self.textboxvariables[num].set(value)
            else:
               self.textbox[num].set(value)
            num +=1

   def updateData(self):
      data = self.collectData()
      print(data)
      self.patientsDB_handler.updatePatient(data,self.regnumber)
      self.displaylist()
      self.clearText()

   def collectData(self):
      i = 0
      values = []
      details = []
      for txtbox in self.textboxvariables:
           if  i == 2:
               values.append(self.textbox[2].get())
           elif i != 2 and txtbox.get() != "":
               values.append(txtbox.get())
           i += 1

      for txtbox in self.nktxtvariables:
         details.append(txtbox.get())
      details.append(self.textboxvariables[6].get())

      details[2],details[3] = details[3],details[2]

      return values, details

   def clearText(self):
      i = 0
      for txtbox in self.textboxvariables:
         if  i == 2:
            self.textbox[2].set('Select')
         elif i != 2 and txtbox.get() != "":
            txtbox.set("")
         i += 1
      self.textboxvariables[5].set("yyyy-mm-dd")

      for txtbox in self.nktxtvariables:
         txtbox.set('')
   
   def cancel(self):
      result = messagebox.askyesno('Blood Donation System', 'Are you sure you wiish to cancel records added.')
      if result == True:
         self.clearText()
         self.lblRecordsNumber.configure(text='',text_color='green')
         self.displayMessage("All records cancelled.",'green')
         self.patientsRecords = []

   def logout(self):
      self.destroy()
      from logIn import login
      app = login()
      app.mainloop()
   
   def mainMenu(self):
      self.destroy()
      from mainMenu import main_Menu
      app= main_Menu()
      app.mainloop()   

   def diagnosis(self):
      data = self.item_selected()
      self.destroy()
      from capturediagnosis import diagnosisCapture
      app = diagnosisCapture()
      if len(data) > 0:  app.search(data[0])
      app.mainloop()
      
      

if __name__ == "__main__":
    papp = patientsMenu()
    papp.mainloop()
    