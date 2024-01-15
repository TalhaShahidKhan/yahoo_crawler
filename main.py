import requests
from bs4 import BeautifulSoup
url = "https://finance.yahoo.com/crypto"
r = requests.get(url)
if r.status_code == 200:
    with open("y_finance.html","w") as f:
        f.write(r.text)

with open("y_finance.html","r") as f:
    soup = BeautifulSoup(f,"html.parser")
    

