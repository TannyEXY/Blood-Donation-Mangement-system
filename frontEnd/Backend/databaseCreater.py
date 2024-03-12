import mysql.connector

mydb = mysql.connector.connect(
 host = "localhost",
 user="root",
 passwd="root"
#  database="blooddonation"   
)

mycursor =  mydb.cursor()


def createTables():
    global mycursor
    tables = {"patients": """
                create table patients(
                    regnumber int auto_increment not null unique primary key,
                    name varchar(255) not null,
                    lname varchar(255),
                    gender varchar(7),
                    dob date not null,
                    homeaddress varchar(255),
                    nationalid varchar(255),
                    phone varchar(255)
                    );
                """,
                "donor": """
                create table donor(
                    regnumber int auto_increment not null unique primary key,
                    name varchar(255) not null,
                    lname varchar(255),
                    dob date not null,
                    homeaddress varchar(255),
                    nationalid varchar(255),
                    phone varchar(255)
                    );
                """,
                "nextofkin":"""
                create table nextofkin(
                        kinid int not null unique auto_increment,
                        patientid int not null,
                        name varchar(255),
                        lname varchar(255),
                        homeaddress varchar(255),
                        phone varchar(255),
                        primary key (kinid)
                        );
                """,
                "bloodbank":"""
                    create table bloodbank(
                        bloodbankid int unique auto_increment primary key,
                        donorid int,
                        bloodgroup varchar(4) not null,
                        storage_location varchar(255) not null,
                        daterecieved date,
                        amount float,
                        usedstate boolean
                        );
                """,
                "medicals_patient":"""
                    create table medicals_patient(
                        medicalid int not null auto_increment primary key,
                        patientid int,
                        illness varchar(255),
                        bloodgroup varchar(255),
                        allergy varchar(255),
                        prescriptions varchar(255),
                        bloodbankid int,
                        `condition` varchar(255),
                        DateRecorded varchar(255)
                        );
                """,
                "medical_donor":"""
                    create table medical_donor(
                        medid int unique not null primary key,
                        donorid int not null,
                        weight int not null,
                        illness varchar(255),
                        allergy varchar(255),
                        daterecorded date,
                        bloodgroup varchar(255)
                        );
                """,
                "users": """
                    create table users(
                        userid int auto_increment primary key,
                        user varchar(255),
                        pass varchar(255)
                        );"""
                        
            }
    
    mycursor.execute("show tables")
    table = [""]
    for value in mycursor:
        table.append(value[0])
    
    for tablename, tablequery in tables.items():
         if not tablename in table:
             if tablename != 'users':
                mycursor.execute(tablequery)
             elif tablename == 'users':
                mycursor.execute(tablequery)
                
                mycursor.execute("""insert into users(user,pass) values('admin','admin');""")
                mydb.commit()
              


def initialiseDatabase():
    global mycursor
    try:
        mycursor.execute("Show Databases")
        databases = []
        for database in mycursor:
            databases.append(database[0])
        
        if not "blooddonation" in databases:
            mycursor.execute('create database blooddonation;')

        mydb.database = "blooddonation"
        mycursor =  mydb.cursor()

        createTables()
        print("connection successful")

    except Exception as message:
        print(message)
    