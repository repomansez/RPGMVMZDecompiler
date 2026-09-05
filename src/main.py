from decrypt import decrypt_mv, decrypt_mz
from reconstruct import reconstruct, determine_rpgmver


def main():
    old_gamepath = input("old dir: ")
    game_path = input("new dir: ")
    rpgm_version = determine_rpgmver(old_gamepath)

    reconstruct(old_gamepath, game_path, rpgm_version)
    if rpgm_version == "MV":
        decrypt_mv(game_path)
    elif rpgm_version == "MZ":   
        decrypt_mz(game_path)

if __name__ == "__main__":
    main()