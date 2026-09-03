import os
import shutil
import time

rpgm_dirs = ["audio", "css", "data", "effects", "fonts", "icon", "img", "js", "movies"]
rpgm_files = ["package.json"]


def copy_files():
    if os.path.exists("files"):
        print("Deleting shitty directory")
        time.sleep(1)
        shutil.rmtree("files")
        os.mkdir("files")
    else:
        os.mkdir("files")

    for dir in rpgm_dirs:
        source = os.path.join("game", "www", dir)
        dest = os.path.join("files", dir)
        if not os.path.isdir(source):
            print("Skipping missing directory:", dir)
            time.sleep(1)
            continue
        print("Copying directory:" + dir)
        shutil.copytree(source, dest)

copy_files()