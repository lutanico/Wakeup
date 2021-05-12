
import win10toast
toaster =  win10toast.ToastNotifier()
import winreg as reg1
import os

def AddToRegistry():
    # in python __file__ is denoeted as the instant of
    # file path where it was run or executed
    # so if it was executed from desktop,
    # then __file__ will be
    # c:\users\current_user\desktop
    pth1 = os.path.dirname(os.path.realpath(__file__))
    # Python file name with extension
    s_name1 = "mYscript.py"
    # The file name is joined to end of path address
    address1 = os.join(pth1, s_name1)
    # key we want to modify or change is HKEY_CURRENT_USER
    # key value is Software\Microsoft\Windows\CurrentVersion\Run
    key1 = reg1.HKEY_CURRENT_USER
    key_value1 = "Software\Microsoft\Windows\CurrentVersion\Run"
    # open the key to make modifications or changes to
    open = reg1.OpenKey(key1, key_value1, 0, reg1.KEY_ALL_ACCESS)
    # change or modifiy the opened key
    reg1.SetValueEx(open, "any_name", 0, reg1.REG_SZ, address1)
    # now close the opened key
    reg1.CloseKey(open)
    # Driver Code
    pass


AddToRegistry()
import schedule
import time
txt1=("Time for relaxing, Life is Precious")
txt2 =("Tme for Programming, You need step up your  Game")
txt3= ("Time for Graphics, You need much prgress ")
txt4 =("Goodmorning Luttampanga, remember to avoid    silly mistakes ")
txt5 =("Good Afternoon Luttampanga, dont forget lucnh mukwano")
txt6 =("Good Evening Luttampanga, Hope you  worked upon your day Goals")
txt7 =("Good Night Luttampanga Rememeber life is precious")
def graphic():
    toaster.show_toast('WAKEUP', txt1, icon_path='D:\wakeup.ico',duration=10 )
def program():
    toaster.show_toast('WAKEUP',txt2,icon_path='D:\wakeup.ico',duration=10 )
def resting():
    toaster.show_toast('WAKEUP',txt1,icon_path='D:\wakeup.ico',duration=10)
def lunch():
    toaster.show_toast('WAKEUP',txt5, icon_path='D:\wakeup.ico',duration=10)
def morn():
    toaster.show_toast("WAKEUP",txt4, icon_path='D:\wakeup.ico', duration=10)
def goodnite():
    toaster.show_toast("WAKEUP",txt7, icon_path='D:\wakeup.ico',duration=10)
def evenning():
    toaster.show_toast("WAKEUP",txt6, icon_path='D:\wakeup.ico', duration=10)

def greet():
    toaster.show_toast("WAKEUP","HEllo , thank you am now running", icon_path='D:\wakeup.ico', duration=10)
#Time
schedule.every(30).minutes.do(resting)
schedule.every().day.at("01:00").do(lunch)
schedule.every().day.at("13:00").do(lunch)
schedule.every().day.at("06:00").do(evenning)
schedule.every().day.at("19:00").do(evenning)
schedule.every().day.at("01:30").do(goodnite)
schedule.every().day.at("13:30").do(goodnite)
schedule.every().day.at("08:30").do(morn)
schedule.every().day.at("20:30").do(morn)
schedule.every().hour.do(program)
schedule.every(2).hours.do(graphic)

while True:
    schedule.run_pending()
    time.sleep(1)