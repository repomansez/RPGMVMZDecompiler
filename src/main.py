from decrypt import decrypt_mv, decrypt_mz
from reconstruct import reconstruct, determine_rpgmver
from cli import parse_args


def main():
    args = parse_args()
    old_gamepath = args.input
    game_path = args.output
    print(old_gamepath, game_path)

    rpgm_version = determine_rpgmver(old_gamepath)

    reconstruct(old_gamepath, game_path, rpgm_version)
    if rpgm_version == "MV":
        decrypt_mv(game_path)
    elif rpgm_version == "MZ":   
        decrypt_mz(game_path)

if __name__ == "__main__":
    main()