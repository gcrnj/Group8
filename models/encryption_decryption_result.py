class Result:
    # [is_passed] - If there is not error.
    # [message] - is the encrypted, decrypted, or error message depending on the value of [is_passed].
    def __init__(self, is_passed: bool, message: str):
        self.__is_passed = is_passed
        self.__message = message

    def is_passed(self):
        return self.__is_passed

    def message(self):
        return self.__message

    def __str__(self):
        return f"User(username={self.__is_passed}, email={self.__message})"
