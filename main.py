import requests
import os

r = requests.get("https://northstar.tf/client/servers")     # get the server list

serverindex = 0
def ServerGet():
  if r.status_code == 200:
    for server in r.json():    # iterate through server list
  
      try:
        serverregion = server["region"]
      except:
        serverregion = ["Unknown"]
        
      if server["hasPassword"] == True:
        serverpass = "[Password Protected]"
      else:
        serverpass = ""  
      
      
      servername = server["name"]
      playercount = server["playerCount"]
      playermax = server["maxPlayers"]
      servermap = server["map"]
        
      print(servername + "     " + serverpass)
      print("Map: " + servermap)
      
      try:
        print("Region: " + serverregion)
      except:
        print("Region: Unknown")
        
      print("Playercount: " + "[" + str(playercount) + "/" + str(playermax) + "]")
      print("=========================")
      
      break
  
  else:
    print("Error gathering information")

ServerGet()