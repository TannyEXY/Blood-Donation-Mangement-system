import mysql.connector

class loginDB():
    mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="root",
    database="blooddonation" )

    def __init__(self):
        self.mycursor =  self.mydb.cursor()

    def getLogInDeatails(self,username,password):
        self.mycursor.execute(f"select user, pass From users where user = '{username}' and pass = '{password}'")
        self.data = self.mycursor.fetchall()
        return self.data
    
    def saveDeatails(self,username,password):
        self.mycursor.execute(f"insert into users(user, pass) value('{username}','{password}');")
        self.mydb.commit()

class patientsDB():
    mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="root",
    database="blooddonation" )


    def __init__(self):
        self.mycursor = self.mydb.cursor()



    def display(self):
        self.mycursor.execute("select regnumber, name,lname,gender,phone,nationalid,dob,homeaddress from patients")
        data = self.mycursor.fetchall()
        return data
    

    def searchPatient(self, fname='', lname=''):
        # "Reg number","First Name", "Last Name","Gender", "Phone","National ID","Date of Birth","Home Address"

        self.mycursor.execute(f"select regnumber, name,lname,gender,phone,nationalid,dob,homeaddress from patients where name like '{fname}%' and lname like '{lname}%'")
        data = self.mycursor.fetchall()
        return data
    

    def savePatient(self,datalist):
        self.mycursor.execute(f'''
                                insert into patients(name,lname,gender,phone,nationalid,dob,homeaddress)
                                values('{datalist[0]}','{datalist[1]}', '{datalist[2]}','{datalist[3]}',
                                '{datalist[4]}','{datalist[5]}','{datalist[6]}');
                              ''')
        self.mydb.commit()



    def deletePatient(self, regnumber):
        self.mycursor.execute(f"Delete from patients where regnumber = {regnumber};")
        self.mydb.commit()


    def updatePatient(self,datalist,regnumber):
        self.mycursor.execute(f'''
                                update patients set name ='{datalist[0]}', lname = '{datalist[1]}',
                                gender = '{datalist[2]}',phone = '{datalist[3]}',nationalid = '{datalist[4]}'
                                ,dob ='{datalist[5]}', homeaddress = '{datalist[6]}' 
                                where regnumber = {regnumber};
                              ''')
        self.mydb.commit()

class diagnosisDB():
    mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="root",
    database="blooddonation" )
   
    def __init__(self):
        self.mycursor = self.mydb.cursor()

    def searchDiagnosis(self,regnumber):
        self.mycursor.execute(f'''
                    select p.name, p.lname, p.gender,year(current_date()) - year(p.dob) as age,
                        mp.illness, mp.bloodgroup,mp.prescriptions,Daterecorded as `date`, mp.medicalid,
                        `condition`,allergy
                    from patients as p left join medicals_patient as mp on mp.patientid = p.regnumber
                    where p.regnumber = {str(regnumber)};
                ''')
        data = self.mycursor.fetchall()
        return data
    
    def saveDiagnosis(self,data):
        query = (f'''insert into medicals_patient(patientid,bloodbankid,illness,bloodgroup,allergy,prescriptions,`condition`,DateRecorded)
                                values({data[0]},'{data[1]}','{data[2]}','{data[3]}','{data[4]}','{data[5]}','{data[6]}','{data[7]}');
                ''')
        self.mycursor.execute(query)
        self.mydb.commit()
        if data[1] != 0:
            query = f'update bloodbank set usedstate = True where bloodbankid = {data[1]};'
            self.mycursor.execute(query)
            self.mydb.commit()

        



    def updateDiagnosis(self,data,medicalid):
        self.mycursor.execute(f'''
                                update medicals_patient set patientid = {data[0]} ,bloodbankid = '{data[1]}',illness = '{data[2]}',
                                bloodgroup = '{data[3]}',allergy= '{data[4]}',prescriptions = '{data[5]}',`condition` = '{data[6]}',
                                DateRecorded = '{data[7]}' where medicalid = '{medicalid}';
                            ''')
        self.mydb.commit()

    
    def searchBG(self, bloodgroup):
        self.mycursor.execute(f'''
                                select bloodbankid, bloodgroup, storage_location, amount from bloodbank
                                where bloodgroup = '{bloodgroup}' and usedstate = 0;
                            ''')
        data = self.mycursor.fetchall()
        return data

class nextkinDB():
    mydb = mysql.connector.connect(
                host = "localhost",
                user="root",
                passwd="root",
                database="blooddonation" )
    
    def __init__(self):
        self.mycursor = self.mydb.cursor()


    def saveKin(self,data):
        self.mycursor.execute("select max(regnumber)  from patients;")
        records = self.mycursor.fetchall()
        regnumber = 0
        for set in records:
            regnumber = set[0]
                
        self.mycursor.execute(f'''
                                insert into nextofkin(patientid,name,lname,homeaddress,phone)
                                values({regnumber},'{data[0]}','{data[1]}','{data[2]}','{data[3]}');
                             ''')
        self.mydb.commit()

class bloodBankDB():
    mydb = mysql.connector.connect(
                host = "localhost",
                user="root",
                passwd="root",
                database="blooddonation" )
    
    def __init__(self):
        self.mycursor = self.mydb.cursor()

    def SaveBloodBank(self,data):
        self.mycursor.execute(f'''
                                insert into bloodbank(bloodgroup,storage_location,daterecieved,amount,usedstate)
                                values('{data[0]}','{data[1]}','{data[2]}','{data[3]}', 0)
                            ''')
        self.mydb.commit()

    
    def search(self,bloodgroup):
        self.mycursor.execute(f'''
                                select b.bloodgroup, b.daterecieved, concat(d.name ,' ', d.lname), b.storage_location, b.amount 
                                from bloodbank as b left join donor as d on d.regnumber = b.donorid
                                where b.bloodgroup like '{bloodgroup}%';
                            ''')
        setsList = self.mycursor.fetchall()
        data = []
        for set in setsList:
            data.append([set[0],set[1],set[2],set[3],set[4]])

        return data
        

