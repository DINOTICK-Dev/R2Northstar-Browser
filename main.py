import requests
import os
from func.playcnt import *
from func.servbrow import *
from func.servcnt import *
from rich.console import Console
from rich.table import Table
from rich import print
from rich.layout import Layout

"""
Ion Server Browser
Made by DINOTICK
Ion Server Browser is a simple server browser made in python for the Titanfall 2 community mod "Northstar" that has some tools for the northstar serverbrowser

How it Works:
The files inside of the folder "func" are used for obtaining information, such as players, maxplayers, a parsable dictionary (oo lah lah!) and servercount. Then you can import variables from this main.py file here! Easy as pie... Or cake... Or whatever you call it.
"""

def cls():
    os.system('cls' if os.name=='nt' else 'clear')