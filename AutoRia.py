import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
url="https://auto.ria.com/uk/newauto/marka-jeep/"
def pars(site=url):
    inf=[]
    res = requests.get(site)
    if res.status_code != 200:
        print("Error 1")
    else:
        soup = bs(res.text, features="html.parser")
        soup_list = soup.find_all("section", class_="propositions")
        for i in soup_list:
            usd = soup.find("span", class_="green bold size22 tooltip-price")
            ua = soup.find("span", class_="size16")
            reg = soup.find("span", class_="item region")
            inf.append({
                "title": i.find("h3", class_="propositions_name").get_text(),
                "link": i.find("a").get("href"),
                "USD": usd,
                "UA": ua,
                "REG": reg
            })
    print(inf)
pars()