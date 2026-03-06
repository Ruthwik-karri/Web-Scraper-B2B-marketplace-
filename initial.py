import requests
from bs4 import BeautifulSoup

headers = {"user-agency":"Mozilla/5.0"}

url="https://dir.indiamart.com/search.mp?ss=industrial+machinery"
response=requests.get(url)

soup=BeautifulSoup(response.content,"html.parser")
print(len(soup))
results=soup.find_all("div",class_="cardbody")
for result in results:
    print(result)