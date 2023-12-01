import sys
from models.polybius import Polybius
from constants import *
from models.rot13 import Rot13


class Group8Project:

    def __init__(self):
        self.rot13 = Rot13()
        self.polybius = Polybius()

    def __exit_all(self):
        print(goodbyeMessage)
        sys.exit()

    def clear_console(self):
        pass  # Todo clear console

    def get_user_selection(self) -> Topic:
        selected = Topic.Invalid
        while selected == Topic.Invalid:
            userSelection = input(
                f"{divider}"
                f"{userSelectionQuestion} {newLine}"
                f"{rot13EncryptionOption} {newLine}"
                f"{rot13DecryptionOption} {newLine}"
                f"{polybiusEncryptionOption} {newLine}"
                f"{polybiusDecryptionOption} {newLine}"
                f"{exitOption} {newLine}"
                f"{divider}"
                f"{selectionText}"
            ).upper()  # Convert to uppercase so that the input is NOT case-sensitive
            isValidTopicsOption = any(userSelection == topic.value for topic in Topic)
            if isValidTopicsOption and userSelection != Topic.Exit.value and userSelection != Topic.Invalid.value:
                selected = Topic.find_member_by_value(userSelection)
            elif userSelection == Topic.Exit.value:  # Exit
                self.exit_all()
            else:  # Invalid
                print(invalidOption)
                selected = Topic.Invalid
        return selected

    # Rot 13 - Encrypt
    def encrypt_rot13(self):
        self.rot13.perform_encryption(input("Decrypted code > "))

    # Rot 13 - Decrypt
    def decrypt_rot13(self):
        self.rot13.perform_decryption(input("Encrypted Code > "))

    # Polybius - Encrypt
    def encrypt_polybius(self):
        self.polybius.perform_encryption(input("Decrypted code > "))
        pass

    # Polybius - Decrypt
    def decrypt_polybius(self):
        self.polybius.perform_decryption(input("Decrypted code > "))
        pass


if __name__ == '__main__':
    print(title)
    group_project = Group8Project()
    selection = group_project.get_user_selection()

    while selection != Topic.Exit:
        group_project.clear_console()
        if selection == Topic.ROT13_Encryption:
            group_project.encrypt_rot13()
        if selection == Topic.ROT13_Decryption:
            group_project.decrypt_rot13()
        elif selection == Topic.Polybius_Encryption:
            group_project.encrypt_polybius()
        elif selection == Topic.Polybius_Decryption:
            group_project.decrypt_polybius()
        selection = group_project.get_user_selection()
    print(exitMessage)
