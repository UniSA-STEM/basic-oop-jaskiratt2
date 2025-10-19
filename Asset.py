"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: <Jaskirat Uppal>
ID: <110426141>
Username: <uppjy001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def is_encrypted(self):
        return self.encrypted

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def encrypt(self):
        if not self.encrypted:
            self.encrypted = True
            print(f"{self.name} came out to be encrypted")
        else:
            print(f"{self.name} is previously encrypted")

    def decrypt(self):
        if self.encrypted:
            self.encrypted = False
            print(f"{self.name} cam out to be decrypted")
        else:
            print(f"{self.name} is previously decrypted")

