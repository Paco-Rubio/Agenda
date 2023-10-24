import pystray
from pystray import MenuItem as item
from pystray import Menu as menu
from PIL import Image
import os

# import webbrowser

def on_click(icon, item):
    if str(item) == "Agenda":
        os.startfile(r"C:\Jorge\Programming\Agenda\Agenda.lnk")
    elif str(item) == "Birthdays":
        os.startfile(r"C:\Jorge\Programming\Agenda\BirthdaysCheck.pyw")
    elif str(item) == "Password Manager":
        os.startfile(r"C:\Jorge\Programming\Password Manager\Password_Manager.py")

image = Image.open(r"C:\Users\jlpen\Downloads\Iconos\Home (Blue).ico")

menu = (
    item('Agenda', on_click),
    item('Birthdays', on_click),
    item('Password Manager', on_click),
    menu.SEPARATOR,
    item('Exit', lambda icon, item: icon.stop()),
)

icon = pystray.Icon("name", image, "Agenda", menu)

icon.run()
