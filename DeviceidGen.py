import json
import os
try:
    import names
except ModuleNotFoundError:
    os.system("pip install names")
    import names
import threading
from hashlib import sha1
from functools import reduce
from base64 import b85decode, b64decode
import random
import requests
import hmac
import platform,socket,re,uuid
os.system("clear")
print("\n\33[93;5;5m\33[93;5;234m ❮ DeviceId Generator ❯ \33[0m\33[93;5;235m\33[93;5;5m \33[0m")
def device_gen():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    key='02b258c63559d8804321c5d5065af320358d366f'
    mac = hmac.new(bytes.fromhex(key), b"\x42" + identifier, sha1)
    return (f"42{identifier.hex()}{mac.hexdigest()}").upper()
    
def dev():
	try:
		for i in range(generatingnumber):
			device = device_gen()
			devfile = open('deviceid.txt', "a+")
			devfile.write(device + '\n\n')
	except:
		return

generatingnumber = int(input("\nNo. of DeviceId to Generate : "))

dev()
print(f"\nGenerated {generatingnumber} deviceids")