import requests
import sys
import os
import time
from func.playcnt import *
from func.servbrow import *
from func.servcnt import *
from func.playcnt import refresh as playref
from func.servbrow import refresh as browref
from func.servcnt import refresh as servref
from rich import print

"""
Ion Server Browser
Made by DINOTICK
"""

def ErrorMSG(sleeptime):
  time.sleep(sleeptime)
  sys.exit()


def cls():
  try:
    os.system('cls' if os.name=='nt' else 'clear')
  except:
    print("[red]There was an error wiping the screen, are you on a supported operating system? (Linux, Windows)[/red]")
    ErrorMSG(2)
    

def RefreshAll(): 
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


def ShowCredits():
  print("[orange1]Made by DINOTICK[/orange1]")
  print("[red]Youtube:  https://www.youtube.com/@dinotick[/red]")
  print("[bright_black]Github:  https://github.com/DINOTICK-Dev[/bright_black]")
  print("[dodger_blue2]Discord:  DINOTICK#6969[/dodger_blue2]")
  print("[bold orange1]Press enter to go back[/bold orange1]")
  input("")
  runtime()


def runtime():
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

runtime()