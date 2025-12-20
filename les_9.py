import urllib.request
import requests
from bs4 import BeautifulSoup
"""
opener = urllib.request.build_opener()
response = opener.open("https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0")
print(response.read())

response = requests.get("https://www.google.com/")
print(response.content)

response = requests.post(url="httpbin.org", data="Test data", headers={"h1": "Test title"})
print(response.text)
"""
response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
parsed_html = response.text
"""
response_parse = parsed_html.split("<span>")
result = []
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        #print(parse_elem_1)
        result.append(parse_elem_1)
print(result[4].split("</span>")[0])
"""
soup = BeautifulSoup(parsed_html, features="html.parser")
soup_list = soup.find_all(name="span", attrs={"class": "sc-65e7f566-0 WXGwg base-text"})
print(soup_list)