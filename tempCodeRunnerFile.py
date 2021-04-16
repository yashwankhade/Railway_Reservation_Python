from tkinter import *
import tkinter as tk
from tkinter import ttk


def create_button_frame(container):
    frame = Frame(container)
    frame.columnconfigure(0, weight=1)

    Button(frame, text='Show Passengers').grid(column=0, row=0)
    Button(frame, text='Show Trains').grid(column=0, row=1)
    Button(frame, text='Add Trains').grid(column=0, row=2)
    Button(frame, text='Cancel Trains').grid(column=0, row=3)
    Button(frame, text='Bas yu hi').grid(column=0, row=4)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame

def create_root():

    root = Tk()
    root.title('Admin')
    root.geometry('400x200')
    root.resizable(True, True)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=4)

    button_frame = create_button_frame(root)
    button_frame.grid(row=0, column=0)
    root.mainloop()

create_root()
