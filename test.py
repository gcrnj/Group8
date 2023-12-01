import constants
from models.polybius import Polybius
from models.rot13 import Rot13

__polybius = Polybius()
__rot13 = Rot13()
__hello_world = "Hello World"
__cpe_c311 = "CPE C311-301G Operating Systems T/F"
__all_letters = "The quick brown fox jumps over the lazy dog"


def failed_get_expected(code, expected, result) -> str:
    return f"        - Code:        {code}\n" \
           f"        - Expected:    {expected}\n" \
           f"        - Result:      {result}\n\n"


def testROT13Encryption() -> str:
    __result = ""
    to_encrypt = [
        ###
        # HOW TO USE?
        # [ DECRYPTED_CODE, EXPECTED_ENCRYPTED_VALUE]
        ###
        [__hello_world, "Uryyb Jbeyq"],
        [__cpe_c311, "PCR P311-301T Bcrengvat Flfgrzf G/S"],
        [__all_letters, "Gur dhvpx oebja sbk whzcf bire gur ynml qbt"],
    ]
    for my_list in to_encrypt:
        if __rot13.encrypt(my_list[0]) != my_list[1]:
            __result += failed_get_expected(
                my_list[0],  # Word to Encrypt
                my_list[1],  # Expected Value
                __rot13.encrypt(my_list[0]),  # Encrypted Value
            )
    return __result


def testROT13Decryption() -> str:
    __result = ""
    to_decrypt = [
        ###
        # HOW TO USE?
        # [ ENCRYPTED_CODE, EXPECTED_DECRYPTED_VALUE]
        ###
        ["Uryyb Jbeyq", __hello_world],
        ["PCR P311-301T Bcrengvat Flfgrzf G/S", __cpe_c311],
        ["Gur dhvpx oebja sbk whzcf bire gur ynml qbt", __all_letters],
    ]
    for my_list in to_decrypt:
        if __rot13.decrypt(my_list[0]) != my_list[1]:
            __result += failed_get_expected(
                my_list[0],  # Word to Encrypt
                my_list[1],  # Expected Value
                __rot13.decrypt(my_list[0]),  # Decrypted Value
            )
    return __result


def testPolybiusEncryption() -> str:
    __result = ""
    to_encrypt = [
        ###
        # HOW TO USE?
        # [ ENCRYPTED_CODE, EXPECTED_DECRYPTED_VALUE]
        ###
        [__hello_world, "23 15 31 31 34 52 34 42 31 14"],
        # [__cpe_c311, "13 35 15 13 22 34 35 15 42 11 44 24 33 22 43 54 43 44 15 32 43 44 21"],
        [__all_letters, "44 23 15 41 45 24 13 25 12 42 34 52 33 21 34 53 24 45 32 35 43 34 51 15 42 44 23 15 31 11 55 54 14 34 22"],
    ]
    for my_list in to_encrypt:
        if __polybius.encrypt(my_list[0]) != my_list[1]:
            __result += failed_get_expected(
                my_list[0],  # Word to Encrypt
                my_list[1],  # Expected Value
                __polybius.encrypt(my_list[0]),  # Encrypted Value
            )
    return __result


def testPolybiusDecryption() -> str:
    __result = ""
    to_decrypt = [
        ###
        # HOW TO USE?
        # [ ENCRYPTED_CODE, EXPECTED_DECRYPTED_VALUE]
        ###
        ["23 15 31 31 34 52 34 42 31 14", __hello_world],
        # ["44 23 15 41 45 24 13 25 12 42 34 52 33 21 34 53 24 45 32 35 43 34 51 15 42 44 23 15 31 11 55 54 14 34 22", __all_letters],
    ]
    for my_list in to_decrypt:
        decrypted = __polybius.decrypt(my_list[0])
        expected = my_list[1].replace(constants.empty_space, constants.empty_string).upper()
        if decrypted != expected:
            __result += failed_get_expected(
                my_list[0],  # Word to Encrypt
                expected,  # Expected Value
                decrypted,  # Decrypted Value
            )
    return __result


def __print_pass(message):
    print(f"\033[92m{message}\033[0m")


def __print_failed(message, failed_message):
    print(f"\033[91m{message}\033[0m")
    print(f"\033[91m{failed_message}\033[0m")


if __name__ == '__main__':
    # ROT13 - Encryption
    rot13Encryption = testROT13Encryption()
    if rot13Encryption:
        __print_failed("ROT13 Encryption Failed", rot13Encryption)
    else:
        __print_pass("ROT13 Encryption Passed")

    # ROT13 - Decryption
    rot13Decryption = testROT13Decryption()
    if rot13Decryption:
        __print_failed("ROT13 Decryption Failed", rot13Decryption)
    else:
        __print_pass("ROT13 Decryption Passed")

    # Polybius - Encryption
    polybiusEncryption = testPolybiusEncryption()
    if polybiusEncryption:
        __print_failed("Polybius Encryption Failed", polybiusEncryption)
    else:
        __print_pass("Polybius Encryption Passed")

    # Polybius - Decryption
    polybiusDecryption = testPolybiusDecryption()
    if polybiusDecryption:
        __print_failed("Polybius Decryption Failed", polybiusDecryption)
    else:
        __print_pass("Polybius Decryption Passed")
