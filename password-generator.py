import secrets
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
characters = lowercase + uppercase + string.digits + string.punctuation
password_length = 12

password = ''.join(secrets.choice(characters) for _ in range(password_length))
print("Generated secure password:", password)

