import requests

r = requests.get("https://northstar.tf/client/servers")   # get the server list

serverindex = 0
indexlimit = 20
if r.status_code == 200:
  for server in r.json():    # iterate through server list
    servername = server["name"]
    playercount = server["playerCount"]
    playermax = server["maxPlayers"]
    serverregion = server["region"]
    servermap = server["map"]
    print(servername)
    print("Map: " + servermap)
    print("Region: " + serverregion)
    print("Playercount: " + "[" + str(playercount) + "/" + str(playermax) + "]")
    print("=========================")
  
    serverindex += 1
    if serverindex >= indexlimit:
      break
else:
  print("Error gathering information")
