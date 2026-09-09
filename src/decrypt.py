import json
import os


from sys import exit
from constants import *
from constants import rpgm_encrypted_dirs


# RPGM "encrypts" files by adding 16 bytes of junk at the start, then XORing the next 16 bits with an encryption key
# if you remove the first 16 bytes and XOR the 16 next bytes again, you get the original file :)
def get_enc_key(game_path):
    mv_system_json = os.path.join(game_path, "data", "System.json")
    with open(mv_system_json, "r") as file:
        system_json = json.load(file)
        md5_hash = system_json["encryptionKey"]
        return bytes.fromhex(md5_hash)


def decrypt_file_mv(game_path, filepath, filedir, filextension):
    key = get_enc_key(game_path)
    new_extension = mv_extension_map[filextension]
   # input_path = filepath
    output_path = os.path.splitext(filepath)[0] + new_extension
    print("FILEPATH: ", filepath)

    with open(file=filepath, mode="rb") as encrypted_file:
        output: bytearray = bytearray(encrypted_file.read()[16:])
    for i in range(16):
        output[i] ^= key[i]
    with open(file=output_path, mode="wb") as file:
        file.write(output)

    print(filepath, "decrypted.")


def list_files_mv(game_path):
    for directory in rpgm_encrypted_dirs:
        recurse_dir = os.path.join(game_path, directory)
        for root, dirs, files in os.walk(recurse_dir):
            for f in files:
                file_dir = root
                file_path = os.path.join(root, f)
               # file_name = f
                file_extension = os.path.splitext(f)[1]
                if file_extension in mv_extension_map:
                    # print("decrypting file: ", file_path, file_name, root)
                    decrypt_file_mv(game_path, file_path, file_dir, file_extension)

def decrypt_file_mz(game_path, filepath, filedir, filextension):
    key = get_enc_key(game_path)
    new_extension = mz_extension_map[filextension]
   # input_path = filepath
    output_path = os.path.splitext(filepath)[0] + new_extension

    with open(file=filepath, mode="rb") as encrypted_file:
        output: bytearray = bytearray(encrypted_file.read()[16:])
    for i in range(16):
        output[i] ^= key[i]
    with open(file=output_path, mode="wb") as file:
        file.write(output)

    print(filepath, "decrypted.")


def list_files_mz(game_path):
    for directory in rpgm_encrypted_dirs:
        recurse_dir = os.path.join(game_path, directory)
        for root, dirs, files in os.walk(recurse_dir):
            for f in files:
                file_dir = root
                file_path = os.path.join(root, f)
               # file_name = f
                file_extension = os.path.splitext(f)[1]
                if file_extension in mz_extension_map:
                    # print("decrypting file: ", file_path, file_name, root)
                    decrypt_file_mz(game_path, file_path, file_dir, file_extension)


def decrypt_mv(game_path):
    try:
        list_files_mv(game_path)
    except IndexError:
        print("Index Error! Gamefiles are likely corrupted.")
        exit(1)

def decrypt_mz(game_path):
    try:
        list_files_mz(game_path)
    except IndexError:
        print("Index Error! Gamefiles are likely corrupted.")
        exit(1)

