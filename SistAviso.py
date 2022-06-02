from bs4 import BeautifulSoup

#import urllib.request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
page='https://web.whatsapp.com/'
driver.get(page)


#open_page=urllib.request.urlopen(page)
time.sleep(90)

html_page = driver.page_source

soup = BeautifulSoup(html_page, 'html.parser')

print(soup.prettify())