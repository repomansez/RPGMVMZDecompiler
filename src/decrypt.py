import json
import os

from constants import *
from constants import rpgm_encrypted_dirs


# RPGM "encrypts" files by adding 16 bytes of junk at the start, then XORing the next 16 bits with an encryption key
# if you remove the first 16 bytes and XOR the 16 next bytes again, you get the original file :)
def get_enc_key():
    with open(mv_system_json, "r") as file:
        system_json = json.load(file)
        md5_hash = system_json["encryptionKey"]
        return bytes.fromhex(md5_hash)

def decrypt_file(filepath, filedir, filextension):
    key = get_enc_key()
    new_extension = mv_extension_map[filextension]
    input_path = filepath
    output_path = os.path.splitext(filepath)[0] + new_extension

    with open(file=filepath, mode="rb") as encrypted_file:
        output: bytearray = bytearray(encrypted_file.read()[16:])
    for i in range(16):
        output[i] ^= key[i]
    with open(file=output_path, mode="wb") as file:
        file.write(output)

    print(filepath, "decrypted.")

def list_files():
    for directory in rpgm_encrypted_dirs:
        recurse_dir = os.path.join(game_path, directory)
        for root, dirs, files in os.walk(recurse_dir):
            for f in files:
                file_dir  = root
                file_path = os.path.join(root, f)
                file_name = f
                file_extension = os.path.splitext(f)[1]
                if file_extension in mv_extension_map:
                    #print("decrypting file: ", file_path, file_name, root)
                    decrypt_file(file_path, file_dir, file_extension)

list_files()