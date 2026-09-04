import json

from constants import mv_system_json


def get_enc_key():
    with open(mv_system_json, "r") as file:
        system_json = json.load(file)
        md5_hash = system_json["encryptionKey"]
        return bytes.fromhex(md5_hash)

def decrypt_files():
    key = get_enc_key()
    print(key)

decrypt_files()