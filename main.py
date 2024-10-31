"""

Canteen Management App 

manav eee appinte aishwaryam

"""


# MODULES

import os 
import csv
import time
import pickle
import datetime

# DIRECTORIES
SPREADSHEET_DIR = "./spreadsheets/"
DATA_DIR = "./data/"
BOOKING_DIR = DATA_DIR + "/bookingdata/"
USER_DATA = DATA_DIR + "/USER.DAT"
STAFF_DATA = DATA_DIR + "/STAFF.DAT"


# CORE FUNCTIONS

def init_databases():
    pass    

def initialize_student(st_adm: int, st_name: str, st_class: str, st_password: str):
    rf = open(USER_DATA, "rb")

    students = []

    try:
        while True:
            cur_data = pickle.load(rf)
            if cur_data['st_adm'] == st_adm:
                return "ERR 101: Tried to initialize a pre-existing student user."
            else:
                students.append(cur_data)
    except EOFError:
        pass

    rf.close()
    wf = open(USER_DATA, "wb")

    st_data = {
        "st_adm": st_adm, 
        "st_name": st_name, 
        "st_class": st_class, 
        "st_balance": 0,
        "st_booked": False,
        "st_password": st_password
    }

    students.append(st_data)

    for s in students:
        pickle.dump(s, wf)

    wf.close()
    return st_data

def initialize_teacher(te_id: int, te_name: str, te_class: list, te_password: str):

    rf = open(STAFF_DATA, "rb")

    teachers = []

    try:
        while True:
            cur_data = pickle.load(rf)
            if cur_data['te_id'] == te_id:
                return "ERR 101: Tried to initialize a pre-existing teacher user."
            else:
                teachers.append(cur_data)
    except EOFError:
        pass

    rf.close()
    wf = open(STAFF_DATA, "wb")

    te_data = {
        "te_id": te_id, 
        "te_name": te_name, 
        "te_class": te_class,
        "te_password": te_password
    }

    teachers.append(te_data)

    for s in teachers:
        pickle.dump(s, wf)

    wf.close()
    return te_data

def temp_print_db():
    rf = open(USER_DATA, "rb")

    try:
        while True:
            cur_data = pickle.load(rf)
            print(cur_data)
    except EOFError:
        pass 

    rf.close()

def book_student(st_adm: int):
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    wf = open(USER_DATA, "wb") 

    for s in students:
        if s['st_adm'] == st_adm:
            if s['st_booked'] == False:
                if s['st_balance'] >= 45:
                    s['st_booked'] = True
                    s['st_balance'] -= 45
                    op = "SUCCESS: Booked Coupon for {} ({})".format(s['st_name'], s['st_adm'])
                else:
                    op = "ERR 103: Insufficient Balance for {} ({})".format(s['st_name'], s['st_adm'])
            else:
                op = "ERR 104: Coupon is already booked. If this is a mistake, contact Administrator."    

        pickle.dump(s, wf)

    wf.close()
    return op

def force_student_book(st_adm: int):
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    wf = open(USER_DATA, "wb") 

    for s in students:
        if s['st_adm'] == st_adm:
            if s['st_booked'] == False:
                s['st_booked'] = True
                op = "SUCCESS: Booked Coupon for {} ({})".format(s['st_name'], s['st_adm'])

            else:
                op = "ERR 104: Coupon is already booked."

        pickle.dump(s, wf)

    wf.close()
    return op

def generate_entire_csv():
    rf = open(USER_DATA, "rb")

    date = datetime.datetime.now()
    datestring = "{}-{}-{}".format(date.day, date.month, date.year)
    path = f"{SPREADSHEET_DIR}/{datestring}.csv"
    csvf = open(path, "w", newline="")

    writer = csv.writer(csvf, delimiter=",")
    header = ("SI No", "Name", "Class")
    writer.writerow(header)
    students = []


    try:
        while True:
            s_data = pickle.load(rf)
            students.append(s_data)
    except EOFError:
        pass
    
    i = 1
    for student in students:
        st_name = student['st_name']
        st_class = student['st_class']
        data = (i, st_name, st_class)
        writer.writerow(data)
        i += 1

    csvf.close()
    rf.close()
    
    return path

def generate_class_csv(te_class: str):
    rf = open(USER_DATA, "rb")

    date = datetime.datetime.now()
    datestring = "{}-{}-{}".format(date.day, date.month, date.year)
    path = f"{SPREADSHEET_DIR}/{te_class}_{datestring}.csv"
    csvf = open(path, "w", newline="")

    writer = csv.writer(csvf, delimiter=",")
    header = ("SI No", "Name")
    writer.writerow(header)
    students = []


    try:
        while True:
            s_data = pickle.load(rf)
            students.append(s_data)
    except EOFError:
        pass
    
    i = 1
    for student in students:
        st_name = student['st_name']
        st_class = student['st_class']
        if st_class.lower() in te_class.lower():
            data = (i, st_name)
            writer.writerow(data)
            i += 1

    csvf.close()
    rf.close()
    
    return path

