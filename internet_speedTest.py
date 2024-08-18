from tkinter import *
import speedtest

def check():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + "Mbps"
    up = str(round(sp.upload()/(10**6),3)) + "Mbps"
    lb_down.config(text=down)
    lb_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry('500x600')
sp.config(bg = 'Black')

lb = Label(sp, text="Internet Speed Test", font=('Times New Roman', 30, 'bold'), bg='black', fg='white')
lb.place(x=60, y=40, height=50, width=380)

lb = Label(sp, text="Downloading Speed", font=('Times New Roman', 30, 'bold'))
lb.place(x=60, y=130, height=50, width=380)

lb_down = Label(sp, text="00", font=('Times New Roman', 30, 'bold'))
lb_down.place(x=60, y=200, height=50, width=380)

lb = Label(sp, text="Upload Speed", font=('Times New Roman', 30, 'bold'))
lb.place(x=60, y=290, height=50, width=380)

lb_up = Label(sp, text="00", font=('Times New Roman', 30, 'bold'))
lb_up.place(x=60, y=360, height=50, width=380)

button = Button(sp, text='Check Speed',font=('Times New Roman', 30, 'bold'), relief=RAISED, command=check)
button.place(x=60, y=460, height=50, width=380)


sp.mainloop()