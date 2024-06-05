import os
import threading
from configparser import ConfigParser
from tkinter import Button, Entry, Label, Tk

import mineflayer
from javascript import On, require

class MinecraftBotApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        Label(self.root, text='IP Address: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=35, y=20)
        Label(self.root, text='IP Port: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=35, y=50)
        Label(self.root, text='Username: ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=35, y=80)

        self.host = Entry(self.root)
        self.host.place(x=135, y=20)

        self.port = Entry(self.root)
        self.port.place(x=135, y=50)

        self.nick = Entry(self.root)
        self.nick.place(x=135, y=80)

        Button(self.root, text='Start the bot', bg='#F0F8FF', font=('arial', 12, 'normal'), command=self.start_bot).place(x=200, y=115)
        Button(self.root, text='Server List', bg='#F0F8FF', font=('arial', 12, 'normal'), command=self.show_server_list).place(x=20, y=115)
        Button(self.root, text='Stop', bg='#F0F8FF', font=('arial', 12, 'normal'), command=self.stop_bot).place(x=131, y=115)
        Button(self.root, text="Based on", bg="#F0F8FF", font=('arial', 12, 'normal'), command=self.open_based_on).place(x=20, y=158)
        Button(self.root, text="My GitHub Page", bg="#F0F8FF", font=('arial', 12, 'normal'), command=self.open_github_page).place(x=131, y=158)

    def start_bot(self):
        bot_thread = threading.Thread(target=self.run_bot)
        bot_thread.start()

    def run_bot(self):
        bot = mineflayer.createBot({
            'host': self.host.get(),
            'port': int(self.port.get()),
            'username': self.nick.get()
        })

        @On(bot, "login")
        def login(this):
            bot.chat(config.get('command', 'commandjoin'))
            bot.chat('Hi everyone')


    def stop_bot(self):
        os.system('taskkill /f /im node.exe')

    def show_server_list(self):
        with open("ServerList.txt") as server_list_file:
            print(server_list_file.read())

    def open_based_on(self):
        webbrowser.open('https://github.com/YTFort/24-Aternos')

    def open_github_page(self):
        webbrowser.open('https://github.com/Ateee329')

def main():
    root = Tk()
    app = MinecraftBotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
