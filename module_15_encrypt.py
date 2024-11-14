class Encrypt:
    def __init__(self, s):
        self.s = s.lower()

    def encrypt_message(self):
        encrypted_message = ""
        for char in self.s:
            if char.isalpha():
                encrypted_message += chr(ord('z') - ord(char) + ord('a'))
            elif char == ' ':
                encrypted_message += '$'
            else:
                encrypted_message += char
        return encrypted_message

# Get input from the user
s = input("Enter the string: ")

# Create an Encrypt object
encryptor = Encrypt(s)

# Encrypt the message
encrypted_message = encryptor.encrypt_message()

# Print the encrypted message
print(encrypted_message)