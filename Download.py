import requests
from bs4 import BeautifulSoup


def download_images():
    url_link = input("Please enter the website's URL\n")  # Replace this with the website's URL
    try:
        get_url = requests.get(url_link, headers={"User-Agent": "Mozilla/5.0"})
    except requests.exceptions.MissingSchema:
        url_link = "https://"+url_link
        get_url = requests.get(url_link, headers={"User-Agent": "Mozilla/5.0"})
    print(get_url.status_code)
    soup = BeautifulSoup(get_url.text, 'html.parser')
    images = soup.find_all('img')
    print(images)
    image_sources = []
    sources = []
    print(images)
    for image in images:
        try:
            if image.get('src').split('.')[-1].lower() == "png":
                src = image.get('src')
                sources.append('{url_link}/{src}'.format(url_link=url_link, src=src))

        except AttributeError:
            print("No png images exist in this website")
    print(sources)
    for src in sources:
        print(src)
        webs = requests.get(src)
        open('images/' + src.split('/')[-1], 'wb').write(webs.content)
