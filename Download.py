import requests
from bs4 import BeautifulSoup
def download_images():
    url_link = "https://mkops.com"  # Replace this with the website's URL
    get_url = requests.get(url_link, headers={"User-Agent": "Mozilla/5.0"})
    print(get_url.status_code)
    soup = BeautifulSoup(get_url.text, 'html.parser')
    images = soup.find_all('img')
    print(images)
    image_sources = []

    for image in images:
        image_sources.append(url_link + "/" + image.get('src'))

    print(image_sources)
    for image in image_sources:
        print(image)
        webs = requests.get(image)
        open('images/' + image.split('/')[-1], 'wb').write(webs.content)
