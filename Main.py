"""
File: main.py
Description: <A Main file to test all the 3 Asset, Rig and Hacker classes>
Author: <Jaskirat Uppal>>
ID: <110426141>>
Username: <uppjy001>>>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig
from Hacker import Hacker


def design_crypto_token():
    """Design and returns a CryptoToken asset."""
    return Asset("CryptoToken", "It is used to acquire or repair rigs")

def design_hardware_patch():
    """Design and returns a Hardware Patch asset."""
    return Asset("Hardware Patch", "It is used to upgrade rigs")

hacker1 = Hacker("HackerOne")
hacker2 = Hacker("HackerTwo")

hacker1.acquire_rig()
hacker2.acquire_rig()
hacker2.get_rig().repair(hacker2)


if hacker1.rig:
    hacker1.rig.generate_asset()
    print(f"Hacker1 Rig Storage: {[str(asset) for asset in hacker1.rig.get_storage()]}")


if hacker1.rig and hacker2.rig:
    hacker1.launch_data_spike(hacker2)
    print(f"Hacker2 Rig Condition: {hacker2.rig.condition()}")
    hacker1.launch_data_spike(hacker2)
    print(f"Hacker1 Trace Level: {hacker1.get_trace_level()}")

crypto_token = design_crypto_token()
hacker2.inventory.append(crypto_token)
hacker2.rig.take_hit()
hacker2.rig.take_hit()
print(f"Hacker2 Rig Condition before repair: {hacker2.rig.condition()}")
hacker2.get_rig().repair(hacker2)
print(f"Hacker2 Rig Condition after repair: {hacker2.rig.condition()}")


hardware_patch = design_hardware_patch()
hacker2.inventory.append(hardware_patch)
hacker2.get_rig().repair(hacker2)
print(f"Hacker2 Rig Upgrade Level: {hacker2.rig.get_upgrade_level()}")


hacker2.rig.take_hit()
hacker2.rig.take_hit()
hacker1.encrypt_assets(hacker2.rig)
for asset in hacker2.rig.get_storage():
    print(f"Asset {asset.name} is {str(asset)}")

new_asset = Asset("TestAsset", "Test Description")
hacker2.rig.store_asset(new_asset)
new_asset.encrypt()
hacker2.rig.store_asset(new_asset)
released_asset = hacker2.rig.release_asset("TestAsset")
if released_asset:
    print(f"Released Asset: {str(released_asset)}")