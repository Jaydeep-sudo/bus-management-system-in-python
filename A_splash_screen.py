
from tkinter import *
root=Tk()

#Connection Function
def B(temp=1):
    root.destroy()
    import B

#Main Heading
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root,image=bus).pack()
Label(root, text="Online Bus Booking System", bg="Light Blue", fg="Red", font=("Arial Bold", 40)).pack()
Label(root).pack(pady=30)
Label(root, text="Name: Jaydeep Bohra", fg="blue", font=("Bold", 20)).pack()
Label(root, text="ER: 211B428",fg="blue", font=("Bold", 20)).pack(pady=20)
Label(root, text="Mobile: 8449698584", fg="blue", font=("Bold", 20)).pack()
Label(root).pack(pady=30)
Label(root, text="Submitted To: Dr. Mahesh Kumar", bg="Light Blue", fg="Red", font=("Arial", 25)).pack()
Label(root, text="Project Based Learing", fg="Red", font=("Arial", 20)).pack()
root.bind("<KeyPress>", B)
root.mainloop()

