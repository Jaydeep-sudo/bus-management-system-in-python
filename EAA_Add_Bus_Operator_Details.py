

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
    import BE1



def add_bop():
    iopid=opid.get()
    iname=name.get()
    iaddress=address.get()
    iphn=phn.get()
    imail=mail.get()
    try:
        if str(iopid)=="":
            cur.execute("insert into OPERATOR(ONAME, ADDRESS, EMAIL, PHONE) values('{}','{}','{}',{})".format(iname,iaddress,imail,iphn))
        else:
            cur.execute("insert into OPERATOR values({},'{}','{}','{}',{})".format(iopid,iname,iaddress,imail,iphn))
        Label(options, text="{}".format(str(iopid)+" "+str(iname)+" "+str(iaddress)+" "+str(imail)+" "+str(iphn))).grid(row=1,column=0, columnspan=11)
        mb.showinfo("Operator Entry", message="Operator Record Added")
        conn.commit()
    except sqlite3.OperationalError:
        mb.showerror("Invalid Input", message="Unacceptable Input.")
    except sqlite3.IntegrityError:
        mb.showerror("DB insertion Error", message="Operator Record Already Exists")

def edit_bop():
        iopid=opid.get()
        iname=name.get()
        iaddress=address.get()
        iphn=phn.get()
        imail=mail.get()
        try:
            cur.execute("update OPERATOR set ONAME='{1}',ADDRESS='{2}',EMAIL='{3}',PHONE={4} where OPID={0}".format(iopid,iname,iaddress,imail,iphn))
            Label(options, text="{}".format(str(iopid)+" "+str(iname)+" "+str(iaddress)+" "+str(imail)+" "+str(iphn))).grid(row=1,column=0, columnspan=11)
            mb.showinfo("Operator Entry Updated", message="Operator Record updated Successfully")
            conn.commit()
        except sqlite3.OperationalError:
            mb.showerror("Invalid Input", message="Unacceptable Input.")
        except sqlite3.IntegrityError:
            mb.showerror("Record Not Found", message="Operator Record does not Exists")


bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0)
root.update()
a=w-H.winfo_width()
H.destroy()
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0, padx=a//2)


Label(root, text="Add Bus Operator Details", fg="green", font=("Arial Bold", 30)).grid(row=2, column=0, pady=30)

options=Frame(root)
Label(options, text="Operator id", font=("Arial", 15)).grid(row=0, column=0, padx=5)
opid=Entry(options, width=5)
opid.grid(row=0, column=1, padx=5)
Label(options, text="Name", font=("Arial", 15)).grid(row=0, column=2, padx=5)
name=Entry(options, width=25)
name.grid(row=0, column=3, padx=5)
Label(options, text="Address", font=("Arial", 15)).grid(row=0, column=4, padx=5)
address=Entry(options)
address.grid(row=0, column=5, padx=5)
Label(options, text="Phone", font=("Arial", 15)).grid(row=0, column=6, padx=5)
phn=Entry(options)
phn.grid(row=0, column=7, padx=5)
Label(options, text="Email", font=("Arial", 15)).grid(row=0, column=8, padx=5)
mail=Entry(options)
mail.grid(row=0, column=9, padx=5)
add=Button(options, text="Add", bg="springgreen3", font=("Arial", 15), command=add_bop).grid(row=0, column=10, padx=5)
edit=Button(options, text="Edit", bg="springgreen3", font=("Arial", 15), command=edit_bop).grid(row=0, column=11, padx=5)
hm=PhotoImage(file="./assets/home.png")
home=Button(options, image=hm, command=home).grid(row=1, column=8, pady=30)
options.grid(row=3, column=0, pady=50)

root.mainloop()
conn.commit()
conn.close()

