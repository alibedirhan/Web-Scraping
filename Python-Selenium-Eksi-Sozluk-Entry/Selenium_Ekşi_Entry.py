from selenium import webdriver # Selenium içindeki webdriver ı dahil ettik
import time #web sayfası açılınca ne kadar süre kalması gerektiğini belirtmek gerek

browser = webdriver.Firefox() # Firefox browser ı açmak için
url = "https://eksisozluk.com/ali-ulvi-yilmazer--2215579" # gideceğimiz url adresimiz

browser.get(url) # browserden url e gitmek için

time.sleep(5) # açılan sayfa 5 saniye beklesin


elements = browser.find_elements_by_css_selector(".content")
authors = browser.find_elements_by_css_selector(".info")


for element in elements:
    print("******************************")
    print(element.text)
        

browser.close() # 5 saniye sonra browser ı kapatır

