from typing import Tuple
import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from Backend.dbManager import bloodBankDB


class bloodbank(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1266x720")
        self.config(bg ="#161C25")
        self.resizable(False,False)
        self.font1 = ("Arial",20,'bold')
        self.font2 = ("Arial",12,'bold')
        self.font4= ("Arial",60,'bold')
        self.color = "#161C25"

        # Database Handler
        self.bloodbankDB_handler = bloodBankDB()

        # Results Container
        self.AV_BloodBanks_Data = []

        self.pointer = 1


        # Frames 
        self.frameBKAdder = customtkinter.CTkFrame(self,width=430,height=270,bg_color=self.color, corner_radius=20)
        self.frameBKAdder.place(x=20, y=80)

        self.frameUSEDBK = customtkinter.CTkFrame(self,width=730,height=270,bg_color=self.color, corner_radius=20)
        self.frameUSEDBK.place(x=460, y=80)

        self.frameAVBK = customtkinter.CTkFrame(self,width=880,height=270,bg_color=self.color, corner_radius=20)
        self.frameAVBK.place(x=20, y=360)

        self.frameNavigator = customtkinter.CTkFrame(self,width=285,height=270,bg_color=self.color, corner_radius=20)
        self.frameNavigator.place(x=910, y=360)

        # Menu Label
        self.lblmeasage = customtkinter.CTkLabel(self,text='Blood Bank',bg_color=self.color, text_color='#161C65',font=self.font4,
                                                 corner_radius=100)
        self.lblmeasage.place(x=400,y=5) 

        # Message
        self.lblmeasage = customtkinter.CTkLabel(self.frameUSEDBK,text='No Service yet!',font=self.font4,
                                                 corner_radius=100)
        self.lblmeasage.place(x=30,y=80) 

        #  Contained Frames
            # Available blood banks
        self.createAV_BloodBank()
        
            

        #  frame label
        locations = [[30,80,'Blood bank'],[480,80,'Used blood banks'],[30,360,'Available Blood Banks']]

        for pnt in locations:
            self.framelbl = customtkinter.CTkLabel(self,text=pnt[2], bg_color=self.color,font=self.font1)
            self.framelbl.place(x=pnt[0],y=pnt[1])

        


        # textboxes variables
        self.BG = StringVar()
        self.BL = StringVar()
        self.BDate = StringVar()
        self.BAMT = StringVar()

        self.txtvariables=[ self.BG ,
                            self.BL,
                            self.BDate,
                            self.BAMT]

        self.Data = []

        # Blood Bank labels
        lblnames = ['Blood Group :','Location :','Date :', 'Amount :']
        y_axis = 50

        for labelname in lblnames:
            self.lbl = customtkinter.CTkLabel(self.frameBKAdder, text= labelname)
            self.lbl.place(x=20,y=y_axis)
            y_axis += 50

        
        # Blood Bank textboxes
        self.txtbox = [''] * 4
        
        y_axis = 50
        for i in range(4):
            self.txtbox[i] = customtkinter.CTkEntry(self.frameBKAdder, width=200,corner_radius=10,textvariable=self.txtvariables[i])
            self.txtbox[i].place(x=130,y=y_axis)
            y_axis += 50


        # Blood Bank Button
        
        self.btnSave = customtkinter.CTkButton(self.frameBKAdder,text='Save',corner_radius=15,font=self.font2,width=70,
                                               command=self.Save)
        self.btnSave.place(x=340, y=150)

        self.btnClear = customtkinter.CTkButton(self.frameBKAdder,text='Clear',corner_radius=15,font=self.font2,width=70,
                                                command=self.ClearText)
        self.btnClear.place(x=340, y=200)


        # Navigation Button
        self.btnlogout = customtkinter.CTkButton(self.frameNavigator,text='Log out',corner_radius=25,command=self.logout,
                                                 font=self.font2,width=150,height=70)
        self.btnlogout.place(x=60, y=50)

        self.btnBack = customtkinter.CTkButton(self.frameNavigator,text='Back',corner_radius=25,font=self.font2,command=self.back,
                                               width=150,height=70)
        self.btnBack.place(x=60, y=150)
        
        
        # message label
        self.lblmeasage = customtkinter.CTkLabel(self.frameBKAdder,text='', text_color='green',font=self.font2)
        self.lblmeasage.place(x=330,y=237) 

        # Clearing text
        self.ClearText()



#  Contained Frame creater
        # Available blood banks
    def createAV_BloodBank(self):
        # variables
        self.BG_value = StringVar()

        # Frames
        self.frameAVBKSearch = customtkinter.CTkFrame(self.frameAVBK,width=300,height=200, corner_radius=20)
        self.frameAVBKSearch.place(x=20, y=40)

        self.frameAVBKResults = customtkinter.CTkFrame(self.frameAVBK,width=500,height=200, corner_radius=20)
        self.frameAVBKResults.place(x=330, y=40)

        # Frame label
        self.lblmeasage = customtkinter.CTkLabel(self.frameAVBK,text='Search',font=self.font2)
        self.lblmeasage.place(x=30,y=40)

        self.lblmeasage = customtkinter.CTkLabel(self.frameAVBK,text='Results',font=self.font2)
        self.lblmeasage.place(x=350,y=40)

        # Label
        self.lblBloodGroup = customtkinter.CTkLabel(self.frameAVBKSearch, text='Blood Group :',font=self.font2)
        self.lblBloodGroup.place(x=30,y=60)

        self.lbl = customtkinter.CTkLabel(self.frameAVBKSearch, text='Records :',font=self.font2)
        self.lbl.place(x=130,y=140)

        self.lblresults = customtkinter.CTkLabel(self.frameAVBKSearch, text='0',font=self.font2)
        self.lblresults.place(x=200,y=140)

        # Searched Results
            # labels
        labelnames = [[30,50, 'Blood Group :'], [240,50,'Location :'],
                     [30,100,'Date :'], [240,100,'Amount :'],
                     [30,150,"Donor's Full Name :"]]
        
        for label in labelnames:
            self.lblBloodGroup = customtkinter.CTkLabel(self.frameAVBKResults, text=label[2],font=self.font2)
            self.lblBloodGroup.place(x=label[0],y=label[1])

        self.lblBGResult = customtkinter.CTkLabel(self.frameAVBKResults,text= '- - - - - - - - - - -',font=self.font2)
        self.lblBGResult.place(x=140,y=50)
        
        self.lblDate = customtkinter.CTkLabel(self.frameAVBKResults,text= '- - - - - - - - - - -',font=self.font2)
        self.lblDate.place(x=140,y=100)
        
        self.lblDonorname = customtkinter.CTkLabel(self.frameAVBKResults,text= '- - - - - - - - - - -',font=self.font2)
        self.lblDonorname.place(x=145,y=150)
        
        self.lbllocationResult = customtkinter.CTkLabel(self.frameAVBKResults,text= '- - - - - - - - - - -',font=self.font2)
        self.lbllocationResult.place(x=320,y=50)
        
        self.lblamount = customtkinter.CTkLabel(self.frameAVBKResults,text= '- - - - - - - - - - -',font=self.font2)
        self.lblamount.place(x=320,y=100)
       

            # buttons
        self.prev = customtkinter.CTkButton(self.frameAVBKResults,text= 'Prev',font=self.font2,width=60,
                                            command=self.Prev,corner_radius=20)
        self.prev.place(x=300,y=150)

        self.next = customtkinter.CTkButton(self.frameAVBKResults,text= 'Next',font=self.font2,width=60,
                                            command=self.Next,corner_radius=20)
        self.next.place(x=364,y=150)


        self.lbl_Value_Setter= [self.lblBGResult,
                                self.lblDate,
                                self.lblDonorname,
                                self.lbllocationResult,
                                self.lblamount]
        
        
        # textbox
        self.txtBGSearch = customtkinter.CTkEntry(self.frameAVBKSearch, textvariable=self.BG_value)
        self.txtBGSearch.place(x=120,y=60)

        # Button
        self.btnSearch = customtkinter.CTkButton(self.frameAVBKSearch, text='Search',width=80,
                                                 command=self.searchAVBloodGroup,corner_radius=20)
        self.btnSearch.place(x=180,y=100)






    # Load Data
    def LoadData(self,record):
        i = 0
        for label in self.lbl_Value_Setter:
            text = record[i]
            if i == 4:
                text = f'{text} ml'
            label.configure(text=text)
           
            i+=1
    
    # clear Labels
    def ClearLabels(self):
        text = '- - - - - - - - - - -'
        for label in self.lbl_Value_Setter:
            label.configure(text=text)


    # next
    def Next(self):
        p = self.pointer
        data = self.AV_BloodBanks_Data
        
        if len(data) == 0:
            messagebox.showinfo('Blood Donation System',
                       'Info! \nNo record ere found.')
            return

        if p < len(data):
            self.ClearLabels()
            self.pointer += 1
            self.LoadData(data[p])
        else:
            messagebox.showinfo('Blood Donation System',
                       "Info! \nYou have reached the last result.")

    # Prev
    def Prev(self):
        data = self.AV_BloodBanks_Data
        if len(data) == 0:
            messagebox.showinfo('Blood Donation System',
                       'Info! \nNo record ere found.')
            return

        if self.pointer > 1:
            self.ClearLabels()
            self.pointer -= 1
            p = self.pointer
            self.LoadData(data[p-1])
        else:
            messagebox.showinfo('Blood Donation System',
                       "Info! \nThis is the first result.")


    # Search
    def searchAVBloodGroup(self):

        bloodgroup = self.BG_value.get()
        
        self.pointer = 1

        self.AV_BloodBanks_Data = self.bloodbankDB_handler.search(bloodgroup)
        
        data = self.AV_BloodBanks_Data


        self.lblresults.configure(text=f'{len(data)}')

        if len(data) == 0:
            self.ClearLabels()
            return

        # loading data at position {p?}
        p = self.pointer

        self.LoadData(data[p - 1])

    # Get data
    def getData(self):
        for textbox in self.txtvariables:
            self.Data.append(textbox.get())

    # Save
    def Save(self):
        self.getData()
        data = self.Data
        try:    
            self.bloodbankDB_handler.SaveBloodBank(data)
            self.displayMessage('Record Saved.','green')
        except Exception as erro:
            self.displayMessage(f'{erro}!!','red')
            self.lblmeasage.place(x=30,y=237) 
        finally:
            self.Data = []
        
    # Clear
    def ClearText(self):
        i = 0
        for textbox in self.txtvariables:
            textbox.set('')
            if i == 2:
                textbox.set('yyyy-mm-dd')
            i += 1

        self.displayMessage("",'green')

    
    # results message
    def displayMessage(self,message, color):
        self.lblmeasage.configure(text=message,text_color=color)
        self.lblmeasage.place(x=330,y=237) 
  

    # log Out
    def logout(self):
        self.destroy()
        from logIn import login
        app = login()
        app.mainloop()

    # back
    def back(self):
        self.destroy()
        from mainMenu import main_Menu
        app = main_Menu()
        app.mainloop()


        






if __name__ == "__main__":
    app = bloodbank()
    app.mainloop()