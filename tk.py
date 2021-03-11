import tkinter as tk
import requests
import json
from tkinter import font
from pycoingecko import CoinGeckoAPI

class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_components()
    
    def init_components(self):
        self.fuente = font.Font(weight='bold')
        self.create_etiq_btc()
        self.create_etiq_ada()
        self.create_etiq_dot()
        self.create_etiq_eth()
        self.create_etiq_eth_gass()
        self.create_refresh_widget()
        self.create_exit_widget()

    def create_etiq_btc(self):
        self.etiq_btc = tk.Label(self)
        self.etiq_btc["text"] = "Btc: " + self.get_price("btc")
        self.etiq_btc["font"] = self.fuente
        self.etiq_btc.pack(side="top")

    def create_etiq_ada(self):
        self.etiq_ada = tk.Label(self)
        self.etiq_ada["text"] = "Ada: " + self.get_price("ada")
        self.etiq_ada["font"] = self.fuente
        self.etiq_ada.pack(side="top")
    
    def create_etiq_dot(self):
        self.etiq_dot = tk.Label(self)
        self.etiq_dot["text"] = "Dot: " + self.get_price("dot")
        self.etiq_dot["font"] = self.fuente
        self.etiq_dot.pack(side="top")

    def create_etiq_eth(self):
        self.etiq_eth = tk.Label(self)
        self.etiq_eth["text"] = "Eth: " + self.get_price("eth")
        self.etiq_eth["font"] = self.fuente
        self.etiq_eth.pack(side="top")
    
    def create_etiq_eth_gass(self):
        self.etiq_eth_gass = tk.Label(self)
        self.etiq_eth_gass["text"] = "Gas:   " + self.get_price("eth_gas")
        self.etiq_eth_gass["font"] = self.fuente
        self.etiq_eth_gass.pack(side="top")

    def create_refresh_widget(self):
        self.refresh = tk.Button(self)
        self.refresh["text"] = "Refresh"
        self.refresh["fg"] = "black"
        self.refresh["bg"] = "yellow"
        self.refresh["command"] = self.update_coins
        self.refresh.pack(side="left")

    def create_exit_widget(self):
        self.exit = tk.Button(self)
        self.exit["text"] = "Exit"
        self.exit["fg"] = "black"
        self.exit["bg"] = "red"
        self.exit["command"] = self.master.destroy
        self.exit.pack(side="right")
        
    def update_coins(self):
        self.etiq_btc["text"] = "Btc: " + self.get_price("btc")
        self.etiq_eth["text"] = "Eth: " + self.get_price("eth")
        self.etiq_ada["text"] = "Ada: " + self.get_price("ada")
        self.etiq_dot["text"] = "Dot: " + self.get_price("dot")
        self.etiq_eth_gass["text"] = "Gas:   " + self.get_price("eth_gas")
    
    def get_price(self, coin):
        try:
            if(coin == "btc"):
                return str(cg.get_price(ids='bitcoin', vs_currencies='usd')["bitcoin"]["usd"])
            elif(coin == "eth"):
                return str(cg.get_price(ids='ethereum', vs_currencies='usd')["ethereum"]["usd"])
            elif(coin == "ada"):
                return str(cg.get_price(ids='cardano', vs_currencies='usd')["cardano"]["usd"])
            elif(coin == "dot"):
                return str(cg.get_price(ids='polkadot', vs_currencies='usd')["polkadot"]["usd"])
            elif(coin == "eth_gas"):
                gas = requests.get("https://ethgasstation.info/api/ethgasAPI.json?")
                if(gas.status_code == 200):
                    json_file = gas.json()
                    fastest = int(int(json_file["fastest"])/10)
                    fast = int(int(json_file["fast"])/10)
                    average = int(int(json_file["average"])/10)
                    slow = int(int(json_file["safeLow"])/10)
                    stri = "Fastest: "+str(fastest) + "  Fast: "+str(fast)
                    stri+="  Average: " + str(average) + "  SafeLow: " + str(slow)
                    return stri
        except:
            return "You're offline"

cg = CoinGeckoAPI()
root = tk.Tk()
root.geometry("500x160")
app = Window(root)
app.master.title("Cryptocurrency ticker by Lluc")
app.mainloop()