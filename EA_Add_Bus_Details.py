from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))


def new_op():
    root.destroy()
    import EAA_Add_Bus_Operator_Details


def new_bus():
    root.destroy()
    import EAB_Add_Bus_Details


def new_route():
    root.destroy()
    import EAC_Add_Bus_Route


def new_run():
    root.destroy()
    import EAD_Add_Bus_Running


bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root, image=bus).grid(row=0, column=0)
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0)
root.update()
a=w-H.winfo_width()
H.destroy()
H=Label(root, text="Online Bus Booking System", fg="red", bg="lightblue", font=("Arial Bold", 40))
H.grid(row=1, column=0, padx=a//2)

Label(root, text="Add New Details to Database", fg="green", font=("Arial Bold", 30)).grid(row=2, column=0, pady=50)

options=Frame(root)
nop=Button(options, text="New Operator", font=("Arial", 20), bg="#96fe92", command=new_op).grid(row=0, column=0, padx=30)
nbus=Button(options, text="New Bus", font=("Arial", 20), bg="#f37754", command=new_bus).grid(row=0, column=1, padx=30)
nroute=Button(options, text="New Route", font=("Arial", 20), bg="#517990", command=new_route).grid(row=0, column=2, padx=30)
nrun=Button(options, text="New Run", font=("Arial", 20), bg="#b78b90", command=new_run).grid(row=0, column=3, padx=30)
options.grid(row=3, column=0)

root.mainloop()
