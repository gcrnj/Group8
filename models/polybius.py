from constants import empty_space
from models.encryption_base import EncryptionBase


class Polybius(EncryptionBase):

    #      1   2   3    4    5
    # 1    A   B   C    D    E
    # 2    F   G   H   I/J   K
    # 3    L   M   N    O    P
    # 4    Q   R   S    T    U
    # 5    V   W   X    Y    Z

    def __init__(self):
        self.dict = {
            'A': (1, 1), 'B': (1, 2), 'C': (1, 3), 'D': (1, 4), 'E': (1, 5),
            'F': (2, 1), 'G': (2, 2), 'H': (2, 3), 'IJ': (2, 4), 'K': (2, 5),
            'L': (3, 1), 'M': (3, 2), 'N': (3, 3), 'O': (3, 4), 'P': (3, 5),
            'Q': (4, 1), 'R': (4, 2), 'S': (4, 3), 'T': (4, 4), 'U': (4, 5),
            'V': (5, 1), 'W': (5, 2), 'X': (5, 3), 'Y': (5, 4), 'Z': (5, 5),
        }
        self.j = 'J'

    def __get_coordinates_of(self, code: str) -> str:
        for key, (row, col) in self.dict.items():
            if code.upper() in key:
                return f"{str(row)}{str(col)}"
        # If not found, return the passed str
        return code.strip()

    def __get_key_of(self, coordinate: tuple) -> str:
        for key, value in self.dict.items():
            if value == coordinate:
                return key[0]
        # If not found, return an empty string or another suitable default value
        return ""

    # [code] parameter is the user input
    def encrypt(self, code: str) -> str:
        result = []
        if code:
            for character in code:
                result.append(self.__get_coordinates_of(character))
        result = [value for value in result if value != '' and value != ' ']  # Remove all empty values
        return " ".join(map(str, result))

    # [code] parameter is the user input
    def decrypt(self, code: str) -> str:
        # code = code.replace(empty_space, empty_string)
        result = ""
        codes_list = code.split(empty_space)

        if codes_list:  # List is not empty
            for coordinate in codes_list:
                if len(coordinate) == 2:
                    result += self.__get_key_of((int(coordinate[0]), int(coordinate[1])))
                else:
                    return f"Invalid Value: {coordinate}"

        return result
