from constants import UPPER_LETTERS, LOWER_LETTERS

from models.encryption_base import EncryptionBase


class Rot13(EncryptionBase):
    def encrypt(self, code: str) -> str:
        return self.another(True, code)

    def decrypt(self, code: str) -> str:
        return self.another(False, code)

    def another(self, is_encryption: bool, code: str):
        indention = 13 if is_encryption else -13
        result = ""
        if code:  # code is not empty
            for character in code:
                if character.isupper():
                    result += self._alphabet_conversion(character, UPPER_LETTERS, indention)
                elif character.islower():
                    result += self._alphabet_conversion(character, LOWER_LETTERS, indention)
                else:
                    result += character
        return result

    def _alphabet_conversion(self, alphabet: str, cases: str, indention: int) -> str:
        index = cases.index(alphabet) + indention
        return cases[index % len(cases)]
