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
                                update table patients set name ='{datalist[0]}', lname = '{datalist[1]}',
                                gender = '{datalist[2]}',phone = '{datalist[3]}',nationalid = '{datalist[4]}'
                                ,dob ='{datalist[5]}', homeaddress = '{datalist[6]}' 
                                where regnumber = {regnumber};
                              ''')
        self.mydb.commit()



