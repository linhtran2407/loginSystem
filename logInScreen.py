# import all (*) and message box (to send message boxes to users later) from tkinter lib
from tkinter import *
from tkinter import messagebox
# import Regular Expression and OS (used for moving to the next screen from the current screen):
import re
import os

# Create the main window for the registration form (I name the object to be window), using tkinter (TK) class:
window = Tk()
# Set title, size, and background color for the form:
window.title("Welcome to the Log-In Screen") # title shown at the top of the form
window.geometry('500x500') # size of the form: 500x500
window.configure(background="light pink")

# Create input fields: full name and password
v_fullName = StringVar()
v_passWord = StringVar()

"""HEADING"""
lb_heading = Label(window, text="Log In", width=30, font=('bold', 30), bg='light pink')
lb_heading.place(x=-40, y=53) # set the position of the heading (RECHECK)

"""FULL NAME"""
lb_fullName = Label(window, text="Full Name:", width=15, font=('normal', 15), bg='salmon2')
lb_fullName.place(x=80, y=150)
# In order to create a box for the users to type in input, we need Entry:
entry_fullName = Entry(window, textvariable=v_fullName)
entry_fullName.place(x=240, y=150)

"""PASSWORD"""
lb_passWord = Label(window, text="Password:", width=15, font=('normal', 15), bg='salmon2')
lb_passWord.place(x=80, y=200)
entry_passWord = Entry(window, textvariable=v_passWord, show='*')
entry_passWord.place(x=240, y=200)

"""Function to validate users' credentials:"""
def validateUser (userFullname, userPwd):
    if userFullname == "admin" and userPwd == "admin":
        return True
    else:
        return False

"""Function to validate all fieds:"""
def validateAllFields ():
    if v_fullName.get() == "" or v_passWord.get() == "":
        messagebox.showinfo('opps!', "Please enter full name andp password.")
    else:
        isValidUser = validateUser(v_fullName, v_passWord)
        if isValidUser:
            messagebox.showinfo('Congrats!', "Login Success")
        else:
            messagebox.showinfo('oops!', 'Invalid Information')

"""Function to clear all fields:"""
def clearAllFields():
    v_fullName.set("")
    v_passWord.set("")

"""These commented-out lines are to call for the Registration form in case the users have not created an account.
They would only be used after adding a Python file that runs Registration form.
Go to my github "Registration form" project to see how they would be conducted."""
# """Function to open a new screen:"""
# def callNewScreen():
#     window.destroy()
#     os.system('python registrationForm.py')

"""Create 3 buttons at the bottom of the form:"""
btn_login = Button(window, text='Login', command=validateAllFields, bg='deep pink', fg='black', font=('bold', 15)).\
    place(x=120, y=280)
btn_clear = Button(window, text='Clear All', command=clearAllFields, bg='deep pink', fg='black', font=('bold', 15)).\
    place(x=200, y=280)
# btn_register = Button(window, text='Register', command=callNewScreen, bg='deep pink', fg='black', font=('bold', 15)).\
#     place(x=300, y=280)

window.mainloop() # call the function endlessly so that the window remains open until the user closes it