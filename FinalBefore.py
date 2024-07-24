"""
Author: Ashley Torres
Date Written: 07/01/2024
Assignment: Final Project
Short Desc: To Do List
"""
import tkinter 
from tkinter import messagebox

#Create functions


def add_task():
    pass

def alph_task():
    pass

def mark_done():
    pass

def num_task():
    pass

def delete_all():
    pass

def del_one():
    pass

def exit_all():
    pass

#Create root window
root = tkinter.Tk()

#Change root window background color
root.configure(bg="white")


#Change the title
root.title("My super to do list")

#Change the window size
root.geometry("300x300")

#Creat an empty list
tasks = []

#Creating the functions
lbl_title = tkinter.Label(root, text="To-Do-List", bg="white")
lbl_title.pack()

lbl_display = tkinter.Label(root, text="My Favorites", bg="white")
lbl_display.pack

txt_input = tkinter.Entry(root, width=15 )
txt_input.pack()

btn_add_task = tkinter.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_alph_task = tkinter.Button(root, text="List in Alphabetical order", fg="pink", bg="white", command=alph_task)
btn_alph_task.pack()
btn_mark_done = tkinter.Button(root, text="Mark as Done", fg="blue", bg="white", command=mark_done)
btn_mark_done.pack()

btn_num_task = tkinter.Button(root, text="Total number of tasks", fg="purple", bg="white", command=num_task)
btn_num_task.pack()

btn_delete_all  = tkinter.Button(root, text="DELETE ALL", fg="red", bg="white", command=delete_all)
btn_delete_all.pack()

btn_del_one  = tkinter.Button(root, text="Delete One", fg="red", bg="white", command=del_one)
btn_del_one.pack()

btn_exit_all  = tkinter.Button(root, text="Exit List", fg="green", bg="white", command=exit_all)
btn_exit_all.pack()

lb_tasks = tkinter.Listbox(root)
lb_tasks.pack()


#Start the main loop of events
root.mainloop()
