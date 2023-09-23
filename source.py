from config import *
from encrypt import encrypt
from decrypt import decrypt
from key_picker import pick_key


def get_integer() -> int:
    while True:
        number = input()
        if quit_check(number):
            return QUIT_ID
        try:
            number = int(number)
            return number
        except ValueError:
            print("Enter an integer : ", end='')


def quit_check(command: str):
    for quit_command in QUIT_COMMANDS:
        if command == quit_command:
            return True
    return False


Exit = False
Mode = KEY_CHANGER
Key = 0
String = ""
while not Exit:
    if Mode == MENU_MODE:
        print(f"Enter {QUIT_COMMANDS} to get back to main menu")
        print(f"Change key - {KEY_CHANGER}\tEncrypt - {ENCRYPT_MODE}")
        print(f"Decrypt - {DECRYPT_MODE}\tFind key - {KEY_FINDER_MODE}")
        print("Choose mode : ", end='')
        Mode = get_integer()
    elif Mode == KEY_CHANGER:
        print(f"Enter key (0-{MAX_KEY}) : ", end='')
        Key = get_integer()
        if Key > MAX_KEY:
            Key = MAX_KEY
        Mode = MENU_MODE
    elif Mode == ENCRYPT_MODE:
        String = input()
        if quit_check(String):
            Mode = MENU_MODE
        else:
            print(encrypt(String, Key))
    elif Mode == DECRYPT_MODE:
        String = input()
        if quit_check(String):
            Mode = MENU_MODE
        else:
            print(decrypt(String, Key))
    elif Mode == KEY_FINDER_MODE:
        String = input()
        if quit_check(String):
            Mode = MENU_MODE
        else:
            picks = pick_key(String)
            if PICK_KEYS_IN_TXT:
                with open("picks.txt", 'a', encoding="utf-8") as file:
                    for i, string in enumerate(pick_key(String)):
                        try:
                            file.write(f"{i} - {string}\n")
                        except Exception as exception:
                            file.write(f"{i} - {exception}\n")
            else:
                for i, string in enumerate(pick_key(String)):
                    try:
                        print(f"{i} - {string}")
                    except Exception as exception:
                        print(f"{i} - {exception}")
    elif Mode == QUIT_ID:
        Exit = True
    if Mode != QUIT_ID and not Exit:
        print("#"*EDGE_LENGTH)
