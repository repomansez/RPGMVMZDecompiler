import os
import shutil
import time

from constants import *

#game_path = "files"


def copy_files(old_gamepath, game_path):
    if os.path.exists(game_path):  # This gotta be gone l8r!
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


def create_project_file(game_path):
    project_file = os.path.join(game_path, mv_proj_filename)
    with open(project_file, "w", encoding="utf-8") as file:
        file.write(mv_proj_content)

def reconstruct(old_gamepath, game_path):
    copy_files(old_gamepath, game_path)
    create_project_file(game_path)