# creating the Diagnosis interface
from typing import Tuple
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Backend.dbManager import diagnosisDB

class diagnosisCapture(customtkinter.CTk):

    # constructor
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

        self.createDiagnosticsDetails()
        self.createbloodbankDetails()
        self.searchPatients()


        # variables
        self.regnumder = ''
        self.medicalid = ''
        self.diagnosisDB = diagnosisDB()
        
        
        # buttons
        self.backbtn = customtkinter.CTkButton(self, text='Back',font = self.font3,command=self.back, 
                                               width=90)
        self.backbtn.place(x=1070,y=670)

        self.logbtn = customtkinter.CTkButton(self, text='Log out',font = self.font3,command=self.logout,
                                               width=90)
        self.logbtn.place(x=970,y=670)

    # Blood Banks
    def createbloodbankDetails(self):
        # variables
        self.checkAssign = IntVar()
        self.searchBG =StringVar()


        # Frames
        self.Bloodbankframe = customtkinter.CTkFrame(self,bg_color=self.color,width=570,height=300,corner_radius=10)
        self.Bloodbankframe.place(x=640,y=80)

        self.framelabel = customtkinter.CTkLabel(self,bg_color=self.color,text=' -Blood Banks-')
        self.framelabel.place(x=670,y=80)

        self.Searchframe = customtkinter.CTkFrame(self.Bloodbankframe,bg_color=self.color,width=540,height=50,
                                                  corner_radius=5)
        self.Searchframe.place(x=10,y=40)

        self.Resultsframe = customtkinter.CTkFrame(self.Bloodbankframe,bg_color=self.color,width=540,height=170,
                                                  corner_radius=5)
        self.Resultsframe.place(x=10,y=100)

        # labels
        self.lblsearch = customtkinter.CTkLabel(self.Searchframe, text="Enter Blood Group : ")
        self.lblsearch.place(x=34,y=10)

        x=34
        y=10
        labelText = ['Blood Group :', 'Storage Location :', 'Amount (ml) :']
        for name in labelText:
            self.lblresult = customtkinter.CTkLabel(self.Resultsframe,text=name)
            self.lblresult.place(x=x,y=y)
            y += 50
           

        self.dashLines = '- - - - - - - - - - - - - - - - - - - - '
        self.lblresultBG = customtkinter.CTkLabel(self.Resultsframe,text=self.dashLines)
        self.lblresultBG.place(x=150,y=10)

        self.lblresultSL = customtkinter.CTkLabel(self.Resultsframe,text=self.dashLines)
        self.lblresultSL.place(x=150,y=60)

        self.lblresultAMT = customtkinter.CTkLabel(self.Resultsframe,text=self.dashLines + 'ml' )
        self.lblresultAMT.place(x=150,y=110)


        # textboxes
        self.txtsearch = customtkinter.CTkEntry(self.Searchframe,textvariable=self.searchBG,width=160,font=self.font3, bg_color=self.color)
        self.txtsearch.place(x = 160,y=12)
        

        # self.txtBG = customtkinter.CTkEntry(self.Resultsframe, width=160,font=self.font3, bg_color=self.color
        #                                         )
        # self.txtBG.place(x = 120,y=12)
        

        # checkbox
        self.chkAssign = customtkinter.CTkCheckBox(self.Resultsframe,text='Assign',variable=self.checkAssign)
        self.chkAssign.place(x=400,y=100)


        # Buttons
        self.searchbtn = customtkinter.CTkButton(self.Searchframe, text='Search',font = self.font3,command=self.bloodbankSearch,
                                                  width=90)
        self.searchbtn.place(x=325,y=12)

    # Patient Record 
    def searchPatients(self):
        # variables
        self.searchbyregnumber = StringVar()
        self.data = []

        # Frames
        self.patientSearchframe = customtkinter.CTkFrame(self,bg_color=self.color,width=1168,height=250,corner_radius=10)
        self.patientSearchframe.place(x=40,y=400)

        self.framelabel = customtkinter.CTkLabel(self,bg_color=self.color,text=' -Search- ')
        self.framelabel.place(x=50,y=400)

        self.psearchframe = customtkinter.CTkFrame(self.patientSearchframe,width=300,height=200,
                                                  corner_radius=15)
        self.psearchframe.place(x=10,y=30)

        self.precordframe = customtkinter.CTkFrame(self.patientSearchframe,width=800,height=200,
                                                  corner_radius=15)
        self.precordframe.place(x=320,y=30)

        # textboxes
        self.txtpatientsearch = customtkinter.CTkEntry(self.psearchframe,width=160,textvariable=self.searchbyregnumber)
        self.txtpatientsearch.place(x=110,y=50)


        # labels
        self.lbl = customtkinter.CTkLabel(self.psearchframe, text="Reg Number : ", font=self.font3)
        self.lbl.place(x=10, y=48)

        self.lbl = customtkinter.CTkLabel(self.psearchframe, text="Search", font=self.font1)
        self.lbl.place(x=70, y=10)

        labelnames = ['First name :', 'Last name :', 'Gender :', 'Age :',
                       'Blood Group :', 'illness :', 'Prescription :', 'Date :']
        x = 10
        y = -40

        for i in range(0,len(labelnames)):
            if i % 2 == 1:
                x = x + 300
            else:
                y += 50 
                x = 10
                
            self.label = customtkinter.CTkLabel(self.precordframe,font=self.font2, text= labelnames[i])
            self.label.place(x=x,y=y)
        

        # Left labels
        self.lblname = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lblname.place(x=110,y=10)

        self.lblgender = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lblgender.place(x=110,y=60)

        self.lblBG = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lblBG.place(x=110,y=110)

        self.lblprescription = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lblprescription.place(x=110,y=160)

        # Right Lebels
        self.lblsname = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lblsname.place(x=410,y=10)

        self.lblage = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lblage.place(x=410,y=60)

        self.lblillness = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lblillness.place(x=410,y=110)

        self.lbldate = customtkinter.CTkLabel(self.precordframe,font=self.font3, text= self.dashLines)
        self.lbldate.place(x=410,y=160)

        # Buttons
        self.pbtnSearch = customtkinter.CTkButton(self.psearchframe,width=100, text="Search",command=self.searchPatientrecord,
                                                   font=self.font2)
        self.pbtnSearch.place(x=170, y=90)

        self.pbtnedit = customtkinter.CTkButton(self.psearchframe,width=100, text="Edit",command=self.editPatientRecord,
                                                   font=self.font2)
        self.pbtnedit.place(x=170, y=125)

    # creating the daignosis record    
    def createDiagnosticsDetails(self):
        self.frame = customtkinter.CTkFrame(self,bg_color=self.color,width=570,height=300,corner_radius=10)
        self.frame.place(x=40,y=80)

        self.flamelabel = customtkinter.CTkLabel(self,bg_color=self.color,text=' -Diagnosis Details-')
        self.flamelabel.place(x=50,y=80)

        self.bloodBankId = 0

        labelnames = ['Condition :','illness :','Blood group :', 'Date Recorded :','Prescription :','Allergy :']

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
        self.allergy = StringVar()


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

        self.txtallergy = customtkinter.CTkEntry(self.frame, width=160,font=self.font3, bg_color=self.color
                                                      ,textvariable=self.allergy)
        self.txtallergy.place(x = 370,y=170)

        # Buttons

        self.clearBtn = customtkinter.CTkButton(self.frame,text="CLEAR",width=100,font=self.font2,command=self.clearText)
        self.clearBtn.place(x = 220, y=250)

        self.updateBtn = customtkinter.CTkButton(self.frame,text="UPDATE",width=100,font=self.font2,command=self.update)
        self.updateBtn.place(x = 325, y=250)

        self.saveBtn = customtkinter.CTkButton(self.frame,text="SAVE",width=100,font=self.font2,command=self.save)
        self.saveBtn.place(x = 430, y=250)

    # creating a search button
    def bloodbankSearch(self):
        bloodgroup = self.searchBG.get()
        data = self.diagnosisDB.searchBG(bloodgroup)

        if len(data)> 0:
            for record in data:
                self.lblresultBG.configure(text=record[1])
                self.lblresultSL.configure(text=record[2])
                self.lblresultAMT.configure(text=f"{record[3]} ml" )
                self.bloodBankId = record[0]
        else:
            self.lblresultBG.configure(text=self.dashLines)
            self.lblresultSL.configure(text=self.dashLines)
            self.lblresultAMT.configure(text=self.dashLines + 'ml' )
            self.bloodBankId = 0  

        # print(self.bloodBankId)

    def getData(self):
        data = []
        if self.checkAssign.get() == 1:
            data = [self.regnumber,
                    self.bloodBankId,
                    self.illness.get(),
                    self.bloodgroup.get(),
                    self.allergy.get(),
                    self.prescription.get(),
                    self.condition.get(),
                    self.daterecorded.get(),
                    ]
        else:
            data = [self.regnumber,
                    self.bloodBankId,
                    self.illness.get(),
                    self.bloodgroup.get(),
                    self.allergy.get(),
                    self.prescription.get(),
                    self.condition.get(),
                    self.daterecorded.get(),
                    ]

        return data

    # Save
    def save(self):
        data = self.getData()
        print(data)
        if self.checkAssign.get() == 1:
            self.diagnosisDB.saveDiagnosis(data)

        self.bloodBankId = 0

    # Update
    def update(self):
        data = self.getData()
        self.diagnosisDB.updateDiagnosis(data,self.medicalid)

    # Clear text
    def clearText(self):
        self.condition.set('')
        self.illness.set('')
        self.bloodgroup.set('')
        self.daterecorded.set('')
        self.prescription.set('')
        self.allergy.set('')

    # log Out
    def logout(self):
        self.destroy()
        from logIn import login
        app = login()
        app.mainloop()

    # back
    def back(self):
        self.destroy()
        from patients import patientsMenu
        app = patientsMenu()
        app.mainloop()

    # search Patient record
    def searchPatientrecord(self):

        self.regnumber = self.searchbyregnumber.get()
        self.search(self.regnumber)

    # searching and displayingg the record
    def search(self, regnumber):
        self.regnumber = regnumber
        if self.regnumber == "": self.regnumber = 0

        list1 = self.diagnosisDB.searchDiagnosis(self.regnumber)
        self.data = []
        for record in list1:
            for i in range(11):
                self.data.append(record[i])
        data = self.data
        self.medicalid = 0
        print(data)
        self.clearPatientValues()

        if len(data) > 0:
            self.lblname.configure(text=data[0])
            self.lblsname.configure(text=data[1])
            self.lblgender.configure(text=data[2])
            self.lblage.configure(text=data[3])
            self.lblillness.configure(text=data[4])
            self.lblBG.configure(text=data[5])
            self.lblprescription.configure(text=data[6])
            self.lbldate.configure(text=data[7])
            self.medicalid = data[8] 
                             
    # clear Patient record values
    def clearPatientValues(self):
        # Left Lebels
        self.lblname.configure(text=self.dashLines)
        self.lblgender.configure(text=self.dashLines)
        self.lblBG.configure(text=self.dashLines)
        self.lblprescription.configure(text=self.dashLines)

        # Right Lebels
        self.lblsname.configure(text=self.dashLines)
        self.lblage.configure(text=self.dashLines)
        self.lblillness.configure(text=self.dashLines)
        self.lbldate.configure(text=self.dashLines)

    # edit Patient medicals
    def editPatientRecord(self):
        print(self.data)
        if self.medicalid == 0 or self.medicalid == None:
            messagebox.showinfo('Blood Donor System','Info! \nThis patient has no medical record. \nEnter their diagnosis details then save them.')
        else:
            data = self.data
            self.condition.set(data[9])
            self.illness.set(data[4])
            self.bloodgroup.set(data[5])
            self.daterecorded.set(data[7])
            self.prescription.set(data[6]) 
            self.allergy.set(data[10]) 





if __name__ == '__main__':
    app = diagnosisCapture()
    app.mainloop()        



# Update that theblood was used when it is assign to a patients