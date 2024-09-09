from tkinter import *

# Create the main window
root = Tk()
root.geometry("500x300")

# Function to handle form submission
def getvals():
    print("Accepted")

# Heading
Label(root, text="Python Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Field Names
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment Mood")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Variables for storing data
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmoodvalue = StringVar()
checkvalue = IntVar()

# Creating entry fields
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)

# Packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

# Creating Checkbox
checkbtn = Checkbutton(root, text="Remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

# Submit button
Button(root, text="Submit", command=getvals).grid(row=7, column=3)

# Start the GUI event loop
root.mainloop()
