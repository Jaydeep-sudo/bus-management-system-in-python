import sqlite3
conn=sqlite3.Connection("bus_booking.db")
cur=conn.cursor()
from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))


def home():
    root.destroy()
    import BE4


def add_run():
        ibid=bid.get()
        irdate=rdate.get()
        iseat=seat.get()
        try:
            cur.execute("insert into RUNS values({}, '{}', {})".format(ibid, irdate, iseat))
            Label(options, text="".format(ibid+" "+irdate+" "+iseat)).grid(row=1,column=0, columnspan=11)
            mb.showinfo("Bus Running Details Entry", message="Bus Running Record Added")
            conn.commit()
        except sqlite3.OperationalError:
            mb.showerror("Invalid Input", message="Unacceptable Input.")
        except sqlite3.IntegrityError:
            mb.showerror("DB insertion Error", message="Bus Record Already Exists")


def edit_run():
        ibid=bid.get()
        irdate=rdate.get()
        iseat=seat.get()
        try:
            cur.execute("update RUNS SEAT_AVAIL={2} where BUSID={0} AND DATE={1}".format(ibid, irdate, iseat))
            Label(options, text="".format(ibid+" "+irdate+" "+iseat)).grid(row=1,column=0, columnspan=11)
            mb.showinfo("Bus Running Entry Updated", message="Bus Running Record updated Successfully")
            conn.commit()
        except sqlite3.OperationalError:
            mb.showerror("Invalid Input", message="Unacceptable Input.")
        except sqlite3.IntegrityError:
            mb.showerror("Record Not Found", message="Bus Running Record does not Exists")


bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0)
root.update()
a=w-H.winfo_width()
H.destroy()
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0, padx=a//2)


Label(root, text="Add Bus Running Details", fg="green", font=("Arial Bold", 30)).grid(row=2, column=0, pady=30)

options=Frame(root)
Label(options, text="Bus id", font=("Arial", 15)).grid(row=0, column=0, padx=5)
bid=Entry(options, width=5, font=("Arial", 15))
bid.grid(row=0, column=1, padx=5)
Label(options, text="Date", font=("Arial", 15)).grid(row=0, column=2, padx=5)
rdate=Entry(options, width=25, font=("Arial", 15))
rdate.grid(row=0, column=3, padx=5)
Label(options, text="Seat Available", font=("Arial", 15)).grid(row=0, column=4, padx=5)
seat=Entry(options, font=("Arial", 15))
seat.grid(row=0, column=5, padx=5)
addr=Button(options, text="Add Run", bg="#97ffa0", font=("Arial", 15), command=add_run).grid(row=0, column=6, padx=5)
editr=Button(options, text="Edit Run", bg="#97ffa0", font=("Arial", 15), command=edit_run).grid(row=0, column=7, padx=5)
hm=PhotoImage(file="./assets/home.png")
home=Button(options, image=hm, command=home).grid(row=1, column=6, pady=30)
options.grid(row=3, column=0, pady=50)

root.mainloop()
conn.commit()
conn.close()
