from enum import Enum


class Topic(Enum):
    ROT13_Encryption = "RE"
    ROT13_Decryption = "RD"
    Polybius_Encryption = "PE"
    Polybius_Decryption = "PD"
    Exit = "X"
    Invalid = "Z"

    @classmethod
    def find_member_by_value(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"No member with value '{value}' found in enum {cls.__name__}")


# =========================== GENERAL STRINGS ==========================
newLine = "\n"
divider = "=" * 20 + newLine
title = """
 _____                    ___                                             
|   __|___ ___ _ _ ___   | . |                                            
|  |  |  _| . | | | . |  | . |                                            
|_____|_| |___|___|  _|  |___|                                            
                  |_|                                                     
                                     _                                    
 _____ _____ _____    ___   ___    _| |_    _____     _     _   _         
| __  |     |_   _|  |_  | |_  |  |   __|  |  _  |___| |_ _| |_|_|_ _ ___ 
|    -|  |  | | |     _| |_|_  |  |   __|  |   __| . | | | | . | | | |_ -|
|__|__|_____| |_|    |_____|___|  |_   _|  |__|  |___|_|_  |___|_|___|___|
                                    |_|                |___|
"""
encryptionResult = "Encryption Result > "
decryptionResult = "Decryption Result > "

goodbyeMessage = "Goodbye!"

# =========================== USER SELECTION ==========================
userSelectionQuestion = "What topic do you want to try?"
rot13EncryptionOption = f"[{Topic.ROT13_Encryption.value}]\t-\tROT13 Encryption"
rot13DecryptionOption = f"[{Topic.ROT13_Decryption.value}]\t-\tROT13 Decryption"
polybiusEncryptionOption = f"[{Topic.Polybius_Encryption.value}]\t-\tPolybius Encryption"
polybiusDecryptionOption = f"[{Topic.Polybius_Decryption.value}]\t-\tPolybius Decryption"
exitOption = f"[{Topic.Exit.value}]\t\t-\t{Topic.Exit.name}"
invalidOption = "\033[1m\033[3mYou selected an invalid selection.\033[0m"  # Prints in bold-italic
selectionText = "Selection > "
exitMessage = "Thank you"
empty_space = ' '
empty_string = ''
comma = ','

# =========================== ROT 13 ==========================
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
