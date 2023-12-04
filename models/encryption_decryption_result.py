class Result:
    # [is_passed] - If there is not error.
    # [message] - is the encrypted, decrypted, or error message depending on the value of [is_passed].
    def __init__(self, is_passed: bool, message: str):
        self.is_passed = is_passed
        self.message = message

    def __str__(self):
        return f"User(username={self.is_passed}, email={self.message})"
