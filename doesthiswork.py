import requests
import tkinter as tk
from tkinter import messagebox
import os

def download_mod(url, path):
    # Downloads the mod from the given URL to the specified path
    response = requests.get(url)
    with open(path, "wb") as file:
        file.write(response.content)

def install_ea():
    # Installs the mod for the EA app
    # Replace the file path with the appropriate destination for the EA app
    download_mod("https://github.com/R2Northstar/Northstar/releases/latest", "C:\Program Files\EA Games\Titanfall2")
    messagebox.showinfo("Northstar Mod", "Northstar Mod successfully installed for the EA app!")

def install_steam():
    # Installs the mod for Steam
    # Replace the file path with the appropriate destination for Steam
    download_mod("https://github.com/R2Northstar/Northstar/releases/latest", "C:\Program Files (x86)\Steam\steamapps\common\Titanfall2")
    messagebox.showinfo("Northstar Mod", "Northstar Mod successfully installed for Steam!")

# Create the main window
root = tk.Tk()
root.title("Northstar Mod Installer")

# Create the installation options button
install_ea_button = tk.Button(root, text="Install for EA", command=install_ea)
install_steam_button = tk.Button(root, text="Install for Steam", command=install_steam)

# Add the buttons to the window
install_ea_button.pack()
install_steam_button.pack()

# Start the GUI event loop
root.mainloop()
