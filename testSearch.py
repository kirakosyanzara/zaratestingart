from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Chrome()
driver.get("https://www.6pm.com/")
input_element = driver.find_element_by_id('searchAll')
wait = WebDriverWait(driver, "10")
input_element.send_keys("adidas")
input_element.submit()
#def check_exists_by_id(searchAll):
  #  try:
   #     webdriver.find_element_by_id(searchAll)
  #  except NoSuchElementException:
   #     return False
   # return True
driver.quit()
