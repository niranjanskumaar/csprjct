"""

Canteen Management App 

manav eee appinte aishwaryam

"""


# MODULES

import os 
import csv
import pickle

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
            if s['st_balance'] >= 45:
                s['st_booked'] = True
                s['st_balance'] -= 45
                op = "SUCCESS: Booked Coupon for {} ({})".format(s['st_name'], s['st_adm'])
            else:
                op = "ERR 103: Insufficient Balance for {} ({})".format(s['st_name'], s['st_adm'])
                
        pickle.dump(s, wf)

    wf.close()
    return op

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

# initialize_student(7301, "Shreya K Subash", "XII A1", "vazire")
# initialize_student(7302, "Niranjan S Kumar", "XII A1", "0712")
# initialize_student(7303, "Vivek Purushothaman", "XII A1", "adi")
# initialize_student(7304, "Manav Ashok", "XII A1", "odi")


print(increment_balance(7304, 160))
temp_print_db()