import requests
import os

r = requests.get("https://northstar.tf/client/servers")     # get the server list

global serverdict 
serverdict = {}

def ServerGet():
  servnum = 0
  if r.status_code == 200:
    for server in r.json():    # iterate through server list

      serverdict[servnum] = server
      servnum += 1

  else:
    print("Error gathering information")

def refresh():
  ServerGet()
  
ServerGet()