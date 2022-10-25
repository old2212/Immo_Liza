from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page=1&orderBy=relevance"

driver = webdriver.Firefox()
driver.get(url)

#print(driver.title)
#assert "Immoweb" in driver.title

time.sleep(3)
cookie_button = driver.find_element(By.XPATH, "//*[@id='uc-btn-accept-banner']")
time.sleep(1)
cookie_button.click()
time.sleep(1)


page_urls = []
house_urls = driver.find_elements(By.XPATH, "//h2/a[@href]")
for house_url in house_urls:
    if "From" not in house_url.get_attribute('aria-label'):
        page_urls.append(house_url.get_attribute('href'))
        print (house_url.get_attribute('aria-label'))
        print(type(house_url.get_attribute('aria-label')))

print(page_urls)

driver.close()