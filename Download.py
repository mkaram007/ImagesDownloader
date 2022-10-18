import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os
import tempfile
import sys
from getpass import getpass


def download_images():
    sources = get_website()
    download_dir = get_dir()
    if len(sources) == 0:
        print("No png images in the website you provided, try another website")
        download_images()
    decision = input("Number of images is: {number}, would you like to download? [Y,n]".format(number=len(sources)))
    if decision == "Y" or decision == "y" or decision == "":
        print("Downloading...")
        for src in sources:
            print(src)
            image_src = requests.get(src)
            open(download_dir + "/" + src.split('/')[-1], 'wb').write(image_src.content)
        again = input("Success, another website???")
        if not again or again == "y" or again == "Y":
            download_images()
        else:
            print("Thanks for using Images Downloader")
            return
    elif decision == "n" or decision == "N":
        print("abort")
        download_images()


def get_website():
    website = input("Please enter the website's URL [nxlog.co]\n")
    if not website:
        website = "nxlog.co"
    try:
        try:
            resp = requests.get(website, allow_redirects=True)
        except requests.exceptions.MissingSchema:
            website = '{protocol}{website}'.format(protocol="http://", website=website)
            resp = requests.get(website, allow_redirects=True)
    except requests.exceptions.ConnectionError:
        print("Can't connect to the website you entered, try again")
        get_website()
        resp = ""
    #print(resp.history)
    #print(resp.url)
    #print(resp.status_code)
    #print(resp.text)
    if resp.status_code == 401:
        resp = basic_auth(website)
    sources = find_sources(website, resp)
    return sources


def basic_auth(website):
    print("Unauthorized, please enter username and password for authentication")
    username = input("Username: ")
    password = getpass("Password: ")
    resp = requests.get(website, auth=(username, password))
    #print(resp.text)
    return resp


def get_dir():
    download_dir = input("Please enter the directory to save the downloaded images [~/ImagesDownloader/images}\n")
    Path(download_dir).mkdir(parents=True, exist_ok=True)
    if not download_dir:
        download_dir = "{home_path}/ImagesDownloader/images/".format(home_path=Path.home())
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
            print("Found an image that's not in png extension")
    #print(sources)
    return sources
