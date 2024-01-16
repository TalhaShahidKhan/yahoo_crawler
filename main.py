import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/crypto"
r = requests.get(url)
if r.status_code == 200:
    with open("y_finance.html","w") as f:
        f.write(r.text)

with open("y_finance.html","r") as f:
    soup = BeautifulSoup(f,"html.parser")
tabel = soup.find("table", class_ = "W(100%)")

rows = tabel.find("tbody").find_all("tr")
for row in rows:
    names = row.find_all("td",attrs={"aria-label":"Name"})
    print(names)
    