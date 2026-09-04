# Things that don't change, like war
import os

from reconstruct import game_path

mv_extension_map = {
    ".rpgmvo": ".ogg",
    ".rpgmvp": ".png",
    ".rpgmvm": ".m4a"
}

mv_proj_filename = "Game.rpgproject"
mv_proj_content = "RPGMV 1.6.3"
mv_system_json = os.path.join(game_path, "data", "System.json")

rpgm_dirs = ["audio", "css", "data", "effects", "fonts", "icon", "img", "js", "movies"]
rpgm_files = ["package.json", "index.html"]