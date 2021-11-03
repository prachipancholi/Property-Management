import time
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector as mc
conn=mc.connect(host='localhost',port='3306',user='root',passwd='',database='broker')
mycursor=conn.cursor()
user_id=0
print("                                       ____")
print("                                     ________")
print("                                    __________")
print("                                   ____________")
print("                                  ______________")
print("                                 ________________")
print("                                ___________________")
print("                                 ||            ||")
print("                                 ||  ________  ||")
print("                                 ||  |      |  ||")
print("                                 ||  |      |  ||")
print("                                 ||  |      |  ||")
print("                                 ________________")
print("                                   LUXURY HOMES")
print()
print("      WELCOME TO A PLACE WHERE YOUR DREAM HOUSE IS OUR MATTER OF CONCERN")
print("        AND WHERE WE WILL HELP YOU SEARCH A CONVINIENT AND HARMONIOUS")
print("                      PLACE TO LIVE LIFE IN FULL BLOOM")
    
#==============================validation functions=========================================
def isnumber():
    flag=True
    s=input(">>> Enter your choice : ")
    s=s.strip()
    if len(s)==0:
        print("It Can't Be Empty")
        return "nonum"
    for i in range(len(s)):
        if s[i].isdigit()!=True:
            flag=False
    if flag:
        return(int(s))
    else:
        print("\t\t\tPlease Enter a Valid Integer Choice Value !!!")
        return "nonum"

def aadhaar():
    flag=True
    s=input(">>> Enter Aadhaar Number : ")
    s=s.strip()
    if len(s)==0:
        print("It Can't Be Empty")
        return "nonum"
    for i in range(len(s)):
        if s[i].isdigit()!=True:
            flag=False
    if flag:
        if len(s)==12:
            return(int(s))
        else:
            print("\t\t\tPlease Enter Correct Digit Aadhaar Number !!!")
            return "nonum"

    else:
        print("\t\t\tPlease Enter a Valid Integer Choice Value !!!")
        return "nonum"
    
def phone():
    flag=True
    s=input(">>> Enter Phone Number : ")
    s=s.strip()
    if len(s)==0:
        print("It Can't Be Empty")
        return "nonum"
    for i in range(len(s)):
        if s[i].isdigit()!=True:
            flag=False
    if flag:
        if len(s)==10 or (len(s)==11 and s[0]=='0'):
            return(int(s))
        else:
            print("\t\t\tPlease Enter Correct Digit Phone Number !!!")
            return "nonum"

    else:
        print("Please Enter a Valid Integer Choice Value !!!")
        return "nonum"
