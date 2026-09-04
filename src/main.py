from decrypt import decrypt
from reconstruct import reconstruct


def main():
    old_gamepath = input("old dir: ")
    game_path = input("new dir: ")
    reconstruct(old_gamepath, game_path)
    decrypt(game_path)

if __name__ == "__main__":
    main()