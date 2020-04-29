from tkinter import *
from tkinter import ttk
import random

def main():
    window = Tk()
    window.geometry('300x100')
    window.resizable(width=False, height=False)
    window.title('GUI app')

    

    change_title_button = Button(window, text='Change the title above', command=change_title(window)).pack()
    quit_button = Button(window, text='Exit', command=window.destroy).pack()

    

def change_title(window):
    new_title = ''
    for i in range(7):
        new_title = new_title + chr(ord('A') + random.randrange(26))

    window.title(new_title)



main()
