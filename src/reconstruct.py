import os
import shutil
import time

from constants import *

#game_path = "files"

def determine_rpgmver(old_gamepath):
    if os.path.exists(os.path.join(old_gamepath, "www")):
        rpgm_version = "MV"
        return rpgm_version
    elif os.path.exists(os.path.join(old_gamepath, "js")):
        rpgm_version = "MZ"
        return rpgm_version
    else:
        print("Couldn't detect RPGM version")
        sys.exit(1)

def copy_files(old_gamepath, game_path, rpgm_version):
    if os.path.exists(game_path):  # This gotta be gone l8r!
        print("Deleting shitty directory")
        time.sleep(1)
        shutil.rmtree("files")
        os.mkdir("files")
    else:
        os.mkdir("files")

    for dir in rpgm_dirs:
        if rpgm_version == "MV":
            source = os.path.join("game", "www", dir)
            dest = os.path.join("files", dir)
        elif rpgm_version == "MZ":
            source = os.path.join("game", dir)
            dest = os.path.join("files", dir)

        if not os.path.isdir(source):
            print("Skipping missing directory:", dir)
            time.sleep(1)
            continue
        print("Copying directory:" + dir)
        shutil.copytree(source, dest)


def create_project_file(game_path, rpgm_version):
    if rpgm_version == "MV":
        project_file = os.path.join(game_path, mv_proj_filename)
        with open(project_file, "w", encoding="utf-8") as file:
            file.write(mv_proj_content)
    elif rpgm_version == "MZ":
        project_file = os.path.join(game_path, mz_proj_filename)
        with open(project_file, "w", encoding="utf-8") as file:
            file.write(mz_proj_content)

def reconstruct(old_gamepath, game_path, rpgm_version):
        copy_files(old_gamepath, game_path, rpgm_version)
        create_project_file(game_path, rpgm_version)
