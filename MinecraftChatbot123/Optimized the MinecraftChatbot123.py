import os
import threading
import webbrowser
from configparser import ConfigParser
from tkinter import Button, Entry, Label, Tk

config = ConfigParser()
config.read('config.ini')


def startbot():

    @On(bot, "chat")
    def antiafk(this, username, message, *args):

        elif message.lower() in ['go']:
            bot.chat('Please be respectful.')

def stopb():

class MinecraftBotApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):

def main():
    root = Tk()
    app = MinecraftBotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
