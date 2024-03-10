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



class patients():
    mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    passwd="root",
    database="blooddonation" )


    def __init__(self):
        self.mycursor = self.mydb.cursor()
        pass

    def display(self):
        self.mycursor.execute("select * from patients")
        data = self.mycursor.fetchall()
        return data


