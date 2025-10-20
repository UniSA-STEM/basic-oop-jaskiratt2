""" File: Hacker.py
Description: <A Hacker class that can acquire rigs, launch attacks and encrypt assets.>
Author: <Jaskirat Uppal>
ID: <110426141>
Username: <uppjy001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    """Initialise a Hacker class with a name, trace level, inventory and rig"""
    def __init__(self, name):
        self.name = name
        self.trace_level = 0
        self.inventory = [Asset("CryptoToken", "either it will acquire or repare the rigs")]
        self.rig = None

    def get_name(self):
        """Gets hacker's name"""
        return self.name

    def get_trace_level(self):
        """Gets hacker's current trace level"""
        return self.trace_level

    def get_inventory(self):
        """Gets hacker's inventory"""
        return self.inventory

    def get_rig(self):
        """Gets hacker's rig"""
        return self.rig

    def set_name(self, name):
        """Sets hacker's name and making it as a string"""
        if isinstance(name, str):
            self.name = name
        else:
            print("Sorry, name should be a string value")

    def acquire_rig(self):
        """Acquire new rig with the help of CryptoToken from inventory"""
        for asset in self.inventory:
            if asset.name == "CryptoToken":
                self.rig = Rig(self.name + "Rig")
                self.inventory.remove(asset)
                print(f"{self.name}a new rig has been activate named {self.rig.get_name()}")
                return
            print(f"{self.name}Sorry, can't acquire a rig because no CrytoToken was found")

    def launch_data_spike(self, target_hacker):
        """Launch a data spike attack on target hacker rig"""
        if self.rig is None:
            print(f"{self.name} cannot launch an attack because of no rig")
            return
        if target_hacker.rig is None:
            print(f"{target_hacker.name} no rig to attack")
            return
        for asset in self.rig.get_storage():
            if asset.name == "Data Spike":
                self.rig.get_storage().remove(asset)
                print(f"{self.name} Data Spike launched at {target_hacker.name}")
                target_hacker.rig.take_hit()
                self.trace_level += 1
                if self.trace_level > 5:
                    print(f"{self.name} It is exposed because of high trace level")
                return
        print(f"{self.name} no more Data Spike is left to attack")

    def encrypt_assets(self, target_rig):
        """Encrypt all assets that are broken and in target rig"""
        if target_rig is None or not target_rig.is_broken():
            print(f"{self.name} no encryption because target rig is not broken")
            return
        for asset in target_rig.get_storage():
            if not asset.is_encrypted():
                asset.encrypt()
        print(f"{self.name} all asset is encrypted in {target_rig.get_name()}")

    def add_to_inventory(self, asset):
        """Add an asset to inventory if it is unencrypted and valid"""
        if isinstance(asset, Asset) and not asset.is_encrypted():
            self.inventory.append(asset)
            print(f"{asset.name} has added to {self.name}'s inventory")
        else:
            print(f"{asset.name} cant add to {self.name}'s inventory because it is encrypted or invalid")

    def extract_assets(self, target_rig):
        """Extract unencrypted assets from rig"""
        if target_rig.is_broken():
            for asset in target_rig.get_storage():
                if not asset.is_encrypted():
                    self.add_to_inventory(asset)
                    target_rig.get_storage().remove(asset)
            print(f"{self.name} extracted unencrypted assets from {target_rig.get_name()}")
        else:
            print(f"{self.name} cannot extract assets, {target_rig.get_name()} is not broken")

    def upgrade(self):
        """Upgrade using Hardware Patch to the hacker's rig"""
        if self.rig is None:
            print(f"{self.name} cannot upgrade without a rig")
            return
        for asset in self.inventory:
            if asset.name == "Hardware Patch":
                self.inventory.remove(asset)
                self.rig.upgrade()
                print(f"{self.name} upgraded {self.rig.get_name()}")
                return
        print(f"{self.name} Sorry, no Hardware Patch available to upgrade")

    def store_asset(self, asset):
        """Store an asset to rig's storage from inventory"""
        if self.rig and not asset.is_encrypted():
            self.inventory.remove(asset)
            self.rig.get_storage().append(asset)
            print(f"{self.name} stored {asset.name} in {self.rig.get_name()}")

    def retrieve_asset(self, asset_name):
        """Retrieve a asset from rig's storage to inventory """
        if self.rig:
            for asset in self.rig.get_storage():
                if asset.name == asset_name and not asset.is_encrypted():
                    self.rig.get_storage().remove(asset)
                    self.inventory.append(asset)
                    print(f"{self.name} is retrieved under {asset_name} from {self.rig.get_name()}")
                    return True
            print(f"{self.name} {asset_name} is not found or encrypted anywhere in {self.rig.get_name()}")
            return False

    def scan_inventory(self, asset_name):
        """Scan asset from inventory"""
        for asset in self.inventory[:]:
            if asset.name == asset_name:
                self.inventory.remove(asset)
                print(f"{self.name} is removed under {asset_name} from inventory")
                return asset
        print(f"{self.name} {asset_name} is not found in inventory")
        return None

    def __str__(self):

        rig_name = self.rig.get_name() if self.rig else "None"
        inventory_name = self.inventory[0].name if self.inventory else "None"
        return f"{self.name}, {rig_name}, Trace Level: {self.trace_level}, {inventory_name}" + ("[Exposed]" if self.trace_level > 5 else "")