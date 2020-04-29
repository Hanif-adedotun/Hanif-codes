from tkinter import * 
from tkinter import filedialog
import base64
import tkinter
#This app was made by Hanif Adedotun
#copyright 2018
#contact me at hanif.adedotun@gmail.com, 09096281736

 
window = Tk()
window.geometry('-500+100')
window.title("Water App")
window.config(bg="light blue")


def profile():
     prof = Toplevel(window, bg="Light blue")
     prof.title("Profile")
     prof.geometry('300x450')
     prof.resizable(width=False, height=False)
     #icon = base64.encodestring(open('Back.gif').read())
     #iconImage = PhotoImage(master=prof, data=icon)
     #image=iconImage
     Button(prof, command=prof.withdraw, text="Back").grid(row=0, column=0, sticky='nw')
     Label(prof, text="Welcome", font=("Arial", 15, "bold"), bg="light blue", fg="white", anchor='center').grid(column=4, row=2, pady=17)
     Button(prof, command=profpic, anchor='center', text='change profile picture').grid(column=4, row=3, pady=20)
     
     
def profpic():
     file = filedialog.askopenfilename(filetypes = (("Picture files","*.jpg"),("Picturefiles","*.png"),("all files","*.*")))


def chart():
     char = Toplevel(window, bg="Light blue")
     char.title("Chart")
     char.geometry('300x450')
     char.resizable(width=False, height=False)
     Button(char, text="Back", command=char.withdraw).grid(column=0, row=0, sticky='nw')
     
#ph value
lbl = Label(window, text="PH Value(ph)", font=("Arial, 10"), bg="light blue", fg="white")
lbl.grid(column=0, row=0)
txt = Entry(window, width=19)
txt.grid(column=0, row=2, pady=10)
txt.margin_left = 0
lbl.margin_left = 0


#Turpidity
lbl2 = Label(window, text="Turbidity Value(utd)", font=("Arial, 10"), bg="light blue", fg="white")
lbl2.grid(column=0, row=7)
txt = Entry(window, width=19)
txt.grid(column=0, row=9, pady=10)
txt.margin_left = 0
lbl2.margin_left = 0


#conductivity
lbl3 = Label(window, text="Conductivity Value", font=("Arial, 10"), bg="light blue", fg="white")
lbl3.grid(column=0, row=11)
txt = Entry(window, width=19)
txt.grid(column=0, row=13, pady=10)
txt.margin_left = 0
lbl3.margin_left = 0


#Toxic metal
lbl4 = Label(window, text="Toxic metal", font=("Arial, 10"), bg="light blue", fg="white")
lbl4.grid(column=0, row=16)
txt = Entry(window, width=19)
txt.grid(column=0, row=18, pady=10)
txt.margin_left = 0
lbl4.margin_left = 0

#Water Hardness
lbl4 = Label(window, text="Water Hardness(mg/l)", font=("Arial, 10"), bg="light blue", fg="white")
lbl4.grid(column=0, row=19)
txt = Entry(window, width=19)
txt.grid(column=0, row=20, pady=10)
txt.margin_left = 0
lbl4.margin_left = 0

#Fecal caliform
lbl4 = Label(window, text="Fecal caliform(%)", font=("Arial, 10"), bg="light blue", fg="white")
lbl4.grid(column=0, row=21)
txt = Entry(window, width=19)
txt.grid(column=0, row=22, pady=10)
txt.margin_left = 0
lbl4.margin_left = 0

#Submit button
btn = Button(window, text="Submit", bd = 2, anchor=CENTER, bg="Light blue")
btn.grid(column=1, row=25, pady=15)

#def prof():


#Profile screen
btn1 = Button(window, bg = "Light blue", bd = 1, text = "Profile", font = ("Arial, 10"), command=profile) 
btn1.grid(column=2, row = 26, padx=40)

#Chart screen
btn1 = Button(window, bg = "Light blue", bd = 1, text = "Chart", font = ("Arial, 10"), command=chart) 
btn1.grid(column=0, row = 26, padx=0)

#Home screen
btn1 = Button(window, bg = "Light blue", bd = 1, text = "Home", font = ("Arial, 10")) 
btn1.grid(column=1, row = 26, padx=0)

#file = filedialog.askopenfilename(filetypes = (("Picture files","*.jpg"),("Picturefiles","*.png"),("all files","*.*")))



window.resizable(width=False, height=False)
window.mainloop()