#===============main code============= ====================       
def search():
    print()
    print("_"*65)
    print("_"*65)
    print("\t\t Search ")
    x=PrettyTable()
    c_name=input(">>> Enter Your Name : ")
    print("_"*65)
    while True:
        c_cont=phone()
        if c_cont!="nonum":
            break
    while True:
        aadhaar_no=aadhaar()
        if aadhaar_no!="nonum":
            break
    print(" ENTER YOUR CHOICE OF PREFERENCE ")
    print("1. By Locality")
    print("2. By Cost")
    print("3. Show All Available Localities")
    while True:
        pre_fer=isnumber()
        if pre_fer!="nonum":
            break
    if pre_fer==1:
        ch10=input(">>> Enter Locality : ")
        print(" YOU WANT HOUSE ")
        print("1. For Rent")
        print("2. To Buy")
        print("_"*65)
        while True:
            rb=isnumber()
            if rb!="nonum":
                break
        while True:
            if rb==1:
                s_type="rent"
                break
            elif rb==2:
                s_type="sell"
                break
            else:
                print("Enter a valid choice")
                while True:
                    rb=isnumber()
                    if rb!="nonum":
                        break
        s1="select p_id,owner_name,p_type,address,locality,dimn,floor,cost,own_cont from property_info where status='vacant' and s_type='{}'and locality like'%{}%'".format(s_type,ch10[0:4])
        mycursor.execute(s1)
        data=mycursor.fetchall()
        print("_"*65)
        time.sleep(2)
        print("                          These Are Available Choices                  ")
        print("_"*65)
        x.field_names=["P_ID","OWNER NAME","P-TYPE","ADDRESS","LOCALITY","DIMENSION/BHK","FLOOR","COST","OWN_CONTACT"]
        for i in data:
            x.add_row(list(i))
        print(x)
        if data==[]:
            print("\t\tWE DO NOT SEEM TO HAVE THE HOUSE YOU WANTED....")
            print("\t\tSORRY FOR THE INCONVINIENCE")
            print("\t\tTRY FOR ANOTHER PROPERTIES..")
            print("_"*65)
            search()
            
        else:
            print(" Do You Like Any Deal 1 For YES And 2 For NO ")
            while True:
                d1=isnumber()
                if d1!="nonum":
                    break
            while True:
                if d1==1:
                    p1=int(input(">>> Enter The Corresponding P_ID : "))
                    break
                
                elif d1==2:
                    print("### Sorry Search For Any Other Deal ### ")
                    search()
                else:
                    print("Enter a valid choice")
                    while True:
                        d1=isnumber()
                        if d1!="nonum":
                            break
        
    elif pre_fer==2:
        print("  You Want House   ")
        print("1.For rent")
        print("2.To buy")
        print("_"*65)
        while True:
            rb=isnumber()
            if rb!="nonum":
                break
        while True:
            if rb==1:
                s_type="rent"
                break
            elif rb==2:
                s_type="sell"
                break
            else:
                print("  Enter a valid choice !!! ")
                search()
        try:
            cost=float(input("Cost Of your Prefernce : "))
        except:
            print("Enter valid cost !!!")
        s1="select p_id,owner_name,p_type,address,locality,dimn,floor,cost,own_cont from property_info where status='vacant' and s_type='{}'and cost between {}-1000 and {}+1000".format(s_type,cost,cost)
        mycursor.execute(s1)
        data=mycursor.fetchall()
        print("                                These Are Available Choices                           ")
        print("_"*65)
        x.field_names=["P_ID","OWNER NAME","P-TYPE","ADDRESS","LOCALITY","DIMENSION/BHK","FLOOR","COST","OWN_CONTACT"]
        for i in data:
            x.add_row(list(i))
        print(x)    
        if data==[]:
            print("          No Choices Are Available          ")
            print("_"*65)
            search()
        else:
           print("         Do You Like Any Deal 1 For Y And 2 For N :         ")
           while True:
                d1=isnumber()
                if d1!="nonum":
                    break 
           while True:
               if d1==1:
                   p1=int(input(">>> Enter The Corresponding P_ID : "))
                   break
               elif d1==2:
                   print("\t\t Sorry Search For Other Deal ")
                   main_menu()
               else:
                   while True:
                       d1=isnumber()
                       if d1!="nonum":
                           break
    elif pre_fer==3:
        print("  You Want House   ")
        print("1.For rent")
        print("2.To buy")
        print("_"*65)
        while True:
            rb=isnumber()
            if rb!="nonum":
                break
        while True:
            if rb==1:
                s_type="rent"
                break
            elif rb==2:
                s_type="sell"
                break
            else:
                print("  Enter a valid choice  ")
                search()
        s1="select p_id,owner_name,p_type,address,locality,dimn,floor,cost,own_cont from property_info where status='vacant' and s_type='{}'".format(s_type)
        mycursor.execute(s1)
        data=mycursor.fetchall()
        print("                                These Are Available Choices                           ")
        print("_"*65)
        x.field_names=["P_ID","OWNER NAME","P-TYPE","ADDRESS","LOCALITY","DIMENSION/BHK","FLOOR","COST","OWN_CONTACT"]
        for i in data:
            x.add_row(list(i))
        print(x)    
        if data==[]:
            print("          No Choices Are Available          ")
            print("_"*65)
            search()
        else:
           print("         Did You Like Any Deal(1 For Y And 2 For N)        ")
           while True:
                d1=isnumber()
                if d1!="nonum":
                    break 
           while True:
               if d1==1:
                   p1=int(input(">>> Enter The Corresponding P_ID : "))
                   break
               elif d1==2:
                   print("### Sorry Search For Any Other Deal ")
                   search()
               else:
                   while True:
                       d1=isnumber()
                       if d1!="nonum":
                           break
        
         
    else:
        print("Enter A Valid Number")
        while True:
            pre_fer=isnumber()
            if pre_fer!="nonum":
                break
    s4="select p_id,owner_name,p_type,address,locality,dimn,floor,cost,own_cont from property_info where status='vacant' and s_type='{}' and p_id={}".format(s_type,p1)
    mycursor.execute(s4)
    data2=mycursor.fetchall()
    if mycursor.rowcount==1:
        pass
    else:
        print("P_id Entered By You Is Not Correct")
        search()
    print("        Are You Sure To Continue          ")
    print('     If Yes Enter 1 ')
    print('     If No Enter 2 ')
    while True:
        choi_ce=isnumber()
        if choi_ce!="nonum":
            break
    if choi_ce==2:
        print("Want To Search For More Properties")
        print("1 For Yes And 2 For No")
        while True:
            pre1=isnumber()
            if pre1!="nonum":
                break
        if pre1==1:
            search()
        elif pre1==2:
            print('#####  Thank You  #####')
            main_menu()
        else:
            while True:
                pre1=isnumber()
                if pre1!="nonum":
                    break
                         
    elif choi_ce==1:
        print("   WE Request You To Contact Owner And Set Deal And Then Inform Us   ")
        time.sleep(3)
        input("Press 'ENTER' To Continue ")
        print("      So Is Deal Confirmed...?    ")
        print("1 for YES and 2 for NO")
        while True:
            choice2=isnumber()
            if choice2!="nonum":
                break
        if choice2==2:
            choice3=int(input("If You Want To Look Any Other Property Choose 1 Else 2: "))
            if choice3==2:
                print("     THANK YOU...VISIT AGAIN      ")
                print("_"*65)
                main_menu()
            elif choice3==1:
                search()
            else:
                print("Enter valid choices")
                search()
        elif choice2==1 and s_type=="rent":
            print("Congratulations......")
            time.sleep(3)
            print()
            s7="update property_info set status='occupied' where p_id={}".format(p1)
            mycursor.execute(s7)
            conn.commit()
            comm=(8*data[0][7])/100
            deal_amt=comm+data[0][7]
            print("      Commision Charged  : ",comm)
            print()
            print("      Deal Amount  : ",deal_amt)
            print()
            sql8="insert into trans_info(c_id,client_name,c_cont,s_type,comm,deal_amt,aadhaar_no,date) values({},'{}','{}','{}',{},{},'{}',curdate())".format(p1,c_name,c_cont,s_type,comm,deal_amt,aadhaar_no)
            mycursor.execute(sql8)
            conn.commit()
            print('YOUR DEAL HAS BEEN SUCCESSFULL ENTERED....:-)')
            time.sleep(1)
            print('THANK You ......')
            print("-"*65)
            print("-"*65)
            main_menu()
       
        elif choice2==1 and s_type=="sell":
            print("Congratulations......")
            time.sleep(3)
            print()
            s7="delete from property_info where p_id={}".format(p1)
            mycursor.execute(s7)
            conn.commit()
            comm=(2*data[0][7])/100
            deal_amt=comm+data[0][7]
            print("      Commision Charged  : ",comm)
            print()
            print("      Deal Amount  : ",deal_amt)
            print()
            sql8="insert into trans_info(c_id,client_name,c_cont,s_type,comm,deal_amt,aadhaar_no,date) values({},'{}','{}','{}',{},{},'{}',curdate())".format(p1,c_name,c_cont,s_type,comm,deal_amt,aadhaar_no)
            mycursor.execute(sql8)
            conn.commit()
            print("YOUR DEAL HAS BEEN SUCCESSFULL ENTERED....:-)")
            time.sleep(2)
            print()
            print("Thank You ......")
            print("-"*65)
            print("-"*65)
            print()
            input("Press 'ENTER' To Continue")
            main_menu()
           
    else:
        print("### Enter A Valid Choice ###")
        while True:
            cho_ice=isnumber()
            if cho_ice!="nonum":
                break
