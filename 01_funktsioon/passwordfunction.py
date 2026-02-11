import string, random

def createpassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(characters, length))
    return password

newpassword = createpassword(16)

print(f"Sinu uus salasõna on: {newpassword}")