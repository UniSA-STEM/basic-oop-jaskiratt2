"""
File: Asset.py
Description: <A class representing a valuable asset which can be identified by a name, description and encrypted/decrypted.>
Author: <Jaskirat Uppal>
ID: <110426141>
Username: <uppjy001>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    """
    Represents a single value asset.
    Attributes like name, description and encrypted.
    """
    def __init__(self, name, description):

        """Initialise an Asset object"""
        self.name = name
        self.description = description
        self.encrypted = False

    def get_name(self):
        return self.name
    """Return name of an asset"""

    def get_description(self):
        return self.description
    """Return a description of an asset"""

    def is_encrypted(self):
        return self.encrypted
    """Returns the current encryption value of an asset """

    def set_name(self, name):
        """Sets new name for an asset, but only string is input"""
        if isinstance(name, str):
            self.name = name
        else:
            print("Sorry, name should be a string value")


    def set_description(self, description):
        """Sets a new description for an asset, but only string is input"""
        if isinstance(description, str):
            self.description = description
        else:
            print("Sorry, description should be a string value")

    def encrypt(self):
        """Encrypts the asset if encrypted is not done and then it will print a message"""
        if not self.encrypted:
            self.encrypted = True
            print(f"{self.name} came out to be encrypted")
        else:
            print(f"{self.name} is previously encrypted")

    def decrypt(self):
        """Decrypts the asset if it is encrypted already and prints a message"""
        if self.encrypted:
            self.encrypted = False
            print(f"{self.name} cam out to be decrypted")
        else:
            print(f"{self.name} is previously decrypted")

    def __str__(self):
        return f"{self.name}, {self.description}" + ("[Encrypted]" if self.encrypted else "")

    def design_crypto_token():
        """Designs and return CryptoToken asset"""
        return Asset("CryptoToken", "It is used to acquire or repair rigs")

    def design_data_spike():
        """Designs and return Data Spike asset"""
        return Asset("Data Spike", "will be used in battles")

    def design_removable_drive():
        """Designs and return Removable Drive asset"""
        return Asset("Removable Drive", "It is found in rigs and used for extraction")

    def design_security_chip():
        """Designs and return Security Chip asset"""
        return Asset("Security Chip", "It is used to encrypt or decrypt assets")

    def design_hardware_patch():
        """Designs and return Hardware Patch asset"""
        return Asset("Hardware Patch", "It is used to upgrade rigs")

