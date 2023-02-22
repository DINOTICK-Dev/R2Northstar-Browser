# Ion Server Browser

Gathers information about the Northstar server browser! Made entirely in Python, enjoy!

## Contributing
To contribute, please open a pull-request, and label what it does, and why you think it should be added. It'll be added if I believe it's fitting or helps with the project.
Acceptable PRs/Contributions:
- Bug Fixes
- Features
- Translations (COMING SOON!)

## How it Works

Ion Server first gathers information from the masterserver url, `https://northstar.tf/client/servers`. This is because the following link contains UPDATED information on the Northstar masterserver, as `northstar.tf` is the URL for the Titanfall 2 +Northstar Masterserver which contains information and registers the server for all players to see in-game. My scripts grab that URL and rip its information using the `requests` module for Python, which grabs an unparsed output and turns it into a dictionary so you can parse it with ease. An unparsed generated dictionary would look somewhat like this:
```
{
    'lastHeartbeat': 1234567890123,
    'id': '3c86ks29gs9f89r9s98',
    'name': 'Default Server Name',
    'region': 'Some Region Here',
    'description': 'Welcome to my very awesome super cool server!',
    'playerCount': 0,
    'maxPlayers': 16,
    'map': 'mp_box',
    'playlist': 'ps',
    'hasPassword': False,
    'modInfo': {
        'Mods': [
            {
                'Name': 'Northstar.Custom',
                'Version': '1.12.0',
                'RequiredOnClient': True
            }
        ]
    }
}
```
This following information tells us ALOT about the server... For example, the name obviously refers to the name of the server. The "playlist" section is informing you about what gamemode is being played... for example, `ps` means private server. (If I remember correctly lol) When you register a server, the information setup in your server's `config` files will change this information on the server browser making a parsable framework for running through the serverbrowser!

## How to Install
(WARNING! THIS IS NOT DONE, AND STILL BEING WORKED ON, MEANING THERE WILL BE NO DOWNLOADABLE BUILD YET AND RUNNING FROM SOURCE MAY NOT WORK)
Download the sourcecode, and run `pip install rich` then run `main.py` or you can download a "compiled" .exe file from the releases tab.