import requests     # Used to grab information on the Northstar server browser from the internet (however it's not used in this file)
import sys     # I kinda forgor
import os     # I also may or may not have forgor
import time     # Literally only used for time.sleep() (aka used for error messages)
from func.playcnt import *     # Imports all functions from the files/scripts in the func folder
from func.servbrow import *     # Imports all functions from the files/scripts in the func folder
from func.servcnt import *     # Imports all functions from the files/scripts in the func folder
from func.playcnt import refresh as playref     # Imports "playref" function (refresh function) from playercount script
from func.servbrow import refresh as browref    # Imports "browref" function (refresh function) from serverbrowser script
from func.servcnt import refresh as servref    # Imports "servref" function (refresh function) from servercount script
from rich import print     # Adds fancy-shamncy text formatting

"""
Ion Server Browser
Made by DINOTICK
"""

def ErrorMSG(sleeptime):     # Idk I just felt like making this a function (I may remake this so it also handles the error output and not just the exiting and time.sleep)
  time.sleep(sleeptime)
  sys.exit()


def cls():     # Simple "clear" console function that checks if you're using windows or not and then wipes the screen
  try:
    os.system('cls' if os.name=='nt' else 'clear')
  except:
    print("[red]There was an error wiping the screen, are you on a supported operating system? (Linux, Windows)[/red]")
    ErrorMSG(2)
    

def RefreshAll():     # Lazy refresh function I made that basically just runs the refresh function in the scripts inside of the func folder
  try:
    playref()
  except:
    print("[red]There was an error obtaining player information.[/red]")
    ErrorMSG(2)
  try:
    browref()
  except:
    print("[red]There was an error obtaining serverbrowser information.[/red]")
    ErrorMSG(2)
  try:
    servref()
  except:
    print("[red]There was an error obtaining server-based information.[/red]")
    ErrorMSG(2)


def ShowCredits():     # Could use some cleaning up
  print("[orange1]Made by DINOTICK[/orange1]")
  print("[red]Youtube:  https://www.youtube.com/@dinotick[/red]")
  print("[bright_black]Github:  https://github.com/DINOTICK-Dev[/bright_black]")
  print("[dodger_blue2]Discord:  DINOTICK#6969[/dodger_blue2]")
  print("[bold orange1]Press enter to go back[/bold orange1]")
  input("")
  runtime()


def runtime():     # Main function, used to run everything and piece it all together
  cls()
  RefreshAll()
  print("[orange3]Welcome to Ion Mod Manager[/orange3]")
  print("[orange1]Please select an action: \n(1: Server Browser) (2: Coming Soon) (3: Credits)[/orange1]")
  inputinfo = input("")
  if inputinfo == "1":
    print("serverbrowser")
  if inputinfo == "2":
    print("Coming Soon (WIP)")
  if inputinfo == "3":
    cls()
    ShowCredits()

runtime()     # Starts the script pretty much