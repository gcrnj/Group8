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

    def get_user_selection(self) -> Topic:
        selected = Topic.Invalid
        while selected == Topic.Invalid:
            userSelection = input(
                f"{userSelectionQuestion} {newLine}"
                f"{rot13EncryptionOption} {newLine}"
                f"{rot13DecryptionOption} {newLine}"
                f"{polybiusEncryptionOption} {newLine}"
                f"{polybiusDecryptionOption} {newLine}"
                f"{exitOption} {newLine}"
                # f"{divider}"
                f"{selectionText}"
            ).upper()  # Convert to uppercase so that the input is NOT case-sensitive
            isValidTopicsOption = any(userSelection == topic.value for topic in Topic)
            if isValidTopicsOption and userSelection != Topic.Exit.value and userSelection != Topic.Invalid.value:
                selected = Topic.find_member_by_value(userSelection)
            elif userSelection == Topic.Exit.value:  # Exit
                self.__exit_all()
            else:  # Invalid
                print(invalidOption)
                print((divider * 2).strip())
                selected = Topic.Invalid
        return selected

    # Rot 13 - Encrypt
    def encrypt_rot13(self) -> bool:
        return self.rot13.perform_encryption(input("Decrypted code > "))

    # Rot 13 - Decrypt
    def decrypt_rot13(self) -> bool:
        return self.rot13.perform_decryption(input("Encrypted Code > "))

    # Polybius - Encrypt
    def encrypt_polybius(self) -> bool:
        return self.polybius.perform_encryption(input("Decrypted code > "))

    # Polybius - Decrypt
    def decrypt_polybius(self) -> bool:
        return self.polybius.perform_decryption(input("Encrypted code > "))


if __name__ == '__main__':
    print(title)
    group_project = Group8Project()
    selection = group_project.get_user_selection()
    is_input_valid = False

    while selection != Topic.Exit or not is_input_valid:
        if selection == Topic.ROT13_Encryption:
            is_input_valid = group_project.encrypt_rot13()
        if selection == Topic.ROT13_Decryption:
            is_input_valid = group_project.decrypt_rot13()
        elif selection == Topic.Polybius_Encryption:
            is_input_valid = group_project.encrypt_polybius()
        elif selection == Topic.Polybius_Decryption:
            is_input_valid = group_project.decrypt_polybius()

        if is_input_valid:
            print((divider * 2).strip())
        selection = group_project.get_user_selection()
    print(exitMessage)
