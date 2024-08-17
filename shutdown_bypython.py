from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system('shutdown /r /t 20')

def sleep():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")
st = Tk()

st.title("Shutdown! App")
st.geometry('500x500')
st.config(bg='black')

restart_button = Button(st, text='Restart', font=('Times New Roman', 20,'bold'), relief=RAISED, cursor='plus', command=restart)
restart_button.place(x=150, y=60, height=50, width=200)

restartwithtime_button = Button(st, text='Restart with time', font=('Times New Roman', 18,'bold'), relief=RAISED, cursor='plus', command=restart_time)
restartwithtime_button.place(x=150, y=170, height=50, width=200)

sleep_button = Button(st, text='Sleep', font=('Times New Roman', 20,'bold'), relief=RAISED, cursor='plus', command=sleep)
sleep_button.place(x=150, y=270, height=50, width=200)

Shutdown_button = Button(st, text='Shutdown', font=('Times New Roman', 20,'bold'), relief=RAISED, cursor='plus', command=shutdown)
Shutdown_button.place(x=150, y=370, height=50, width=200)
st.mainloop()