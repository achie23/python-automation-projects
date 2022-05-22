# pip install cryptography
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key_file.key", "wb") as keys:
        keys.write(key)

write_key()

def load_key():
    file = open("key_file.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    # create 'password.txt' file
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(password.encode()).decode())

while True:
    mode = input("Would you like to view existing password or add a new one (view/add)?, press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue