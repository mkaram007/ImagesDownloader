# Welcome to the Image Downloder Linux CLI tool
### Image Downloader CLI tool allows its user to download only file with html tag <img> and extension .png in the website the user provides
### The downloaded files would be saved in the directory the user provides
### If the user-provided website required authentication, the user would provide username and password credentials

## Requirements
python3  
pip3  
git  

pip3 dependency: virtualenv  
```
sudo pip3 install virtualenv 
```
# How to use the tool
## Clone the repository
```
git clone https://github.com/mkaram007/ImagesDownloader ~/ImagesDownloader
```
## Create your python virtual environment
```
python3 -m venv ~/ImagesDownloader/venv
```
## Install python dependencies
```
~/ImagesDownloader/venv/bin/pip3 install -r ~/ImagesDownloader/lib/requirements.txt  
```

## Run the tool using the following command
```
~/ImagesDownloader/venv/bin/python3 ~/ImagesDownloader/main.py
```
