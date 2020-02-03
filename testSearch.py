from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Search:
    def __init__(self, id):
        self.id = id

brand_id = ("searchAll")

class Input:
    def __init__(self, key):
        self.key = key

brand_key = ("adidas")

class Url:
    def __init__(self, url):
        self.url = url

brand_url = ("https://www.6pm.com/")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(brand_url)
input_element = driver.find_element_by_id(brand_id)
wait = WebDriverWait(driver, 10)
input_element.send_keys(brand_key)
input_element.submit()
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//*[@id='root']/div[1]/header/div[3]/div/div/div/a/span").click()
wait = WebDriverWait(driver, 100)
driver.quit()
