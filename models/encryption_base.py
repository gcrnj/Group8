from abc import ABC, abstractmethod

from constants import encryptionResult, decryptionResult


class EncryptionBase(ABC):

    def perform_encryption(self, code: str):
        print(f"{encryptionResult} {self.encrypt(code)}")

    def perform_decryption(self, code: str):
        print(f"{decryptionResult} {self.decrypt(code)}")

    @abstractmethod
    def encrypt(self, code: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, code: str) -> str:
        pass