#=======================================Add account===========================================             
def add():
    print()
    print("_"*65)
    print("_"*65)
    print("\t\t Add Account ")
    x=PrettyTable()
    print()
    print("                Enter the following required details             ")
    owner_name=input(">>> Owner name : ")
    while True:
        aadhaar_no=aadhaar()
        if aadhaar_no!="nonum":
            break
    print('''Your House Is For
             1.Sell
             2.Rent''')
    while True:
            p=isnumber()
            if p!="nonum":
                break
    while True:
        if p==1:
            s_type="sell"
            break
        elif p==2:
            s_type="rent"
            break
        else:
           print("Enter a valid choice!!")
           while True:
               p=isnumber()
               if p!="nonum":
                   break
    address=input(">>> Address: ")
    locality=input(">>> Locality:")
    print('''Property type:
             1.House
             2.Flat''')
    
    while True:
            k=isnumber()
            if k!="nonum":
                break
    while True:
        if k==1:
            p_type="house"
            break
        elif k==2:
            p_type="flat"
            break
        else:
            print(" Enter a valid choice !!! ")
            while True:
                k=isnumber()
                if k!="nonum":
                    break
    dimn=input(">>> BHK/Dimension : ")
    floor=int(input(">>> Floor : "))
    cost=float(input(">>> Cost In Rupees : "))
    while True:
        own_cont=phone()
        if own_cont!="nonum":
            break
    sql1="insert into property_info(owner_name,aadhaar_no,own_cont,s_type,p_type,address,dimn,floor,locality,cost)\
          values('{}','{}','{}'\
         ,'{}','{}','{}','{}',{},'{}',{})"\
          .format(owner_name,aadhaar_no,own_cont,s_type,p_type,address,dimn,floor,locality,cost)
    mycursor.execute(sql1)
    conn.commit()
    s1="select p_id,owner_name,p_type,address,locality,dimn,floor,cost,own_cont from property_info where status='vacant' and aadhaar_no='{}'".format(aadhaar_no)
    mycursor.execute(s1)
    data30=mycursor.fetchall()
    print()
    print("##### Data Has Been Saved Successfully #####")
    x.field_names=["P_ID","OWNER NAME","P-TYPE","ADDRESS","LOCALITY","DIMENSION/BHK","FLOOR","COST","OWN_CONTACT"]
    for i in data30:
        x.add_row(list(i))
    print(x)
    time.sleep(2)
    print("### This Is Your P_id ### ",data30[0][0])
    print(" WARNING  :  Make Sure You Keep This P_id Otherwise You Want Be Able To Update Or Delete Your Records Any More")
    print("="*65)
    input("Press Enter To Continue")
    print()
    main_menu()
