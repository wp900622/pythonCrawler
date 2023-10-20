import requests
from bs4 import BeautifulSoup
import os
url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
headers = {"Cookie": "over18=1"}
request = requests.get(url, headers=headers)
soup = BeautifulSoup(request.text, "html.parser")
#print(soup.prettify())
spans = soup.find_all("span", class_="article-meta-value")

title = spans[2].text
dir_name = f"image/{title}"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

links = soup.find_all("a")
print(links)
for link in links:
    href = link.get("href")
    if not href:
        continue
    print(href)
