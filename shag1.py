# import requests
from bs4 import BeautifulSoup
#
# url = "https://manga-chan.me"
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("manga2.html", 'w', encoding="utf-8") as file:
#     file.write(src)

with open("manga2.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
aph = soup.find_all(class_="sidetag")
s = []
q = []
l = []
for i in aph:
    s.append(i.text.strip())

for i in s:
    q.append(i[4:])

for i in aph:
    l.append("https://manga-chan.me" + i.find("a").get("href"))

x = zip(q, l)
y = []
for i in x:
    y.append(i)

a = dict(y)