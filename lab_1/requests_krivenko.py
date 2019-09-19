import requests
from bs4 import BeautifulSoup
print("Hello")
page_url ='https://meduza.io/articles'
meduza = requests.get(page_url)
meduza_constant = meduza.text
if meduza.status_code == 200:
 #print(meduza.text)
 print("yay")
else:
 print("oops")
parced_page = BeautifulSoup(meduza_constant)
print ( type(parced_page))
print ( parced_page.title.text)