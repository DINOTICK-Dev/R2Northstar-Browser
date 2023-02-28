import requests
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

r = requests.get("https://northstar.tf/client/servers")     # get the server list

global serverdict 
serverdict = {}

def ServerGet():
  servnum = 0
  # global serverregion
  # global serverpass
  # global servername
  # global servermap
  if r.status_code == 200:
    for server in r.json():    # iterate through server list

      serverdict[servnum] = server
      servnum += 1

      
      # Previously used code that I don't need but I'm keeping just in case lol      
      """
      try:    # This is here because servers with passwords don't give a region
        serverregion = server["region"]
      except:
        serverregion = ["Unknown"]
        
      if server["hasPassword"] == True:    # Password protection :)
        serverpass = "[Password Protected]"
      else:
        serverpass = ""  
      
      servername = server["name"]
      servermap = server["map"]
      """

  else:
    print("Error gathering information")

def refresh():
  ServerGet()
  
ServerGet()