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
    import BE3

#Add Bus Route Details function
def add_rd():
        irid=rid.get()
        isid=sid.get()
        isname=sname.get()
        try:
            cur.execute("insert into ROUTE values({},{},'{}')".format(irid, isid, isname))
            Label(options, text="".format(str(irid)+" "+str(isid)+" "+str(isname))).grid(row=1,column=0, columnspan=11)
            mb.showinfo("Bus Route Details Entry", message="Bus Route Record Added")
            conn.commit()
        except sqlite3.OperationalError:
            mb.showerror("Invalid Input", message="Unacceptable Input.")
        except sqlite3.IntegrityError:
            mb.showerror("DB insertion Error", message="Bus Route Record Already Exists")

#edit Bus Details funtion
def del_rd():
    # try:
        irid=rid.get()
        isid=sid.get()
        isname=sname.get()
        try:
            cur.execute("delete from ROUTE where ROUTEID={} and SID=P{} and SNAME='{}'".format(irid, isid, isname))
        except:
            cur.execute("delete from ROUTE where ROUTEID={}".format(irid))
        mb.showinfo("Bus Route Entry deleted", message="Bus Route Record updated Successfully")
        conn.commit()
  
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0)
root.update()
a=w-H.winfo_width()
H.destroy()
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0, padx=a//2)

Label(root, text="Add Bus Route Details", fg="green", font=("Arial Bold", 30)).grid(row=2, column=0, pady=30)

options=Frame(root)
Label(options, text="Route id", font=("Arial", 15)).grid(row=0, column=0, padx=5)
rid=Entry(options, width=5, font=("Arial", 15))
rid.grid(row=0, column=1, padx=5)
Label(options, text="Station Name", font=("Arial", 15)).grid(row=0, column=2, padx=5)
sname=Entry(options, width=25, font=("Arial", 15))
sname.grid(row=0, column=3, padx=5)
Label(options, text="Station Id", font=("Arial", 15)).grid(row=0, column=4, padx=5)
sid=Entry(options, font=("Arial", 15))
sid.grid(row=0, column=5, padx=5)
Label(options, font=("Arial", 15)).grid(row=0, column=6, padx=40)
add=Button(options, text="Add Route", bg="#97ffa0", font=("Arial", 15), command=add_rd).grid(row=0, column=7, padx=5)
delete=Button(options, text="Delete Route", bg="#97ffa0", fg="red", font=("Arial", 15), command=del_rd).grid(row=0, column=8, padx=5)
hm=PhotoImage(file="./assets/home.png")
home=Button(options, image=hm, command=home).grid(row=1, column=6, pady=30)
options.grid(row=3, column=0, pady=50)

root.mainloop()
conn.commit()
conn.close()

