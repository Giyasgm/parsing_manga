import requests
from bs4 import BeautifulSoup

spisok = []
name = input()

for i in range(0, 60, 20):
    url = f"https://manga-chan.me/tags/{name}?offset={i}"

    q = requests.get(url)
    lol = q.content

    soup = BeautifulSoup(lol, "lxml")
    ssl = soup.find_all(class_="manga_images")

    for i in ssl:
        sasa = "https://manga-chan.me" + i.find("a").get("href")
        spisok.append(sasa)