#===================delete================================================================    

def delete_acc():
    x=PrettyTable()
    print()
    print("_"*65)
    print("_"*65)
    print("\t\t Delete Account ")
    print(" Hope You Have p_id Provided To You 1 for Yes and 2 for N0 ")
    while True:
            c2=isnumber()
            if c2!="nonum":
                break
    print()
    if c2==1:
        p=int(input(">>> Enter The p_id Provided To You :"))
        while True:
            aadhaar_no=aadhaar()
            if aadhaar_no!="nonum":
                break
    else:
        print("Wait For Alternate Solution....")
        time.sleep(2)
        print(".....")
        print("    Login Through Aadhaar Number")
        while True:
            aadhaar_no=aadhaar()
            if aadhaar_no!="nonum":
                break
    s4="select p_id,owner_name,s_type,address,cost,own_cont from property_info where aadhaar_no='{}' ".format(aadhaar_no)
    mycursor.execute(s4)
    data3=mycursor.fetchall()
    if mycursor.rowcount==1:
        print()
        print("Loading...")
        time.sleep(1)
        print("Loading...")
        time.sleep(1)
        print("    You have selected to delete your property with details     ")
        x.field_names=["P_ID","OWNER NAME","S_TYPE","ADDRESS","COST","OWN_CONT"]
        for i in data3:
            x.add_row(list(i))
        print(x)
        print()
        print("     Are you sure to drop it from records1 For Yes And 2 For No    ")
        while True:
            c1=isnumber()
            if c1!="nonum":
                break
        if c1==2:
            print("\t\t Thank you for continuing ")
            input("\t\tPress 'ENTER' To Continue")
            main_menu()
        elif c1==1:
            s5="delete from property_info where p_id={}".format(data3[0][0])
            mycursor.execute(s5)
            conn.commit()
            print("      Your Record Has Been Successfully Deleted    ")
            main_menu()
        else:
            print("Please Enter Valid Number Only")
            delete_acc()
    else:
        print("    ...........FAILED.................   ")
        print()
        print("     It might be the case that either aadhaar number or p_id number entered by you is wrong    ")
        delete_acc()
