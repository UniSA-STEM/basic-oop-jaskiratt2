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
        if isinstance(name, str):
            self.name = name
        else:
            print("Sorry, name should be a string value")


    def set_description(self, description):
        if isinstance(description, str):
            self.description = description
        else:
            print("Sorry, description should be a string value")

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

    def __str__(self):
        return f"{self.name}, {self.description}" + ("[Encrypted]" if self.encrypted else "")

    def design_crypto_token():
        return Asset("CryptoToken", "It is used to acquire or repair rigs")

    def design_data_spike():
        return Asset("Data Spike", "will be used in battles")

    def design_removable_drive():
        return Asset("Removable Drive", "It is found in rigs and used for extraction")

    def design_security_chip():
        return Asset("Security Chip", "It is used to encrypt or decrypt assets")

    def design_hardware_patch():
        return Asset("Hardware Patch", "It is used to upgrade rigs")

