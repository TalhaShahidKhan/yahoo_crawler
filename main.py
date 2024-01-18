import requests
import os
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
url = "https://finance.yahoo.com/crypto"
r = requests.get(url)
if r.status_code == 200:
    with open("y_finance.html","w") as f:
        f.write(r.text)
        f.close()

with open("y_finance.html","r") as f:
    soup = BeautifulSoup(f,"html.parser")
    f.close()
tabel = soup.find("table", class_ = "W(100%)")

rows = tabel.find("tbody").find_all("tr")

name_l = []
price_l = []
change_l = []
changep_l = []
marc_l = []

for row in rows:
    names = row.find_all("td",attrs={"aria-label":"Name"})
    price = row.find_all("td",attrs={"aria-label":"Price (Intraday)"})
    change = row.find_all("td",attrs={"aria-label":"Change"})
    change_p = row.find_all("td",attrs={"aria-label":"% Change"})
    mc = row.find_all("td",attrs={"aria-label":"Market Cap"})
    name_l.append(names[0].string)
    price_l.append(price[0].string)
    change_l.append(change[0].string)
    changep_l.append(change_p[0].string)
    marc_l.append(mc[0].string)
data_dict = {
    "Name":name_l,
    "Price":price_l,
    "Change":change_l,
    "Change(%)":changep_l,
    "Market Cap":marc_l
}

df = pd.DataFrame(data=data_dict)

df.to_csv("Crypto.csv", index=False)

df.to_excel("Crypto.xlsx",index=False)


    
