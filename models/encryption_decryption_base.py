from abc import ABC, abstractmethod

from constants import encryption_result_message, decryption_result_message
from models.encryption_decryption_result import Result


class EncryptionBase(ABC):

    def perform_encryption(self, code: str) -> bool:
        encrypted_result = self.encrypt(code)
        print(f"{encryption_result_message} {encrypted_result.message}")
        return encrypted_result.is_passed

    def perform_decryption(self, code: str) -> bool:
        decrypted_result = self.decrypt(code)
        print(f"{decryption_result_message} {decrypted_result.message}")
        return decrypted_result.is_passed

    @abstractmethod
    def encrypt(self, code: str) -> Result:
        pass

    @abstractmethod
    def decrypt(self, code: str) -> Result:
        pass
