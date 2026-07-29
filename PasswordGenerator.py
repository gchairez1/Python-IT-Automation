import secrets
import string

alphabet = string.ascii_letters + string.digits + "!@#$%^&*"

password = "".join(secrets.choice(alphabet) for _ in range(20))

print("Generated Password")
print(password)
