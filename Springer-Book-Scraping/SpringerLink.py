import time
import requests
import pathlib
from bs4 import BeautifulSoup

file1 = open("springlink.txt", 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    print(line.strip())
    if len(line.strip()) > 0:
        r = requests.get(line.strip())
        soup = BeautifulSoup(r.content.decode(), 'html.parser')
        try:
            title = soup.find("div", {"class": "page-title"}).find("h1").text + ".pdf"
            url = "https://link.springer.com" + soup.find("a", {"class": "test-bookpdf-link"}).attrs['href']
            print((count + 1), "downloading:", title)

            file = pathlib.Path("Springer_Book/" + title)
            if not file.exists():
                file = requests.get(url)
                open('Springer_Book/' + title, 'wb').write(file.content)
                time.sleep(5)
        except:
            print("hatalı link")
        count += 1
