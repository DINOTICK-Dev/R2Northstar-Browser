import requests
import os

r = requests.get("https://northstar.tf/client/servers")

def ServerCountGet():     # Get servercount information
  global servercount
  servercount = 0
  if r.status_code == 200:
    for server in r.json():    # iterate through server list
      servercount = servercount+1
  else:
    print("Error gathering information")

def refresh():     # Refreshes information
  ServerCountGet()

ServerCountGet()