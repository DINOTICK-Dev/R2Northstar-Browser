import requests
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

r = requests.get("https://northstar.tf/client/servers")     # get the server list

def ServerGet():
  global serverregion
  global serverpass
  global servername
  global servermap
  if r.status_code == 200:
    for server in r.json():    # iterate through server list

      
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
  
  else:
    print("Error gathering information")

ServerGet()