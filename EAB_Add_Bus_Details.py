import sqlite3
conn=sqlite3.Connection("bus_booking.db")
cur=conn.cursor()
from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

#Connection Functions
def home():
    root.destroy()
    import BE2

#Add Bus Details function
def add_bd():
        ibid=bid.get()
        it=t.get()
        icap=cap.get()
        ifare=fare.get()
        iopid=opid.get()
        irid=rid.get()
        try:
            if str(ibid)=="":
                cur.execute("insert into BUS(TYPE, CAPACITY, FARE, OPID, ROUTEID) values('{}',{},{},{},{})".format(it, icap, ifare, iopid, irid))
            else:
                cur.execute("insert into BUS values({}, '{}',{},{},{},{})".format(ibid ,it, icap, ifare, iopid, irid))
            Label(options, text="{}".format((ibid)+" "+str(it)+" "+str(icap)+" "+str(ifare)+" "+str(iopid)+" "+str(irid))).grid(row=1,column=0, columnspan=11)
            mb.showinfo("Bus Details Entry", message="Bus Record Added")
            conn.commit()
        except sqlite3.OperationalError:
            mb.showerror("Invalid Input", message="Unacceptable Input.")
            raise a
        except sqlite3.IntegrityError:
            mb.showerror("DB insertion Error", message="Bus Record Already Exists")

#edit Bus Details funtion
def edit_bop():
        ibid=bid.get()
        it=t.get()
        icap=cap.get()
        ifare=fare.get()
        iopid=opid.get()
        irid=rid.get()
        try:
            cur.execute("update bus SET TYPE='{}', CAPACITY={}, FARE={}, OPID={}, ROUTEID={} where BUSID={}".format(it, icap, ifare, iopid, irid, ibid))
            Label(options, text="{}".format(str(ibid)+" "+str(it)+" "+str(icap)+" "+str(ifare)+" "+str(iopid)+" "+str(irid))).grid(row=1,column=0, columnspan=11)
            mb.showinfo("Bus Entry Updated", message="Bus Record updated Successfully")
            conn.commit()
        except sqlite3.OperationalError:
            mb.showerror("Invalid Input", message="Unacceptable Input.")
        except sqlite3.IntegrityError:
            mb.showerror("Record Not Found", message="Bus Record does not Exists")

#basic Headings
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0)
root.update()
a=w-H.winfo_width()
H.destroy()
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0, padx=a//2)

Label(root, text="Add Bus Details", fg="green", font=("Arial Bold", 30)).grid(row=2, column=0, pady=30)

options=Frame(root)
Label(options, text="Bus ID", font=("Arial Bold", 15)).grid(row=0, column=0, padx=10)
bid=Entry(options, font=("Arial Bold", 15), width=6)
bid.grid(row=0, column=1, padx=10)
Label(options, text="Bus Type", font=("Arial Bold", 15)).grid(row=0, column=2, padx=10)
t=StringVar()
t.set("Bus Type")
types=["AC 2X2", "AC 3X2", "Non AC 2X2", "Non AC 3X2", "AC-Sleeper 2X1", "Non-AC Sleeper 2X1"]
btype=OptionMenu(options, t, *types)
btype.config(font=14)
btype.grid(row=0, column=3, padx=10)
Label(options, text="Capacity", font=("Arial Bold", 15)).grid(row=0, column=4, padx=10)
cap=Entry(options, font=("Arial Bold", 15), width=5)
cap.grid(row=0, column=5, padx=10)
Label(options, text="Fare Rs", font=("Arial Bold", 15)).grid(row=0, column=6, padx=10)
fare=Entry(options, font=("Arial Bold", 15), width=5)
fare.grid(row=0, column=7, padx=10)
Label(options, text="Operator ID", font=("Arial Bold", 15)).grid(row=0, column=8, padx=10)
opid=Entry(options, font=("Arial Bold", 15), width=5)
opid.grid(row=0, column=9, padx=10)
Label(options, text="Route ID", font=("Arial Bold", 15)).grid(row=0, column=10, padx=10)
rid=Entry(options, font=("Arial Bold", 15), width=5)
rid.grid(row=0, column=11, padx=10)
addb=Button(options, text="Add Bus", bg="#7fd27b", font=("Arial Bold", 15), command=add_bd).grid(row=1, column=6, pady=50)
editb=Button(options, text="Edit Bus", bg="#7fd27b", font=("Arial Bold", 15), command=edit_bop).grid(row=1, column=7, pady=50)
hm=PhotoImage(file="./assets/home.png")
home=Button(options, image=hm, command=home).grid(row=1, column=8, pady=50)


options.grid(row=3,column=0, pady=50)

root.mainloop()
conn.commit()
conn.close()