#=====================update============================================================
def update():
    print()
    print("_"*65)
    print("_"*65)
    print("\t\t Update Property Details ")
    print()
    x=PrettyTable()
    print("          You can update following details    ")
    print("  1.) UPDATE PHONE NUMBER")
    print("  2.) UPDATE COST  ")
    print("  3.) NAME OF THE OWNER  ")
    print("  4.) RENT TO SELL  ")
    print("  5.) Status To Vacant ")
    print("  6.) Main_Menu ")
    print()
    while True:
            c1=isnumber()
            if c1!="nonum":
                break
    print("Hope You Have p_id Provided To You 1 Y Or 2 N ")
    while True:
            c2=isnumber()
            if c2!="nonum":
                break
    if c2==1:
        print()
        p=int(input(">>> Enter The p_id Provided To You :"))
        while True:
            aadhaar_no=aadhaar()
            if aadhaar_no!="nonum":
                break
        s4="select p_id,owner_name,s_type,address,cost,own_cont from property_info where p_id={} and aadhaar_no='{}' ".format(p,aadhaar_no)
        mycursor.execute(s4)
        data3=mycursor.fetchall()
    else:
        print("Wait For Alternate Solution....")
        time.sleep(2)
        print(".....")
        print("    Login Through Aadhaar Number")
        while True:
            aadhaar_no=aadhaar()
            if aadhaar_no!="nonum":
                break
        s4="select p_id,owner_name,s_type,address,cost,own_cont from property_info where aadhaar_no='{}' ".format(aadhaar_no)
        mycursor.execute(s4)
        data3=mycursor.fetchall()
    if mycursor.rowcount==1:
        print("    You Have Selected To Update Your Property With Details    ")
        x.field_names=["P_ID","OWNER NAME","S_TYPE","ADDRESS","COST","OWN_CONT"]
        for i in data3:
            x.add_row(list(i))
        print(x)    
    else:
        print("           ..........Failed.............        ")
        print()
        print("   It might be the case that either aadhaar number or p_id number entered by you is wrong   ")
        update()
    
    if c1==3:
        new_name=input(">>> Provide Us Your New Name : ")
        if new_name=='':
            print("It Can't Be Empty !!!")
            update()
        else:
            pass
        s7="update property_info set owner_name='{}' where owner_name='{}'".format(new_name,data3[0][1])
        mycursor.execute(s7)
        conn.commit()
    elif c1==2:
        new_cost=input(">>> New Cost For Your House : ")
        if new_cost=='':
            print("It Can't Be Empty !!!")
            update()
        else:
            pass
        s7="update property_info set cost={} where cost={}".format(new_cost,data3[0][4])
        mycursor.execute(s7)
        conn.commit()
    elif c1==1:
        while True:
            new_cont=phone()
            if new_cont!="nonum":
                break
        s7="update property_info set own_cont='{}' where own_cont='{}'".format(new_cont,data3[0][5])
        mycursor.execute(s7)
        conn.commit()
        
    elif c1==4:
        s_type="sell"
        s7="update property_info set s_type='{}' where aadhaar_no='{}'".format(s_type,aadhaar_no)
        mycursor.execute(s7)
        conn.commit()
    elif c1==5:
        status="occupied"
        print("\t\t Are You Sure To Change Your Status To Vacant 1 For Yes")
        ch23=isnumber()
        if ch23==1:
            s7="update property_info set status='{}' where aadhaar_no='{}'".format(status,aadhaar_no)
        else:
            print("\t\tReturning Bach To Main_Menu")
            print("Loading......")
            time.sleep(2)
            main_menu()
    elif c1==6:
        main_menu()
    else:
        while True:
            c1=isnumber()
            if c1!="nonum":
                break
    print(" Your Record Has Been Successfully Updated ")
    print()
    print("   New Record   ")
    s50="select p_id,owner_name,s_type,address,cost,own_cont from property_info where p_id={}".format(data3[0][0])
    mycursor.execute(s50)
    data50=mycursor.fetchall()
    x.field_names=["P_ID","OWNER NAME","S_TYPE","ADDRESS","COST","OWN_CONT"]
    for i in data50:
        x.add_row(list(i))
    print(x)
    input("\t\tPress 'ENTER To Continue'")
    main_menu()


#=====================About us===========================

def about_us(): 
    print()
    print('|','-'*50,'|')
    print('|','                       ABOUT US                    |')
    print('|','-'*50,'|')
    print('|',' FOR QUERIES,FEEDBACK & ALLIANCE REACH US AT       |')
    print('|','-'*50,'|')
    print('|','                     LUXURY HOMES                  |')
    print('|','-'*50,'|')
    print('|','TIMES CENTER(DIGITAL CONTENT PRODUCTION FACILITY)  |')
    print('|','FC-6,(GROUND FLOOR),SECTOR 16A,FILM CITY           |')
    print('|','RATLAM-457001                                      |')
    print('|','-'*50,'|')
    print('|','CONTACT US:0120-686660000                          |')
    print('|','Email:support@luxuryhomes.com                      |')
    print('|','-'*50,'|')
    print('|','FOR CORPORATE ALLIANCES                            |')
    print('|','Email:times.primlani@timesgroup.com                |')
    print('|','-'*50,'|')
    input("Press 'ENTER' To Continue")
    main_menu()
#=====================market status===========================
def m_status():
    print()
    print("#### Here You Will Get To Know About Market Prices Of Properties In Different Parts Of Countries ### ")
    print()
    delhi=9087
    mumbai=10242
    bhopal=2212
    indore=2295
    kolkata=6035
    chennai=6055
    list1=['delhi','mumbai','bhopal','indore','kolkata','chennai']
    list2=[delhi,mumbai,bhopal,indore,kolkata,chennai]
    plt.bar(list1,list2,color=["b","k","m","g","c","y","r"])
    plt.xticks(list1,["DELHI","MUMBAI","BHOPAL","INDORE","KOLKATA","CHENNAI"])
    plt.title("______________________PROPERTY PRICE STATUS__________________________")
    plt.xlabel("CITY")
    plt.ylabel("PRICES (In Square Feet)")
    time.sleep(4)
    plt.show()
    input("Press 'ENTER' To Continue")
    main_menu()

def main_menu():
    print("="*30,"MAINMENU","="*30)
    print("="*69)
    print()
    print("1.Search house")
    print("2.Add property")
    print("3.Delete property")
    print("4.Update property")
    print("5.About us")
    print("6.Price Status")
    print("7.Logout")
    print("8.Exit")
    print()
    choice=input(">>> Enter Menu To Open  : ")
    if choice=="1":
        search()
    elif choice=="2":
        add()
    elif choice=="3":
        delete_acc()
    elif choice=="4":
        update()
    elif choice=="5":
        about_us()
    elif choice=="6":
        m_status()
    elif choice=="7":
        login()
    elif choice=="8":
        exit()
    else:
        print()
        print("\t\t The Menu Entered By You Do not Exist ")
        print()
        main_menu()
   
def login():
    print()    
    print()        
    a=input(">>> Enter Username : ")
    b=input(">>> Enter Password : ")
    sql="select * from login where username='{}' and password='{}'".format(a,b)
    mycursor.execute(sql)
    mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount==1:
        print()
        time.sleep(1)
        print("......Loading")
        print(".")
        print(".")
        print(".")
        time.sleep(1)
        print("......Loading")
        print(".")
        print(".")
        print(".")
        time.sleep(1)
        print("......Loading")
        print(".")
        print(".")
        print(".")
        time.sleep(1)
        print("......Loading")
        print(".")
        print(".")
        print(".")
        print("......ACCESS CONFIRMED")
        time.sleep(1)
        print()
        main_menu()
               
    else:
        print()
        print("......ACCESS DENIED")
        time.sleep(1)
        print()
        login()
         
login()



    