def increment_balance(st_adm: int, i_amt: int):
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    wf = open(USER_DATA, "wb") 

    for s in students:
        if s['st_adm'] == st_adm:
            s['st_balance'] += i_amt
            op = "SUCCESS: Increased balance by {}".format(i_amt)
        pickle.dump(s, wf)

    wf.close()

    return op
    
def reset_bookings():
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    wf = open(USER_DATA, "wb") 

    for s in students:
        s['st_booked'] = False

        pickle.dump(s, wf)
    op = "SUCCESS: Reset all bookings."


    wf.close()
    return op

def check_booked(st_adm: int):
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    wf = open(USER_DATA, "wb") 

    for s in students:
        if s['st_adm'] == st_adm:
            if s['st_booked'] == True:
                return True
            else:
                return False
        pickle.dump(s, wf)

    wf.close()

def get_booked_list():
    rf = open(USER_DATA, "rb")
    booked = []
    try:
        while True:
            s_data = pickle.load(rf)
            if s_data['st_booked'] == True:
                booked.append(s_data)
    except EOFError:
        pass
    
    rf.close()
    return booked

def get_class_list(te_class: str):
    rf = open(USER_DATA, "rb")
    booked = []
    try:
        while True:
            s_data = pickle.load(rf)
            if s_data['st_class'] == te_class:
                if s_data['st_booked'] == True:
                    booked.append(s_data)
    except EOFError:
        pass
    
    rf.close()
    return booked

def get_booked_count():
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    booked = 0

    for s in students:
        if s['st_booked'] == True:
            booked += 1

    return booked

def get_class_booked_count(te_class: str):
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    booked = 0

    for s in students:
        if s['st_booked'] == True:
            if s['st_class'] == te_class:
                booked += 1

    return booked

def get_student_data(st_adm: int):
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    for s in students:
        if s['st_adm'] == st_adm:
            return s   
        
def get_teacher_data(te_id: int):
    rf = open(STAFF_DATA, "rb")
    
    teachers = []
    try:
        while True:
            cur_data = pickle.load(rf)
            teachers.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    for t in teachers:
        if t['te_id'] == te_id:
            return t   

def s_login(st_adm: int, st_password: str):
    rf = open(USER_DATA, "rb")
    
    students = []
    try:
        while True:
            cur_data = pickle.load(rf)
            students.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    for s in students:
        if s['st_adm'] == st_adm:
            if s['st_password'] == st_password:
                return "std"
            else:
                return "incpass"
    
    return "nostudent"

def te_login(te_id: int, te_password: str):
    rf = open(STAFF_DATA, "rb")
    
    teachers = []
    try:
        while True:
            cur_data = pickle.load(rf)
            teachers.append(cur_data)
    except EOFError:
        pass
    
    rf.close()

    for t in teachers:
        if t['te_id'] == te_id:
            if t['te_password'] == te_password:
                return "teacher"
            else:
                return "incpass"
    
    return "noteacher"

def admin_login(username, password):
    if username == "admin":
        if password == "admin":
            return "admin"
        else:
            return "incpass"
    else:
        return "nouser"

prompts = [
# prompt 1
"""
============================================
\tCanteen Management App v1.0
============================================

Functions

    [1]: Login as student
    [2]: Login as staff
    [3]: Login as administrator
    [4]: Exit

SELECT AN OPTION: """,

# prompt 2
"""
======================================
\tENTER YOUR CREDENTIALS
======================================
\n""",

# prompt 3
"""Logged in as: {}

    BOOKING STATUS: {}
    ACCOUNT BALANCE: ₹{}

=================================
\tFUNCTIONS
=================================
\n
    [1]: Book Coupon
    [2]: Add funds
    [3]: Logout

SELECT AN OPTION: """,

# prompt 4
"""Logged in as: admin

TOTAL BOOKED COUNT: {}

============================
\tFUNCTIONS
============================
\n
    [1]: Initialize a new student
    [2]: Initialize a new teacher
    [3]: Get the total booking count
    [4]: Generate a spreadsheet
    [5]: Force Student Booking
    [6]: Reset all bookings
    [7]: Logout

SELECT AN OPTION: """,

# prompt 5
"""
========================================
\tSTUDENT INITIALIZATION
========================================

""",

# prompt 6
"""
=======================
\tSUCCESS
=======================

Added database entry for {} ({})
""",

# prompt 7
"""
========================================
\tPAYMENT GATEWAY
========================================

""",

# prompt 8
"""Logged in as: {}

    CLASS HANDLED: {}
    BOOKINGS FROM CLASS: {}

=================================
\tFUNCTIONS
=================================
\n
    [1]: Generate spreadsheet for class
    [2]: Logout

SELECT AN OPTION: """,

# prompt 9
"""
========================================
\tTEACHER INITIALIZATION
========================================

""",
]

