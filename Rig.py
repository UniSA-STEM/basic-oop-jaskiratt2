"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: <Jaskirat Uppal>
ID: <110426141>
Username: <uppjy001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        self.storage = [
            Asset.design_data_spike(),
            Asset.design_data_spike(),
            Asset.design_removable_drive()
        ]

    def get_name(self):
        return self.name

    def get_damage(self):
        return self.damage

    def is_broken(self):
        return self.broken

    def get_upgrade_level(self):
        return self.upgrade_level

    def get_storage(self):
        return self.storage

    def repair(self, hacker):
        for asset in hacker.inventory:
            if asset.name == "CryptoToken":
                if self.damage > 0 or self.broken:
                    hacker.inventory.remove(asset)
                    self.damage = 0
                    self.broken = False
                    print(f"{self.name} restored successfully with the help of CryptoToken")
                    return
                else:
                    print(f"{self.name} no repair required")
                    return
        print("Sorry, Failure of Repair!! No CryptoToken accessible")

    def upgrade(self, hacker):
        for asset in hacker.inventory:
            if asset.name == "Hardware Patch":
                hacker.inventory.remove(asset)
                self.upgrade_level += 1
                print(f"{self.name} level has been upgraded {self.upgrade_level}")
                return
        print("Sorry, Failed to upgrade!! unable to find Hardware Patch")

    def take_hit(self):
        self.damage += 1
        print(f"{self.name} hit taken. Currently the damage is {self.damage}")
        if self.damage >= 2 + self.upgrade_level:
            self.broken = True
            print(f"{self.name} hit has broken")

    def generate_asset(self):
        new_asset = Asset("It is a security chip", "It will be used for whether encryption or decryption")
        self.storage.append(new_asset)
        print(f"{self.name} new asset is generated {new_asset.name}")

    def store_asset(self, asset):
        if asset.encrypted:
            print(f"{asset.name} It is encrypted due to which we cannot store the asset")
        else:
            self.storage.append(asset)
            print(f"{asset.name} has been stored into {self.name}")

    def release_asset(self, asset_name):
        for asset in self.storage:
            if asset.name == asset_name:
                if asset.encrypted:
                    print(f"{asset.name} It cannot be transferred because of encryption")
                    return None
                self.storage.remove(asset)
                print(f"{asset.name} has been removed from {self.name}")
                return asset
        print(f"{asset_name} unable to found in {self.name}")
        return None

    def condition(self):
        if self.broken:
            return f"Broken (Level {self.upgrade_level})"
        return f"Pristine (Level {self.upgrade_level})"


