import sched
import time
import schedule
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("Test Notifier")


text1 =("Time for relaxing, Life is Precious")
txt2 =("Tme for Programming, You need step up your  Game")
txt3= ("Time for Graphics, You need much prgress ")
txt4 =("Goodmorning Luttampanga, remember to avoid    silly mistakes ")
txt5 =("Good Afternoon Luttampanga, dont forget lucnh mukwano")
txt6 =("Good Evening Luttampanga, Hope you  worked upon your day Goals")
txt7 =("Good Night Luttampanga Rememeber life is precious")
def graphic():
    notification = Notify.Notification.new("WAKE UP", text1, "/home/lutta/Pictures/wakeup.png",).show()
    #notification.set_urgency(2)
#Time
schedule.every(20).minutes.do(graphic)
while True:
    schedule.run_pending()
    time.sleep(1)


#notification.update("WAKEUP", "Hope you takecare of yourself,Lutta", "/home/lutta/Pictures/wakeup.png")
#notification.show()

