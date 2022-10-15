import hashlib
from getpass import getpass
from Download import download_images


def signup():
    email = input("Enter email address: ")
    pwd = getpass("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")


def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
        f.close()
    if email == stored_email and auth_hash == stored_pwd:
        print("Logged in Successfully!")
        return True

    else:
        print("Login failed! \n")


def check():
    authenticated = False
    while 1:
        print("Please choose what you want to do")
        #print("1.Signup")
        print("1.Login")
        print("2.Download")
        ch = int(input("Enter your choice: "))
        #if ch == 1:
        #    signup()
        if ch == 1:
            authenticated = login()
        elif ch == 2:
            if authenticated:
                download_images()
            else:
                print("You are unauthorized")
        else:
            print("Wrong Choice!")
