import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
from pathlib import Path
import os
import tempfile
import sys
from getpass import getpass


def download_images():
    sources = get_website()
    download_dir = get_dir()
    for src in sources:
        print("Downloading...")
        image_src = requests.get(src)
        open(download_dir + "/" + src.split('/')[-1], 'wb').write(image_src.content)
    print("Success, another website???")
    download_images()


def get_website():
    website = input("Please enter the website's URL [https://nxlog.co]\n")
    if not website:
        website = "https://nxlog.co"

    try:
        resp = requests.get(website)
    except requests.exceptions.MissingSchema:
        website = '{protocol}{website}'.format(protocol="https://", website=website)
        resp = requests.get(website)
    print(resp.status_code)
    print(resp.text)
    if resp.status_code == 401:
        print("Unauthorized, please enter username and password for authentication")
        username = input("Username: ")
        password = getpass("Password: ")
        resp = requests.get(website, auth=(username, password))
        print(resp.text)
    sources = find_sources(website, resp)
    return sources


def get_dir():
    if not sys.stdout.isatty():
        download_dir = ""
    else:
        download_dir = input("Please enter the directory to save the downloaded images [./images}\n")
    Path(download_dir).mkdir(parents=True, exist_ok=True)
    if not download_dir:
        download_dir = "images/"
    if not validate_path(download_dir):
        print("You are not permitted to download files here")
        download_dir = get_dir()
    return download_dir


def validate_path(path):
    try:
        os.makedirs(path, exist_ok=True)
        temp_dir_path = tempfile.mkdtemp(dir=path)
        os.rmdir(temp_dir_path)
        return True
    except OSError:
        return False


def find_sources(website, resp):
    soup = BeautifulSoup(resp.text, 'html.parser')
    images = soup.find_all('img')
    sources = []
    for image in images:
        try:
            if image.get('src').split('.')[-1].lower() == "png":
                src = image.get('src')
                sources.append('{website}/{src}'.format(website=website, src=src))

        except AttributeError:
            print("No png images exist in this website")
    print(sources)
    return sources
