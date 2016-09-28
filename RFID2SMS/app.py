from twilioSMS import SMStwilio
from leeSerial import leeSerial
from time import sleep
import webbrowser

for a in leeSerial():
    print(a)
    print(type(a))
    webbrowser.open('https://www.youtube.com/watch?v=hwsv5q0MKBA')
    print('Si te reconosco')
    SMStwilio(a)
    sleep(.5)


