import requests
import os

r = requests.get("https://northstar.tf/client/servers")

def PlayerCountGet():
  global totalplayers
  global maxplayers
  totalplayers = 0
  maxplayers = 0
  if r.status_code == 200:
    for server in r.json():    # iterate through server list
      playercount = server["playerCount"]
      playermax = server["maxPlayers"]
      totalplayers = totalplayers+playercount
      maxplayers = maxplayers+playermax

def refresh():
  PlayerCountGet()

PlayerCountGet()