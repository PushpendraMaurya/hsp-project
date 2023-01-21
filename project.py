import mysql.connector as db


class Admin:

    def __init__(self):

        # create database name is server...........
        mydb = db.connect(host='localhost', port='3306',
                          user='root', passwd='root')
        query = '''create database if not exists server;'''
        cur = mydb.cursor()
        cur.execute(query)
        mydb.close()

        # Admin Default Data
        self.a_id = 1
        self.a_username = 'admin'
        self.a_password = 'admin'
        self.AdminValue(self.a_id, self.a_username, self.a_password)

        # create table name is admin ..........
        self.connection()
        query = '''create table if not exists admin_pushpendra(
            a_id int primary key unique,
            a_username varchar(50) ,
            a_password varchar(50));'''

        self.cur.execute(query)
        self.mydb.close()

        # create table name is Receptionist ....
        self.connection()

    def AdminValue(self, a_id, a_username, a_password):
        self.connection()
        try:
            data = (a_id, a_username, a_password)
            query = '''insert into admin_pushpendra(a_id,a_username,a_password) values (%s,%s,%s);'''
            self.cur.execute(query, data)
            self.cur.execute("commit;")
            self.mydb.close()
        except:
            pass

    # This is is used to connect Python to Mysql in BasicDB as database name

    def connection(self):
        self.mydb = db.connect(host='localhost', user='root',
                               port='3306', passwd='root', database='server')
        self.cur = self.mydb.cursor()

    def AdminLogin(self, username, password):
        self.connection()
        data = (username,)
        query = '''select a_username,a_password from admin_pushpendra where a_username =%s;'''
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def ChangeAdminUserName(self,new_username,password):
        self.connection()
        data = (new_username,password)
        query = '''update admin_pushpendra set a_username = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin Password Change !"
    
    def ChangeAdminPassword(self,new_password,password):
        self.connection()
        data = (new_password,password)
        query = '''update admin_pushpendra set a_password = %s where a_password = %s;'''
        self.cur.execute(query,data)
        self.cur.execute("commit;")
        self.mydb.close()
        return "SuccessFully Admin Password Change !"

    def checkpass(self,password):
        self.connection()
        data = (password,)
        query = '''select a_username,a_password from admin_pushpendra where a_password = %s; '''
        self.cur.execute(query,data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    # show the doctor info on without register info user 
    def Show_DoctorInfoAll(self):
        self.connection()
        query ='''select dname,dqualification,dspecilist from Doctor;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record
    # def Check_ReceptEmail(self,remail= None):
    #     self.connection()
    #     data =(remail,)
    #     query = '''select contact from Receptionist where remail = %s;'''
    #     self.cur.execute(query,data)
    #     record = self.cur.fetchone()
    #     self.mydb.close()

    # def Remove_ReceptAccount(self,remail):
    #     self.connection()
    #     data = (remail,)
    #     query = '''delete from Receptionist where remail = %s;'''
    #     self.cur.execute(query,data)
    #     self.cur.execute("commit;")
    #     self.mydb.close()



class Receptionist(Admin):
    def __init__(self):
        super().__init__()
        # create table name is receptionist
        self.connection()
        query = '''create table if not exists receptionist(
            rid int primary key auto_increment,
            rname varchar(50) not null,
            rcontact varchar(20) not null unique,
            rage int(3) not null,
            remail varchar(50) not null unique,
            raddress text,
            rpassword varchar(50));'''

        self.cur.execute(query)
        self.mydb.close()

    def R_CreateAccount(self, rname, rcontact, rage, remail, raddress, rpassword):
        self.connection()
        query = '''insert into receptionist(rname,rcontact,rage,remail,raddress,rpassword)
            values(%s,%s,%s,%s,%s,%s);'''
        data = (rname, rcontact, rage, remail, raddress, rpassword)
        self.cur.execute(query, data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True
        # print("account created")

    def Receptionist_Login(self, remail, rpassword):
        self.connection()
        query = '''select remail from Receptionist where remail = %s && rpassword =%s;'''
        data = (remail, rpassword)
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    def Show_DoctorInfo(self):
        self.connection()
        query ='''select * from Doctor;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record
      
    def Show_PatientInfo(self):
        self.connection()
        # data =(dname,dqualification,dspecilist)
        query ='''select * from patient;'''
        self.cur.execute(query,)
        record = self.cur.fetchall()
        return record


class Doctor(Receptionist):
    def __init__(self):
        super().__init__()

        # create doctor table name is Doctor.......
        self.connection()
        query = '''create table if not exists Doctor(
            did int primary key auto_increment ,
            dname varchar(50) not null,
            dage int(3) not null ,
            demail varchar(50) not null unique,
            dqualification varchar(100) not null,
            dspecilist varchar(50) not null,
            dpassword varchar(100) not null);'''

        self.cur.execute(query)
        # self.cur.execute("commit;")
        self.mydb.close()
        # return True
        # print("doctor table created ")

    def D_CreateAccount(self, dname, dage, demail, dqualification, dspecilist, dpassword):
        self.connection()
        query = '''insert into Doctor(dname,dage,demail,dqualification,dspecilist,dpassword)  values(%s,%s,%s,%s,%s,%s);'''
        data = (dname, dage, demail, dqualification, dspecilist, dpassword)
        self.cur.execute(query, data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True
        # print("data inserted succesfully")

    def Doctor_Login(self, demail, dpassword):
        self.connection()
        query = '''select demail from Doctor where demail = %s && dpassword = %s;'''
        data = (demail, dpassword)
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record

    
        


class Patient(Doctor):
    def __init__(self):
        super().__init__()

        # create table patient name is Patient..........
        self.connection()
        query = ''' create table if not exists Patient(
                pid int primary key auto_increment ,
                pname varchar(50) not null ,
                pemail varchar(100) not null,
                page int(3) not null,
                pcontact bigint not null,
                ppassword varchar(50) not null);'''

        self.cur.execute(query)
        self.mydb.close()

    def P_CreateAccount(self, pname, pemail, page, pcontact, ppassword):
        self.connection()
        query = '''insert into Patient(pname,pemail,page,pcontact,ppassword) values(%s,%s,%s,%s,%s);'''
        data = (pname, pemail, page, pcontact, ppassword)
        self.cur.execute(query, data)
        self.cur.execute("commit;")
        self.mydb.close()
        return True

    def Patient_Login(self, pemail, ppassword):
        self.connection()
        query = '''select pemail from Patient where pemail = %s && ppassword = %s;'''
        data = (pemail, ppassword)
        self.cur.execute(query, data)
        record = self.cur.fetchone()
        self.mydb.close()
        return record


class Appintment(Patient):
    pass


class Regx(Appintment):
    pass


App = Regx()
