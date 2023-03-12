#This project is made by Sukumar Rastogi(211B395) B11
#This project is made by Sukumar Rastogi(211B395) B11
#This project is made by Sukumar Rastogi(211B395) B11
#This project is made by Sukumar Rastogi(211B395) B11
#This project is made by Sukumar Rastogi(211B395) B11

#This Python Script will create a dummy Database to combine with the rest of the modules for a test run

import sqlite3
conn=sqlite3.Connection("bus_booking.db")
cur=conn.cursor()

# creating all the tables in database
try:
    cur.execute("""
        create table OPERATOR(
        OPID INTEGER PRIMARY KEY AUTOINCREMENT, 
        ONAME TEXT, 
        ADDRESS TEXT, 
        EMAIL TEXT, 
        PHONE INTEGER
        )""")
    cur.execute("""
        create table ROUTE(
        ROUTEID INTEGER,
        SID INTEGER,
        SNAME TEXT,
        PRIMARY KEY(ROUTEID, SID)
        )""")
    cur.execute("""create table BUS(
        BUSID INTEGER PRIMARY KEY AUTOINCREMENT,
        TYPE TEXT, 
        CAPACITY INTEGER, 
        FARE INTEGER, 
        OPID INTEGER, 
        ROUTEID INTEGER, 
        CONSTRAINT fk_operator 
        FOREIGN KEY (OPID) 
        REFERENCES OPERATOR(OPID),
        CONSTRAINT fk_route 
        FOREIGN KEY (ROUTEID) 
        REFERENCES ROUTE(ROUTEID)
        )""")
    cur.execute("""create table RUNS(
        BUSID INTEGER, 
        DATE DATE, 
        SEAT_AVAIL INTEGER, 
        PRIMARY KEY(BUSID, DATE), 
        CONSTRAINT fk_bus 
        FOREIGN KEY (BUSID) 
        REFERENCES BUS(BUSID)
        )""")
    cur.execute("""create table BOOKING_HISTORY(
        REF_NO INTEGER, 
        NAME TEXT, 
        GENDER TEXT,
        BUSID INTEGER, 
        SEATS INTEGER, 
        DBOOK TEXT,
        DSTART TEXT, 
        AGE INTEGER,
        BOARD_S TEXT,
        CONSTRAINT fk_bus 
        FOREIGN KEY (BUSID) 
        REFERENCES BUS(BUSID)
        )""")
except:
    pass

# populating the database

#Bus
cur.execute("insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values('AC 2X2', 30, 2000, 1, 1)")
cur.execute('insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values("AC 3X2", 25, 2400, 2, 2)')
cur.execute('insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values("Non AC 2X2", 40, 1500, 3, 1)')
cur.execute('insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values("Non AC 3X2", 35, 1700, 4, 4)')
cur.execute('insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values("AC-Sleeper 2X1", 25, 2500, 3, 5)')
cur.execute('insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values("Non-AC Sleeper 2X1", 28, 2000, 6, 4)')

#Route
cur.execute('insert into ROUTE values(1,1,"Guna")')
cur.execute('insert into ROUTE values(1,2,"JP collage")')
cur.execute('insert into ROUTE  values(1,3,"Binaganj")')
cur.execute('insert into ROUTE  values(1,4,"Biora")')
cur.execute('insert into ROUTE  values(1,5,"Bhopal")')
cur.execute('insert into ROUTE  values(2,1,"Bhopal")')
cur.execute('insert into ROUTE  values(2,2,"Biora")')
cur.execute('insert into ROUTE  values(2,3,"Binaganj")')
cur.execute('insert into ROUTE  values(2,4,"JP collage")')
cur.execute('insert into ROUTE  values(2,5,"Guna")')
cur.execute('insert into ROUTE  values(3,1,"Delhi")')
cur.execute('insert into ROUTE  values(3,2,"Agra")')
cur.execute('insert into ROUTE  values(3,3,"Jhasi")')
cur.execute('insert into ROUTE  values(3,4,"Shivpuri")')

#OPERATOR
cur.execute('insert into OPERATOR values(1,"Kamla","AB Road Guna","Kamla@gmail.com",1231231231)')
cur.execute('insert into OPERATOR values(2,"Best","AB Road Guna","Best@gmail.com",2312312311)')
cur.execute('insert into OPERATOR values(3,"Ram","harinager delhi","Ram@gmail.com",4324324321)')
cur.execute('insert into OPERATOR values(4,"Mohan","AB road jhasi","Mohan@gmail.com",5435435432)')

#Run
cur.execute('insert into RUNS values(1,"2022-11-20",30)')
cur.execute('insert into RUNS values(1,"2022-11-21",30)')
cur.execute('insert into RUNS values(1,"2022-11-22",30)')
cur.execute('insert into RUNS values(3,"2022-11-20",30)')
cur.execute('insert into RUNS values(4,"2022-11-23",30)')
cur.execute('insert into RUNS values(2,"2022-11-24",30)')
cur.execute('insert into RUNS values(2,"2022-11-25",30)')
cur.execute('insert into RUNS values(3,"2022-11-26",30)')
cur.execute('insert into RUNS values(4,"2022-11-27",30)')
cur.execute('insert into RUNS values(5,"2022-11-28",30)')
cur.execute('insert into RUNS values(6,"2022-11-29",30)')
cur.execute('insert into RUNS values(5,"2022-11-30",30)')
cur.execute('insert into RUNS values(6,"2022-12-1",30)')

# Booking History
cur.execute('insert into BOOKING_HISTORY values(1234567890,"Sukumar", "Male",1, 2, "2022-11-19", "2022-11-20", 19, "Guna")')

#These are the loops for populating database from the terminal instead fo putting the values directly in the script

# # Bus
# for i in range(1):
#     typ=input("bus type: ")
#     cap=input("bus capacity: ")
#     fare=input("bus fare: ")
#     opid=input("bus opid: ")
#     rid=input("bus routeid: ")
#     cur.execute("""
#     insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
#     values(
#         '{}', {}, {}, {}, {}
#     )
#     """.format(typ, cap, fare, opid, rid))
# # Operator
# for i in range(1):
#     typ=input("bus type: ")
#     cap=input("bus capacity: ")
#     fare=input("bus fare: ")
#     opid=input("bus opid: ")
#     rid=input("bus routeid: ")
#     cur.execute("""
#     insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
#     values(
#         '{}', {}, {}, {}, {}
#     )
#     """.format(typ, cap, fare, opid, rid))

# # Route
# for i in range(1):
#     typ=input("bus type: ")
#     cap=input("bus capacity: ")
#     fare=input("bus fare: ")
#     opid=input("bus opid: ")
#     rid=input("bus routeid: ")
#     cur.execute("""
#     insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
#     values(
#         '{}', {}, {}, {}, {}
#     )
#     """.format(typ, cap, fare, opid, rid))

# # Runs
# for i in range(1):
#     typ=input("bus type: ")
#     cap=input("bus capacity: ")
#     fare=input("bus fare: ")
#     opid=input("bus opid: ")
#     rid=input("bus routeid: ")
#     cur.execute("""
#     insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
#     values(
#         '{}', {}, {}, {}, {}
#     )
#     """.format(typ, cap, fare, opid, rid))

# # Booking History
# for i in range(1):
#     typ=input("bus type: ")
#     cap=input("bus capacity: ")
#     fare=input("bus fare: ")
#     opid=input("bus opid: ")
#     rid=input("bus routeid: ")
#     cur.execute("""
#     insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID)
#     values(
#         '{}', {}, {}, {}, {}
#     )
#     """.format(typ, cap, fare, opid, rid))


conn.commit()
conn.close()
