import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.ptt.cc/bbs/NBA/index6500.html"
headers = {"User-Agent": "Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.40"}
request = requests.get(url, headers=headers)
# print(request.text)
soup = BeautifulSoup(request.text, "html.parser")
article = soup.find_all("div", class_="r-ent")
data_list = []

# print(article[0])
for a in article:
    dict = {}
    title = a.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "沒有標題"
    # print(title)
    dict["標題"] = title
    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    dict["人氣"] = popular
    #print(f"標題:{title},人氣:{popular}")
    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "沒有日期"
    print(f"標題:{title},人氣:{popular},日期:{date}")
    dict["日期"] = date
    data_list.append(dict)
print(data_list)

df = pd.DataFrame(data_list)
df.to_excel("ppt_nba_copy.xlsx",index=False , engine="openpyxl")

print("已經成功轉成ppt_nba_json")

if request.status_code == 200:
    with open("output.html",'w',encoding="utf-8") as f:
        f.write(request.text)
    print("寫入成功")
else:
    print("沒有抓到資料")


