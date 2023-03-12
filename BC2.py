


from tkinter import *
root=Tk()

def seat_booking():
    root.destroy()
    import CA_Enter_Journey_Details


def check_booked():
    root.destroy()
    import DA_Check_Booked_seat


def add_bd():
    root.destroy()
    import EA_Add_Bus_Details

#Main Heading
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root,image=bus).grid(row=0, column=0, columnspan=10, padx=w//3)
Label(root, text="Online Bus Booking System", bg="Light Blue", fg="Red", font=("Arial Bold", 40)).grid(row=1, column=0, columnspan=10, pady=10, padx=w//3)
B=Button(root,text="Seat Booking", bg="PaleGreen1" , font=("Arial Bold", 25), command=seat_booking).grid(row=3,column=3, padx=30, pady=100)
B=Button(root,text="Check booked Seat", bg="Green2", font=("Arial Bold", 25), command=check_booked).grid(row=3,column=4, padx=30, pady=100)
B=Button(root,text="Add Bus Details", bg="Green", font=("Arial Bold", 25), command=add_bd).grid(row=3,column=5, padx=30, pady=100)
Label(root,text="For Admin Only", fg="Red", font=("Arial Bold", 18)).grid(row=4,column=5)
root.mainloop()

