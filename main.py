from Group8Project import Group8Project
from constants import *


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
