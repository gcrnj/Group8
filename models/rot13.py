from constants import ALPHABETS

from models.encryption_decryption_base import EncryptionBase
from models.encryption_decryption_result import Result


class Rot13(EncryptionBase):
    def encrypt(self, code: str) -> Result:
        return self.process(is_encryption=True, code=code)

    def decrypt(self, code: str) -> Result:
        return self.process(is_encryption=False, code=code)

    # Shift an input character by a certain number of positions in the alphabet
    def __alphabet_conversion(self, character: str, indention: int) -> str:
        index = ALPHABETS.index(character.upper()) + indention  # add index of the alphabet and indention(13 or -13)
        return ALPHABETS[index % len(ALPHABETS)]  # get the alphabet by the modulo of the length of the alphabet.

    def process(self, is_encryption: bool, code: str):
        # if encryption, add 13 indexes. If decryption, minus 13 indexes.
        indention = 13 if is_encryption else -13
        result = ""
        if code:  # Check if code is not empty
            for character in code:
                # Check if it is an alphabet
                if character.isalpha():
                    # add the index if alphabet
                    result += self.__alphabet_conversion(character, indention)
                else:
                    # add the character if not
                    result += character
        return Result(is_passed=True, message=result)
