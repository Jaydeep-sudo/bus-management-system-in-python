import sqlite3
conn=sqlite3.Connection("bus_booking.db")
cur=conn.cursor()
from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))

# Connection Functions
def home():
    root.destroy()
    import BD

#Function to check the ticket
def chk_tkt():
    phn_no=phn.get()
    try:
        data=cur.execute("SELECT * FROM BOOKING_HISTORY WHERE REF_NO={}".format(phn_no))
        userdata=data.fetchall()
    except:
        mb.showerror("Invalid Input", message="Unacceptable Input.")
    if len(userdata)!=0:
        for i in range(len(userdata)):
            data=cur.execute("SELECT * FROM BUS WHERE BUSID={}".format(userdata[i][3]))
            busdata=data.fetchall()
            data=cur.execute("SELECT ONAME FROM OPERATOR WHERE OPID={}".format(busdata[0][4]))
            odata=data.fetchall()
            ticket=Frame(root, borderwidth=5, relief="ridge")
            Label(ticket, text="Passengers: {}".format(userdata[i][1]), font=("Arial Bold", 15)).grid(row=0,column=0)
            Label(ticket, text="No of Seats: {}".format(userdata[i][4]), font=("Arial Bold", 15)).grid(row=1,column=0)
            Label(ticket, text="Age: {}".format(userdata[i][7]), font=("Arial Bold", 15)).grid(row=2,column=0)
            Label(ticket, text="Phone: {}".format(userdata[i][0]), font=("Arial Bold", 15)).grid(row=3,column=0)
            Label(ticket, text="Travel On: {}".format(userdata[i][6]), font=("Arial Bold", 15)).grid(row=4,column=0)
            Label(ticket, text="Gender: {}".format(userdata[i][2]), font=("Arial Bold", 15)).grid(row=5,column=0)
            # Label(ticket, text="Booking Ref: 9", font=("Arial Bold", 15)).grid(row=0,column=1)
            Label(ticket, text="Fare Rs: {} *".format(busdata[0][3]*userdata[i][4]), font=("Arial Bold", 15)).grid(row=1,column=1)
            Label(ticket, text="Bus Details: {}".format(odata[0][0]), font=("Arial Bold", 15)).grid(row=2,column=1)
            Label(ticket, text="Booked On: {}".format(userdata[i][5]), font=("Arial Bold", 15)).grid(row=3,column=1)
            Label(ticket, text="Boarding Point: {}".format(userdata[i][8]), font=("Arial Bold", 15)).grid(row=4,column=1)
            Label(ticket, text="*Total amount Rs {}/- to be paid at the time of Boarding the Bus".format(busdata[0][3]*userdata[i][4]), font=10).grid(row=6,column=0, columnspan=2)
            ticket.grid(row=5,column=0, pady=10)
            
        flag=mb.askyesno("No Booking Record", message="Do you want to book seat now?")
        if flag:
            root.destroy()
            import CA_Enter_Journey_Details

#Basic Headings
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
h=Label(root, text="Online Bus Booking System", bg="Lightblue", fg="red", font=("Arial Bold", 40))
h.grid(row=0, column=0)
root.update()
a=w-h.winfo_width()
h.destroy()
h=Label(root, text="Online Bus Booking System", bg="Lightblue", fg="red", font=("Arial Bold", 40))
h.grid(row=1, column=0, padx=a//2)

#options
Label(root, text="Check your Booking", fg="green4", bg="springgreen2", font=("Arial Bold", 20)).grid(row=2, column=0, pady=40)
phone=Frame(root)
Label(phone, text="Enter Your Mobile No:", font=("Arial Bold", 15)).grid(row=0, column=0, padx=10)
phn=Entry(phone, font=("Arial Bold", 15))
phn.grid(row=0, column=1, padx=10)
check=Button(phone, text="Check Booking", font=("Arial Bold", 20), command=chk_tkt).grid(row=0, column=3, padx=10)
phone.grid(row=3,column=0)
hm=PhotoImage(file="./assets/home.png")
home=Button(root, image=hm, command=home).grid(row=4, column=0, padx=5)

root.mainloop()

conn.commit()
conn.close()

