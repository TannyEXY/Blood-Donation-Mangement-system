# creating the log in interface
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mainMenu
from Backend.dbManager import donorDB,bloodBankDB


class donation(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("")
        self.geometry("1366x780")
        self.config(bg ="#161C25")
        #  self.resizable(False,False)
        self.color = "#161C25"

        self.font1 = ("Arial",20,'bold')
        self.font2 = ("Arial",12,'bold')
        self.font4= ("Arial",60,'bold')
        self.font3 = ("Arial",11,'bold')

        # data variables
        self.donorData = []
        self.bloodBankData = []
        self.diagnosisData = []

        self.donationDB_hanler = donorDB()
        self.bloodBankDB_Handler = bloodBankDB()

        # Frames
        self.frameContainer = customtkinter.CTkFrame(self,bg_color=self.color,width=1000,height=710,corner_radius=50)
        self.frameContainer.pack(pady=50)

        self.frameDiagnosis = customtkinter.CTkFrame(self.frameContainer,width=550,height=400,corner_radius=50)
        self.frameDiagnosis.place(x=430,y=20)

        self.frameDonor = customtkinter.CTkFrame(self.frameContainer,width=400,height=400,corner_radius=50)
        self.frameDonor.place(x=20,y=20)

        self.frameBloodBank = customtkinter.CTkFrame(self.frameContainer,width=550,height=220,corner_radius=50)
        self.frameBloodBank.place(x=20,y=430)

        self.frameButtons = customtkinter.CTkFrame(self.frameContainer,width=400,height=220,corner_radius=50)
        self.frameButtons.place(x=580,y=430)

        #  Frame Label
        framelabels = [[55,20,'Donor'],[465,20,'Diagnosis'],[65,430,'Blood Bank']]
        
        for label in framelabels:
            self.lbl = customtkinter.CTkLabel(self.frameContainer,text=label[2],font=self.font1)
            self.lbl.place(x=label[0],y=label[1])

        self.createDiagnosticsDetails()
        self.createDonorDetails()
        self.createBloodBankDetails()
        self.createButtons()

        self.lblsave = customtkinter.CTkLabel(self.frameDiagnosis,text= '',font=self.font3
                                                 )
        self.lblsave.place(x=20,y=300)

    def createButtons(self):
        self.btnSave = customtkinter.CTkButton(self.frameDiagnosis,text='Save\nRecord',corner_radius=15,command=self.save,
                                               font=self.font2,width=70
                                                 )
        self.btnSave.place(x=460, y=340)

        self.btnDonate = customtkinter.CTkButton(self.frameButtons,text='Donate\nBlood',corner_radius=15,command=self.donate,
                                                 font=self.font2,width=70
                                                 )
        self.btnDonate.place(x=300, y=100)

        self.btnBack = customtkinter.CTkButton(self.frameButtons,text='Back',corner_radius=15,font=self.font2,command=self.Back,
                                               width=70,height=40)
        self.btnBack.place(x=300, y=153)

        self.createDonorSearchResults()

    def createDonorDetails(self):
        # donor labels
            
        y_axis = 30
        donorlabelnames = ["First Name :", "Last Name :","Gender :", "Phone :","National ID :","Date of Birth :","Home Address :"]
        for lablename in donorlabelnames:
           self.pnameLabel = customtkinter.CTkLabel(self.frameDonor, text=lablename, font=self.font2)
           self.pnameLabel.place(x=40,y=y_axis)
           y_axis += 50

        # Varibles for the textboxes
        self.txtname = StringVar()
        self.txtlname = StringVar()
        self.txtgender = ''
        self.txtphone = StringVar()
        self.txtnationid = StringVar()
        self.txtdob = StringVar()
        self.txthome = StringVar()


        self.textboxvariables = [self.txtname,self.txtlname, self.txtgender,self.txtphone,self.txtnationid,self.txtdob,self.txthome]
        self.Namesearch = StringVar()

        self.textbox = [""] * 8

        y_axis = 30
        # Creating textboxes on the interface
        for num in range(len(donorlabelnames)):
            if num == 2:
                self.textbox[num]=customtkinter.CTkComboBox(self.frameDonor, width=200,
                                                        font=self.font2, corner_radius=5)
                self.textbox[num].place(x=135,y=y_axis)
                self.textbox[num].configure(values=["Male", "Female"])
                self.textbox[num].set("Select")
                self.textboxvariables[num]=self.textbox[num] 
                y_axis += 50
                continue
            if num == 5:
                self.textbox[num]=customtkinter.CTkEntry(self.frameDonor, width=200,textvariable=self.textboxvariables[num],
                                                        font=self.font2, corner_radius=5)
                self.textbox[num].place(x=135,y=y_axis)
                self.textboxvariables[num].set("yyyy-mm-dd")
                
                
                y_axis += 50
                continue
            
                
            self.textbox[num]=customtkinter.CTkEntry(self.frameDonor, width=200,textvariable=self.textboxvariables[num],
                                                        placeholder_text= "", font=self.font2, corner_radius=5)
            self.textbox[num].place(x=135,y=y_axis)
            y_axis += 50

        self.btnClear = customtkinter.CTkButton(self.frameDonor,text='Clear',corner_radius=15,command=self.clearDonorText,
                                                font=self.font2,width=70)
        self.btnClear.place(x=266, y=365)



        # creating the daignosis record    
    
    def createDiagnosticsDetails(self):

        self.bloodBankId = 0

        labelnames = ['illness :','Blood group :', 'Date Recorded :','Weight :','Allergy :']

        column = 0
        x = 10
        y = 100
        for label in labelnames:
            if column == 2:
                y += 80
                x = 10
            elif column == 4:
                y += 80
                x = 10
            
            self.lbl = customtkinter.CTkLabel(self.frameDiagnosis,text=label,font =self.font3)
            self.lbl.place(x=x,y=y)
            x += 260
            column += 1

       
        self.illness = StringVar()
        self.bloodgroup = StringVar()
        self.daterecorded = StringVar()
        self.weight = StringVar()
        self.allergy = StringVar()




        # Creating textboxes

        self.txtillness = customtkinter.CTkEntry(self.frameDiagnosis, width=160,font=self.font3, bg_color=self.color
                                                 ,textvariable=self.illness)
        self.txtillness.place(x = 105,y=100)

        self.txtbloodgroup = customtkinter.CTkEntry(self.frameDiagnosis, width=160,font=self.font3, bg_color=self.color
                                                    ,textvariable=self.bloodgroup)
        self.txtbloodgroup.place(x = 370,y=100)

        self.txtdaterecorded = customtkinter.CTkEntry(self.frameDiagnosis, width=160,font=self.font3, bg_color=self.color
                                                      ,textvariable=self.daterecorded)
        self.txtdaterecorded.place(x = 105,y=180)
        self.daterecorded.set('yyyy-mm-dd')
        

        self.txtweight = customtkinter.CTkEntry(self.frameDiagnosis, width=160,font=self.font3, bg_color=self.color
                                                     ,textvariable=self.weight)
        self.txtweight.place(x = 370,y=180)

        self.txtallergy = customtkinter.CTkEntry(self.frameDiagnosis, width=160,font=self.font3, bg_color=self.color
                                                      ,textvariable=self.allergy)
        self.txtallergy.place(x = 105,y=260)

        # button
        self.btnClear = customtkinter.CTkButton(self.frameDiagnosis,text='Clear',corner_radius=15,command=self.cleardiagnosisText,
                                                font=self.font2,width=70)
        self.btnClear.place(x=460, y=300)

    def createBloodBankDetails(self):
        # textboxes variables
        self.BG = StringVar()
        self.BL = StringVar()
        self.BDate = StringVar()
        self.BAMT = StringVar()

        self.txtBBvariables=[ self.BG ,
                            self.BL,
                            self.BDate,
                            self.BAMT]

        self.Data = []

        # Blood Bank labels
        lblnames = ['Blood Group :','Location :','Date :', 'Amount :']
        y_axis = 35

        for labelname in lblnames:
            self.lbl = customtkinter.CTkLabel(self.frameBloodBank, text= labelname)
            self.lbl.place(x=60,y=y_axis)
            y_axis += 50

        
        # Blood Bank textboxes
        self.txtbox = [''] * 4
        
        y_axis = 35
        for i in range(4):
            self.txtbox[i] = customtkinter.CTkEntry(self.frameBloodBank, width=200,corner_radius=10,
                                                    textvariable=self.txtBBvariables[i])
            self.txtbox[i].place(x=200,y=y_axis)
            y_axis += 50
        self.BDate.set('yyyy-mm-dd')

        # button
        self.btnClear = customtkinter.CTkButton(self.frameBloodBank,text='Clear',corner_radius=15,font=self.font2,width=70,
                                                command=self.clearBloodbanktext)
        self.btnClear.place(x=410, y=184)          

    def createDonorSearchResults(self):

        self.txtDonorSearch = StringVar()

        self.lblData = [''] * 4

        # Labels
        self.lbl = customtkinter.CTkLabel(self.frameButtons,text='Enter reg number :',font=self.font2)
        self.lbl.place(x=20,y=20)

        self.lbl = customtkinter.CTkLabel(self.frameButtons,text='Full name :',font=self.font2)
        self.lbl.place(x=20,y=80)

        self.lbl = customtkinter.CTkLabel(self.frameButtons,text='Gender :',font=self.font2)
        self.lbl.place(x=20,y=110)

        self.lbl = customtkinter.CTkLabel(self.frameButtons,text='Last Donated :',font=self.font2)
        self.lbl.place(x=20,y=140)

        self.lbl = customtkinter.CTkLabel(self.frameButtons,text='Phone :',font=self.font2)
        self.lbl.place(x=20,y=170)

        self.txtDonorname = customtkinter.CTkEntry(self.frameButtons,width=140,textvariable=self.txtDonorSearch)
        self.txtDonorname.place(x=140,y=20)

        self.btnDonorsearch = customtkinter.CTkButton(self.frameButtons,text='Search',command=self.searchDonor
                                                      ,width=60,corner_radius=15)
        self.btnDonorsearch.place(x=205,y=50)

        y = 80

        for i in range(len(self.lblData)):
            self.lblData[i] =  customtkinter.CTkLabel(self.frameButtons,text='- - - - - - - - - - - - -',font=self.font2)
            self.lblData[i].place(x=110,y=y)
            y += 30

   
   
   
    def getDonorData(self):
        # "First Name :", "Last Name :","Gender :", "Phone :","National ID :","Date of Birth :","Home Address :"
        
        for textbox in self.textboxvariables:
                self.donorData.append(textbox.get())

    def getBloodBankData(self):
        # 'Blood Group :','Location :','Date :', 'Amount :'
        self.bloodBankData = []
        for value in self.txtBBvariables:
            self.bloodBankData.append(value.get())

    def getDiagnosisData(self):
        # 'illness :','Blood group :', 'Date Recorded :','weight :','Allergy :'
        
        data = [
                self.illness,
                self.bloodgroup,
                self.daterecorded,
                self.weight,
                self.allergy
                ]
        
        for value in data:
            self.diagnosisData.append(value.get())
            
    def setData(self,data):
        
        for i in range(len(data)):
            self.lblData[i].configure(text = data[i])

    def searchDonor(self):
        regnumber =  self.txtDonorSearch.get()
        data = self.donationDB_hanler.getDonor(regnumber)
        print(data)
        if len(data) > 0:
            self.setData(data)
        else:
            self.clearSearchtext()


    def donate(self):
        regnumber =  self.txtDonorSearch.get()
        self.getBloodBankData()
        data = []
        if regnumber.isnumeric() and int(regnumber) > 0:
            data = self.bloodBankData
            self.bloodBankDB_Handler.SaveBloodBanknDonor(data,regnumber)
            messagebox.showinfo("Blood Donation System",'The donor has successfully Donated blood')
            print(data)
        
        # self.bloodBankDB_Handler.SaveBloodBank(data,regnumber) 

    def clearSearchtext(self):
        for i in range(len(self.lblData)):
            self.lblData[i].configure(text = '- - - - - - - - - - - - -')

    def cleardiagnosisText(self):
        data = [
                self.illness,
                self.bloodgroup,
                self.daterecorded,
                self.weight,
                self.allergy
                ]
        num = 0
        for value in data:
            if num == 2:
                data[num].set('yyyy-mm-dd')
            else:
                value.set('')
            num += 1
        self.lblsave.columnconfigure(text='')
    
    def clearBloodbanktext(self):
        num = 0
        for value in self.txtBBvariables:
            if num == 2:
                value.set('yyyy-mm-dd')
            else:
                value.set('')
            num += 1

    def clearDonorText(self):
        num = 0
        for textbox in self.textboxvariables:
            if num == 2:
                self.textbox[num].set('Select')
            elif num == 5:
                textbox.set('yyyy-mm-dd')
            else:
                textbox.set('')

            num += 1
        self.lblsave.configure(text= "hhhhhhhhhhh", text_color='green')
    
    def save(self):
        # 
        self.getDonorData()
        self.getDiagnosisData()

        Donordata = self.donorData
        diagnosisData = self.diagnosisData
        try:
            regnumber =self.donationDB_hanler.saveDonor(Donordata,diagnosisData)

            self.donorData = []
            self.diagnosisData =[]

            self.lblsave.configure(text= f"Record saved. \nDonor's Reg number is {regnumber}", text_color='green')
        except Exception as erro:
            self.lblsave.configure(text= f"{erro}", text_color='green')

    def Back(self):
        self.destroy()
        from mainMenu import main_Menu
        app = main_Menu()
        app.mainloop()

if __name__ == "__main__":
    app = donation()
    app.mainloop()

