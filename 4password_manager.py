from cryptography.fernet import Fernet
'''
def generate_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)
generate_key()'''

def load_key():
    with open("key.key","rb") as f:
        key = f.read()
        return key
key = load_key()
fer = Fernet(key)

master_passw = int(input("Enter Lock Screen password: "))
def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if not data:
                continue
            else:
                name, passw = data.split(":")
                print(f"user_name:{name} and password:{fer.decrypt(passw.encode()).decode()}")
            

def add():
    name = input("Enter Account name: ")
    passw = input("Enter password: ")
    with open("password.txt","a") as f:
        f.write(f"{name}:{fer.encrypt(passw.encode()).decode()}\n")


while True:
    user = input("view/add password? (or) 'Q' for 'Quit': ").lower()
    if user == "q":
        print("Thank You!")
        break

    if user == "view":
        view()
    elif user == "add":
        add()
    else:
        print("Invalid Input!")
        continue