def student():
    print(prompts[1])
    time.sleep(2)

    try:
        st_adm = int(input("Admission No: "))
        st_password = input("Password: ")

    except ValueError:
        print()
        print("[⚠] Expected integers for admission no; Received string. Please try again.")
        
        

    logged_in = s_login(st_adm, st_password)

    print()

    if logged_in == "std":
        while True:
            std_data = get_student_data(st_adm)
            x = input(prompts[2].format(std_data['st_name'], std_data['st_booked'], std_data['st_balance']))

            if x == "1":
                print()

                result = book_student(st_adm)
                print(result)
                time.sleep(2)
                print()

            if x == "2":
                print(prompts[6])
                try:
                    amount = int(input("Enter Amount: "))
                except ValueError:
                    print("[⚠] Expected amount in integers; Received string. Please try again.")
                    time.sleep(2)

                    continue
                finally:
                    if amount < 45:
                        print("[⚠] A minimum of ₹45 required. Please try again.")
                        continue
                time.sleep(2)

                print()                            
                result = increment_balance(st_adm, amount)
                print(result)
                time.sleep(2)

                print()                            
                
            if x == "3":
                break


    elif logged_in == "incpass":
        print("[⚠] Incorrect password, try Again.")
    
    elif logged_in == "nostudent":
        print("[⚠] Found no student account with that admission number ({}). Contact administrator to add student account.".format(st_adm)) 
        
    else:
        print("[⚠] An unknown error has occurred.")    

def teacher():
    print(prompts[1])

    try:
        te_id = int(input("Teacher ID: "))
        te_password = input("Password: ")

    except ValueError:
        print()
        print("[⚠] Expected integers for teacher ID; Received string. Please try again.")

        

    time.sleep(2)
    logged_in = te_login(te_id, te_password)

    print()

    if logged_in == "teacher":
        while True:
            tea_data = get_teacher_data(te_id)
            te_class = tea_data['te_class']
            class_bookings = get_class_booked_count(te_class)
            x = input(prompts[7].format(tea_data['te_name'], te_class, class_bookings))

            if x == "1":
                path = generate_class_csv(te_class)
                print()
                print("SUCCESS: Spreadsheet has been created. ({})".format(path))
                print()
                time.sleep(2)

            if x == "2":
                break


    elif logged_in == "incpass":
        print("[⚠] Incorrect password, try Again.")
    
    elif logged_in == "noteacher":
        print("[⚠] Found no teacher account with that teacher ID ({}). Contact administrator to add student account.".format(st_adm)) 
        
    else:
        print("[⚠] An unknown error has occurred.")    



def admin():
    print(prompts[1])

    username = input("Username: ")
    password = input("Password: ")

    logged_in = admin_login(username, password)

    print()
    
    if logged_in == "admin":
        while True:       
            booked = get_booked_count()
            x = input(prompts[3].format(booked))
            if x == "1":
                # Student Initializaton
                print(prompts[4])
                try: 
                    adm_no = int(input("Admission No: "))
                    name = input("Name: ")
                    st_class = input("Class: ")
                    pwd = input("Password: ")
                
                except ValueError:
                    print()
                    print("[⚠] Expected integers for admission no; Received string. Please try again.")
                    continue


                time.sleep(0.5) 
                student = initialize_student(adm_no, name, st_class, pwd)

                print(prompts[5].format(student['st_name'], student['st_adm']))
                time.sleep(2)

            if x == "2":
                # Teacher Initializaton
                print(prompts[8])
                try: 
                    te_id = int(input("Teacher ID: "))
                    te_name = input("Name: ")
                    te_class = input("Class Handled: ")
                    pwd = input("Password: ")
                
                except ValueError:
                    print()
                    print("[⚠] Expected integers for admission no; Received string. Please try again.")
                    continue


                teacher = initialize_teacher(te_id, te_name, te_class, pwd)

                print(prompts[5].format(teacher['te_name'], teacher['te_id']))
                time.sleep(2)

            if x == "3":
                print()
                print("TOTAL BOOKINGS: {}".format(booked))
                print()
                time.sleep(2)

            if x == "4":
                path = generate_entire_csv()
                print()
                print("SUCCESS: Spreadsheet has been created. ({})".format(path))
                print()
                time.sleep(2)

            if x == "5":
                try:
                    st_adm = int(input("Admission No: "))
                except ValueError:
                    print()
                    print("[⚠] Expected integers for admission no; Received string. Please try again.")
                    time.sleep(2)

                result = force_student_book(st_adm)
                print()
                print(result)

            if x == "6":
                print()
                result = reset_bookings()
                print(result)
                print()
                time.sleep(2)

            if x == "7":
                break

            if x == "8":
                temp_print_db()
            
    elif logged_in == "incpass":
        print("[⚠] Incorrect password, try Again.")
    elif logged_in == "nouser":
        print("[⚠] Incorrect username, try Again.")
    else:
        print("[⚠] An unknown error has occurred.")
        return

def mainloop():
    while True:

        choice = input(prompts[0])

        if choice == "1":
            student()

        if choice == "2":

            teacher()

        elif choice == "3":
            admin()
        elif choice == "4":
            break

    


mainloop()
