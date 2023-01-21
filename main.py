import mysql.connector as db
from project import Regx
from prettytable import PrettyTable

App = Regx()

while True:
    print("*"*65)
    print()
    print("*"*19 + "Hospital Management System "+"*"*19)
    print()
    print("*"*65)
    print("\n1- Admin Login \n2- Receptionist Login \n3- Doctor Login \n4- Patient Login \n5- View all The  Doctors Info \n6- Exit\n")
    ch = input("Enter Your Choice :")
    # Admin Login ...............
    if (ch == "1"):
        print(" "*20+"Admin Login Section")
        a_username = input("Enter Your UserName : ")
        a_password = input("Enter Your Password : ")
        admin = App.AdminLogin(a_username, a_password)
        if admin == None:
            print("*************** Invalid UserName ***********")

        else:
            if a_password != admin[1]:
                print("******** Invalid Password ************")
            else:
                print("******** SuccessFully Logged IN **********")

                # Admin Authentication section .............
                while True:
                    print("*************** Admin Section *******************")
                    print("\n1- Add Receptionist Account \n2- Add Doctor Account \n3- Add Patient Account \n4- Add Appointment \n5- Change Admin Account Info \n6- Remove Receptionist Account \n7- LogOut\n")
                    print()
                    ach = input("Enter Your Admin Choice : ")

                    # Add Receptionist Section ....... # Done Code
                    if (ach == "1"):
                        print(
                            "***************** Add Receptionist Account *************")
                        print()
                        while True:
                            rname = input("Enter Receptionist Name : ")
                            rcontact = input("Enter Receptionist Contact : ")
                            rage = int(input("Enter Receptionist Age : "))
                            remail = input("Enter receptionist Email :")
                            raddress = input('Enter Receptionist Address :')
                            rpassword = input("Enter Receptionist Password :")

                            r_account = App.R_CreateAccount(rname, rcontact, rage, remail, raddress, rpassword)
                              

                    # Add Doctor Section  ..........# Done Code
                    elif (ach == "2"):
                        print(
                            "***************** Add Doctor Section ******************")
                        print()
                        while True:
                            dname = input("Enter Doctor Name :")
                            dage = int(input("Enter Doctor Age :"))
                            demail = input("Enter Doctor Email :")
                            dqualification = input(
                                "Enter Doctor Qualification :")
                            dspecilist = input("Enter Doctor Specification :")
                            dpassword = input("Enter Doctor Password :")
                            d_account = App.D_CreateAccount(
                                dname, dage, demail, dqualification, dspecilist, dpassword)

                    # Add Patient Section ..........# Done Code
                    elif (ach == "3"):
                        print(
                            "****************** Add Patient Section ***************************************")
                        print()
                        while True:
                            pname = input("Enter Patient Name :")
                            pemail = input("Enter Patient Email :")
                            page = int(input("Enter Paitent Age :"))
                            pcontact = input("Enter Paitent Contact : ")
                            ppassword = input("Enter Patient Password :")
                            p_account = App.P_CreateAccount(
                                pname, pemail, page, pcontact, ppassword)

                    # Add Appointment Section .......# Done  Code
                    elif (ach == "4"):
                        pass
                   
                    # Change Admin Account ....... # Done Code
                    elif (ach == "5"):
                        print("*************** Change Admin Account *************")
                        print()
                        print(
                            "\n1- Change Admin UserName \n2- Change Admin Password\n")
                        print()
                        a_change = input("Enter Your Choice :")
                        if (a_change == "1"):
                            password = input("Enter Current Passsword : ")
                            x = App.checkpass(password)
                            if x == None:
                                print(
                                    "***************** Invalid password *************")
                            else:
                                new_username = input(
                                    "Enter Your New UserName :")
                                x1 = App.ChangeAdminUserName(
                                    new_username, password)
                                print(f"********** {x1}**********")
                        elif (a_change == "2"):
                            password = input("Enter Current Password :")
                            x = App.checkpass(password)
                            if x == None:
                                print(
                                    "************** Invalid Admin Password********")
                            else:
                                new_password = input("Enter New Password :")
                                x2 = App.ChangeAdminPassword(
                                    new_password, password)
                                print(f"\n*********** {x2}************\n")
                    # Remove Receptionist Account .....# Pending Code
                    elif (ach == "6"):
                        print(
                            "************* Delete Receptinist Account *************")
                        print()
                        # remail = input("Enter Receptionist Email :")
                        # check_R = App.Check_ReceptEmail(remail = remail)
                        # if check_R == True:
                        #     print("************* User Does Not Exists***********")
                        # else:
                        #     recept_remove = App.Remove_ReceptAccount(remail)
                        #     print("delete data")

                    # Admin logOut Section ......
                    elif (ach == "7"):
                        print("********* Thank You Admin Section *********")
                        break

                    else:
                        print("************ Invalid Admin Choice ********8")

    # Receptionist Login ........ # Done Login Code  
    elif (ch == "2"):
        print("\n***************** Receptionist Login Section **********************\n")
        print() 

        # here start receptionist working  # Pending
        while True:
            remail = input("Enter Your Email - ID : ")
            rpassword = input("Enter Your Password : ")
            R = App.Receptionist_Login(remail, rpassword)
            if R == None:
                print("********** InCorrect Receptionist Password *************")
            else:
                print("************** SuccessFully Receptionist Logged In **********************")
                
                while True:
                    print("**************** Receptionist Section *******************")
                    print("\n1- View Doctor \n2- View Patient \n3- Book Appointment \n4- View Appoinment \n5-Update Receptionist Info \n6- Exit\n")
                    print()
                    r_choice = input("Enter Recepionist Choice : ")

                    # view all the doctor who r present right now in the hosital  # Done Code
                    if (r_choice=="1"):
                        print("******************* View All The Present Doctor in The hospital *****************************")
                        print()
                        # a = (dname,dqualification,dspecilist)
                        view_doctor = App.Show_DoctorInfo()
                        x = PrettyTable()
                        x.field_names = ["Doctor ID","Doctor Name","Doctor Age","Doctor Email","Doctor Qualification","Doctor Specialist","Doctor Password"]
                        x.add_rows(view_doctor)
                        print(x)
                    #  view all the patient who r registered there information  # Done Code 
                    elif (r_choice=="2"):
                        print("******************* View All The Present Doctor in The hospital *****************************")
                        print()
                        # a = (dname,dqualification,dspecilist)
                        view_patient = App.Show_PatientInfo()
                        x = PrettyTable()
                        x.field_names = ["Patient ID","Patient Name","Patient Email ","Patient Age","Patient Contact","Patient Password"]
                        x.add_rows(view_patient)
                        print(x)
                    
                    # Book Appointment With Patient Information and Doctor Information
                    elif (r_choice=="3"):
                        pass
                    # View All The Appointments ......
                    elif (r_choice=="4"):
                        pass
                    # Upate Receptionist Information ...........
                    elif(r_choice =="5"):
                        pass
                    
                    elif (r_choice=="6"):
                        print("*************** Thank You Receptionist Section *************")
                        break
                    else:
                        print("*************** Invalid Syntax **************")       

    # Doctor Login............... # Done Login Code
    elif (ch == "3"):
        print("\n***************** Doctor Login Section **********************\n")
        print()
        while True:
            demail = input("Enter Your Email - ID : ")
            dpassword = input("Enter Your Password : ")
            R = App.Doctor_Login(demail, dpassword)
            if R == None:
                print("********** InCorrect Doctor Password *************")
            else:
                print( "************** SuccessFully Doctor Logged In **********************")
                print()
                
                # here start doctor perform different -2 task 
                while True:
                    print("****************** Doctor Section *******************")
                    print("\n1- View Patient  \n2- View Appoinment \n3- Update Doctor Info \n4- Exit \n")
                    d_choice = input("Enter Doctor CHoice : ")
                    if(d_choice =="1"):
                        pass
                    elif(d_choice =="2"):
                        pass
                    elif(d_choice =="3"):
                        pass
                    
                    elif(d_choice =="5"):
                        print("**************** Thank You Doctor Section *****************")
                        break
                    else:
                        print("*********** Invalid Syntax****************")

    # Patient Login.............. # Done Login Code
    elif (ch == "4"):
        print("\n***************** Doctor Login Section **********************\n")
        print()
        while True:
            pemail = input("Enter Your Email - ID : ")
            ppassword = input("Enter Your Password : ")
            P = App.Patient_Login(pemail, ppassword)
            if P == None:
                print("********** InCorrect Patient Password *************")
            else:
                print("************** SuccessFully Patient Logged In **********************")

                # here start whole the code for patient operations  # Pending
                while True:
                    print("************** Patient Section *****************")
                    print("\n1- View Doctor \n2- View Our Appointment \n3- Apply For  Appointment \n4- Update Patient Info \n5- Exit \n")
                    print()
                    p_choice = input("Enter Your Choice : ")

                    # view the all doctord # Done Code 
                    if (p_choice =="1"):
                        print("******************* View All The Present Doctor in The hospital *****************************")
                        print()
                        # a = (dname,dqualification,dspecilist)
                        view_doctor = App.Show_DoctorInfoAll()
                        x = PrettyTable()
                        x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
                        x.add_rows(view_doctor)
                        print(x)

                    elif (p_choice =="2"):
                        pass
                    elif(p_choice =="3"):
                        pass
                    elif(p_choice =="4"):
                        pass
                    elif(p_choice =="5"):
                        print("************* Thank You Paitent Section ****************")
                        break
                    else:
                        print("*********** Invalid Syntax ********************")


                   
                
    # Print all the doctors list .............. Done View code
    elif (ch == "5"):
        print("******************* View All The Present Doctor in The hospital *****************************")
        print()
        # a = (dname,dqualification,dspecilist)
        view_doctor = App.Show_DoctorInfoAll()
        x = PrettyTable()
        x.field_names = ["Doctor Name","Doctor Qualification","Doctor Specialist"]
        x.add_rows(view_doctor)
        print(x)
    elif (ch == "6"):
        print("****************** Thank You ****************")
        break
    else:
        print(" Invalid Syntax ")
