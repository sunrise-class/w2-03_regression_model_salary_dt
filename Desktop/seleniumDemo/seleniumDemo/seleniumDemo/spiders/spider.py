from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import scrapy
import time

class QuoteSpider(scrapy.Spider):
    name = 'quotes'


options = ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
options.headless = True

driver.get('https://quotes.toscrape.com/js/')
content = driver.find_element(By.LINK_TEXT, 'Login')
content.click()

time.sleep(3)

username = driver.find_element(By.ID, 'username')
password = driver.find_element(By.ID, 'password')
btn = driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]')

username.send_keys('admin')
password.send_keys('admin123')
btn.send_keys(Keys.ENTER)

time.sleep(3)
# driver.close()
