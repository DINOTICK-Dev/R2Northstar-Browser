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

def ShowComingSoon():
  print("[orange1]Coming soon! Make sure to check back on the github[/orange1] [bright_black](https://github.com/DINOTICK-Dev/R2Northstar-Browser)[/bright_black]")
  print("[bold orange1]Press enter to go back[/bold orange1]")
  input("")
  runtime()


def ShowCredits():     # Could use some cleaning up
  print("[orange1]Made by DINOTICK[/orange1]")
  print("[green]Website:  https://dinotick.github.io[/green]")
  print("[red]Youtube:  https://www.youtube.com/@dinotick[/red]")
  print("[bright_black]Github:  https://github.com/DINOTICK-Dev[/bright_black]")
  print("[dodger_blue2]Discord:  DINOTICK#6969[/dodger_blue2]")
  print("[bold orange1]Press enter to go back[/bold orange1]")
  input("")
  runtime()

def PrintInfo(serverpage):     # Gets information on the server using a nifty indexing thingy
  print("[orange1]===============[/orange1]")
  try:
    for x in range(serverpage, serverpage+5):
      if serverdict[x]["hasPassword"] == True:
        serverpass = "[Password Protected]"
      else:
        serverpass = ""
      print("[orange1]Name: "+serverdict[x]["name"] + "[/orange1]    [bright_cyan]" + serverpass+"[bright_cyan]")
      print("[orange1]Playercount: [" + str(serverdict[x]["playerCount"])+"/"+str(serverdict[x]["maxPlayers"])+"][/orange1]")
      try:
        print("[orange1]Region: " + serverdict[x]["region"]+"[/orange1]")
      except:
        print("[orange1]Region: Unkown[/orange1]")
      print("[orange1]Map: " + serverdict[x]["map"] + "[/orange1]")
      print("[bold orange1]=================[/bold orange1]")
  except:
    pass

def ShowBrowser():     # Serverbrowser CLI :skull:
  indexedvariable = 0
  PrintInfo(0)
  while True:
    print("[orange1]Page: ["+str(int(indexedvariable/5))+"/"+str(int(servercount/5))+"][/orange1]")
    print("[orange1]Servercount: "+str(int(servercount))+"[/orange1]")
    print("[orange1]Playercount: ["+str(int(totalplayers))+"/"+str(int(maxplayers))+"][/orange1]")
    print("[orange1](R = Refresh)[/orange1]")
    print("[orange1](A = Go back a page) (D = Go to the next page) (ENTER = Go back)[/orange1]")
    browserpageindex = input("").lower()
    if browserpageindex == "a" and indexedvariable > 0:
      cls()
      indexedvariable = indexedvariable-5
      PrintInfo(indexedvariable)
    if browserpageindex == "d":
      cls()
      indexedvariable = indexedvariable+5
      PrintInfo(indexedvariable)
    if browserpageindex == "r":
      cls()
      RefreshAll()
      PrintInfo(indexedvariable)
    if browserpageindex == "":
      break
      runtime()
    else:
      cls()
      PrintInfo(indexedvariable)

  runtime()

def runtime():     # Main function, used to run everything and piece it all together
  cls()
  RefreshAll()
  print("[orange3]Welcome to Ion Mod Manager[/orange3]")
  print("[orange1]Please select an action: \n(1: Server Browser) (2: Coming Soon) (3: Credits)[/orange1]")
  inputinfo = input("")
  if inputinfo == "1":
    cls()
    ShowBrowser()
  if inputinfo == "2":
    cls()
    ShowComingSoon()
  if inputinfo == "3":
    cls()
    ShowCredits()
  elif inputinfo == "":
    sys.exit()

runtime()     # Starts the script pretty much