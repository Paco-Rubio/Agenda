from win10toast_click import ToastNotifier
from datetime import date
from datetime import datetime
import datetime
import re
from os.path import exists
import playsound

if not exists(r"C:\Jorge\Programming\Agenda\birthday.txt"):
    birthdayfile = open("birthday.txt", "w+")
    birthdayfile.write("# This file is used to store birthdays the user wants to be reminded of")
    birthdayfile.close

if not exists(r"C:\Jorge\Programming\Agenda\config.txt"):

    configfile = open("config.txt", "w+")
    configfile.write("gmail")
    configfile.write("\n")
    configfile.write("# Choose your email provider: 'gmail', 'outlook' ")
    configfile.write("\n")
    configfile.write("yes")
    configfile.write("\n")
    configfile.write("# Reminder of previously selected birthdays?: 'yes' / 'no' ")
    configfile.write("\n")
    configfile.write("windows")
    configfile.write("\n")
    configfile.write("# Chooose your calendar provider: 'windows', 'google'")  
    configfile.write("\n")
    configfile.write("mystudylife")
    configfile.write("\n")
    configfile.write("# Choose your management app:'mystudylife', 'todoist'")
    configfile.write("\n")
    configfile.write("english")
    configfile.write("\n")
    configfile.write("# Choose your preferred language: 'english', 'spanish'")
    configfile.close

def setting():

        with open("C:\Jorge\Programming\Agenda\config.txt") as settingsfile:
            settings = list(settingsfile)[0::2]
        settings = ([s.replace('\n', '') for s in settings])
        return settings

toaster = ToastNotifier()

def action():
    print ("Ok, no more reminders")

rawdoit = setting()
doit = str(rawdoit[1])

languageconfig = setting()
langconfig = str(languageconfig[4])

if doit in ("yes"):
    birthdayfile = "C:\Jorge\Programming\Agenda\birthday.txt"
    rawtoday = date.today()
    strtoday = str(rawtoday)
    today = re.sub(r'.', '', strtoday, count = 5)

    rntoday7 = datetime.date.today()
    ntoday7 = rntoday7 + datetime.timedelta(days=7)
    today7 = re.sub(r'.', '', str(ntoday7), count = 5)
    today7 = str(today7)
        
    rntoday6 = datetime.date.today()
    ntoday6 = rntoday6 + datetime.timedelta(days=6)
    today6 = re.sub(r'.', '', str(ntoday6), count = 5)
    today6 = str(today6)
        
    rntoday5 = datetime.date.today()
    ntoday5 = rntoday5 + datetime.timedelta(days=5)
    today5 = re.sub(r'.', '', str(ntoday5), count = 5)
    today5 = str(today5)
        
    rntoday4 = datetime.date.today()
    ntoday4 = rntoday4 + datetime.timedelta(days=4)
    today4 = re.sub(r'.', '', str(ntoday4), count = 5)
    today4 = str(today4)
        
    rntoday3 = datetime.date.today()
    ntoday3 = rntoday3 + datetime.timedelta(days=3)
    today3 = re.sub(r'.', '', str(ntoday3), count = 5)
    today3 = str(today3)
        
    rntoday2 = datetime.date.today()
    ntoday2 = rntoday2 + datetime.timedelta(days=2)
    today2 = re.sub(r'.', '', str(ntoday2), count = 5)
    today2 = str(today2)

    rntoday1 = datetime.date.today()
    ntoday1 = rntoday1 + datetime.timedelta(days=1)
    today1 = re.sub(r'.', '', str(ntoday1), count = 5)
    today1 = str(today1)
    
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")

    for line in fileName:
        if today in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Hoy es el cumpleaños de" + person.title(), " ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action)
            else:
                toaster.show_toast(person.title() + "'s birthday today!!", " ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )

    fileName.close()
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")

    for line in fileName:
        if today7 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Se acerca el cumpleaños de" + person.title(), " Quedan 7 días", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            else:
                toaster.show_toast(person.title() + "'s birthday in a week!!", " 7 days left ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
                
    fileName.close()
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")

    for line in fileName:
        if today6 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Se acerca el cumpleaños de" + person.title(), " Quedan 6 días", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            else:
                toaster.show_toast(person.title() + "'s birthday is near!!", " 6 days left ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            
    fileName.close()
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")

    for line in fileName:
        if today5 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Se acerca el cumpleaños de" + person.title(), " Quedan 5 días", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            else:
                toaster.show_toast(person.title() + "'s birthday is near!!", " 5 days left ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
             
    fileName.close()
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")
            
    for line in fileName:
        if today4 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Se acerca el cumpleaños de" + person.title(), " Quedan 4 días", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            else:
                toaster.show_toast(person.title() + "'s birthday is near!!", " 4 days left ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            
    fileName.close()
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")
            
    for line in fileName:
        if today3 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Se acerca el cumpleaños de" + person.title(), " Quedan 3 días", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            else:
                toaster.show_toast(person.title() + "'s birthday is near!!", " 3 days left ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            
    fileName.close()
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")
            
    for line in fileName:
        if today2 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Se acerca el cumpleaños de" + person.title(), " Quedan 2 días", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            else:
                toaster.show_toast(person.title() + "'s birthday is near!!", " 2 days left ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            
    fileName.close()
    fileName = open(r"C:\Jorge\Programming\Agenda\birthday.txt", "r")
            
    for line in fileName:
        if today1 in line:
            eachline = line.split(" | ")
            person = eachline[0]
            if langconfig == "spanish":
                toaster.show_toast("Se acerca el cumpleaños de" + person.title(), " Queda 1 día", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
            else:
                toaster.show_toast(person.title() + "'s birthday tomorrow!!", " 1 day left ", icon_path="Birthday.ico", duration=6, threaded = True, callback_on_click= action )
    
    fileName.close()