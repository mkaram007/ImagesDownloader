import hashlib
from getpass import getpass
from Download import download_images
authenticated = False


def signup():
    username = input("Enter Username: ")
    pwd = getpass("Enter password: ")
    conf_pwd = getpass("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
            f.write(username + "\n")
            f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")


def login():
    username = input("Enter username: ")
    pwd = getpass("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    try:
        with open("credentials.txt", "r") as f:
            stored_username, stored_pwd = f.read().split("\n")
            f.close()
    except FileNotFoundError:
        print("You don't have any registered users, enter 4 to register")
    if username == stored_username and auth_hash == stored_pwd:
        print("Logged in Successfully!")
        return True

    else:
        print("Login failed! \n")


def user_choice():
    global authenticated
    while 1:
        print("Please choose what you want to do")
        print("1.Login")
        print("2.Download")
        print("3.Exit")
        try:
            ch = int(input("Enter your choice: "))

            if ch == 4:
                signup()
            if ch == 1:
                if not authenticated:
                    authenticated = login()
                else:
                    print("You are already signed in")
            elif ch == 2:
                if authenticated:
                    download_images()
                else:
                    print("You are unauthorized")
            elif ch == 3:
                exit()
            else:
                print("Wrong Choice!")
        except (ValueError, UnboundLocalError):
            print("Wrong Choice!")
