import requests
from bs4 import BeautifulSoup

# url = "https://manga-chan.me/tags/%D0%B1%D0%BE%D0%B5%D0%B2%D1%8B%D0%B5_%D0%B8%D1%81%D0%BA%D1%83%D1%81%D1%81%D1%82%D0%B2%D0%B0"
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("manga.html", 'w', encoding="utf-8") as file:
#     file.write(src)

with open("manga.html", encoding="utf-8") as file:
     src = file.read()

soup = BeautifulSoup(src, "lxml")
aph = soup.find_all(class_="manga_row1")
for i in aph:
    item1 = i.find(class_="title_link").text
    item2 = "https://manga-chan.me" + i.find("h2").find("a").get("href")
    print(item1, "\n", item2)
