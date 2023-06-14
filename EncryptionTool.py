class EncryptionTool:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            encrypted_char = chr(ord(char) + self.key)
            encrypted_message += encrypted_char
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for char in encrypted_message:
            decrypted_char = chr(ord(char) - self.key)
            decrypted_message += decrypted_char
        return decrypted_message

def main():
    key = 5
    message = "Hello, World!"

    tool = EncryptionTool(key)
    encrypted_message = tool.encrypt(message)
    decrypted_message = tool.decrypt(encrypted_message)

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
