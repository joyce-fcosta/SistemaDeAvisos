from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get("http://www.python.org")