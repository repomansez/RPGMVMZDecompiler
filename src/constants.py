# Things that don't change, like war
import os

#from reconstruct import game_path

## MV EXCLUSIVE ##################################################################
mv_extension_map = {".rpgmvo": ".ogg", ".rpgmvp": ".png", ".rpgmvm": ".m4a"}

mv_proj_filename = "Game.rpgproject"
mv_proj_content = "RPGMV 1.6.3"
##################################################################################

## MZ EXCLUSIVE ##################################################################
mv_extension_map = {".rpgmvo": ".ogg", ".rpgmvp": ".png", ".rpgmvm": ".m4a"}

mv_proj_filename = "Game.rmmzproject"
mv_proj_content = "RPGMZ 1.8.0"
##################################################################################

rpgm_dirs = ["audio", "css", "data", "effects", "fonts", "icon", "img", "js", "movies"]
rpgm_encrypted_dirs = ["audio", "img"]
rpgm_files = ["package.json", "index.html"]
