from constants import empty_space, empty_string, invalidPolybius
from models.encryption_decryption_base import EncryptionBase
from models.encryption_decryption_result import Result
import textwrap


class Polybius(EncryptionBase):

    #      1   2   3    4    5
    # 1    A   B   C    D    E
    # 2    F   G   H   I/J   K
    # 3    L   M   N    O    P
    # 4    Q   R   S    T    U
    # 5    V   W   X    Y    Z

    def __init__(self):
        self.dict = {
            'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
            'F': '21', 'G': '22', 'H': '23', 'IJ': '24', 'K': '25',
            'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
            'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
            'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55',
        }

    def __get_coordinates_of(self, code: str) -> str:
        for key, coordinates in self.dict.items():
            if code.upper() in key:
                return coordinates.__str__()
        # If not found, return the passed str
        return code.strip()

    def __get_key_of(self, coordinate: str) -> str:
        for key, value in self.dict.items():
            if value == coordinate.upper():
                return key[0]
        # If not found, return an empty string or another suitable default value
        return coordinate

    # [code] parameter is the user input
    def encrypt(self, code: str) -> Result:
        # initialize a result of lists
        result = [self.__get_coordinates_of(character)
                  for character in code
                  if character and character not in {'', ' '}
                  ]
        return Result(is_passed=True, message="".join(map(str, result)))

    # [code] parameter is the user input
    def decrypt(self, code: str) -> Result:
        # Remove all spaces in case of typo
        trimmed_code = code.replace(empty_space, empty_string)

        # Check if special chars is present
        if not trimmed_code.isdigit():
            # Return error
            return Result(is_passed=False, message=invalidPolybius)

        # Trim into a list of 2 characters each
        codes_list = textwrap.wrap(trimmed_code, 2)

        result = ''.join(self.__get_key_of(coordinate) for coordinate in codes_list if codes_list)

        return Result(is_passed=True, message=result)
