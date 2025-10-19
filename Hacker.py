"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: <Jaskirat Uppal>
ID: <110426141>
Username: <uppjy001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name ):
        self.name = name
        self.trace_level = 0
        self.inventory = [Asset("CrytoToken, either it will acquire or repare the rigs")]
        self.rig = None

    def acquire_rig(self):
        for asset in self.inventory:
            if asset.name == "CrytoToken":
                self.rig = Rig(self.name + "Rig", 0, False,0, [
                    Asset(''"Data is Spiking", " gonna launch the attacks"),
                    Asset("Data is Spiking", " gonna launch the attacks"),
                    Asset("Removal of Drive", "gonna extract the assets")
                ])
                print(f"{self.name}a new rig has been activate named {self.rig.name}")
                return
            print(f"{self.name}Sorry, can't acquire a rig because no CrytoToken was found")

    def launch_data_spike(self, target_hacker):
        if self.rig is None:
            print(f"{self.name} cannot launch an attack because of no rig")
            return
        if target_hacker.rig is None:
            print(f"{target_hacker.name} no rig to attack")
            return

        for asset in self.rig.storage:
            if asset.name == "Data Spike":
                self.rig.storage.remove(asset)
                print(f"{self.name} Data Spike launched at {target_hacker.name}")
                target_hacker.rig.take_hit()
                self.trace_level += 1
                if self.trace_level > 5:
                    print(f"{self.name} It is exposed because of high trace level")
                return
        print(f"{self.name} no more Data Spike is left to attack")
