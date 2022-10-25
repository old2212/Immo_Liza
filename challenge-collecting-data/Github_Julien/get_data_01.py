from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from concurrent.futures import ThreadPoolExecutor
import threading

list_of_list_of_all_urls = []
all_urls = []
all_data = []

def init_and_cookie_click():
    driver.get(all_search_pages[0])
    time.sleep(1)
    cookie_button = driver.find_element(By.XPATH, "//*[@id='uc-btn-accept-banner']")
    time.sleep(1)
    cookie_button.click()
    time.sleep(3)

def set_up_threads(all_search_pages):
    with ThreadPoolExecutor(max_workers=3) as executor:
        return executor.map(get_urls, all_search_pages, timeout = 60)

def all_search_pages():
    all_pages = []
    for i in range(1,3):
        url = f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page={i}&orderBy=relevance"
        all_pages.append(url)
    return all_pages

def get_urls(url):
    driver.get(url)
    page_urls = []    
    house_urls = driver.find_elements(By.XPATH, "//h2/a[@href]")
    for house_url in house_urls:
        if "From" not in house_url.get_attribute('aria-label'):
            page_urls.append(house_url.get_attribute('href'))
    return page_urls

def get_data_from_page(url):
    driver.get(url)
    page_content = {}
    table_rows = driver.find_elements(By.XPATH, "//tr[@class = 'classified-table__row']")
    for table_row in table_rows:
        try:
            tr_header = table_row.find_element(By.XPATH, ".//th").text
            tr_data = table_row.find_element(By.XPATH, ".//td").text
            page_content[tr_header] = tr_data
        except NoSuchElementException:
            pass
    return page_content

#####################

ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
all_search_pages = all_search_pages()
#print(all_search_pages)
driver = webdriver.Firefox()
init_and_cookie_click()

for search_page in all_search_pages:
    list_of_list_of_all_urls.append(get_urls(search_page))

# Optimization : does NOT work
# try:
#     for result in set_up_threads(all_search_pages):
#         list_of_list_of_all_urls.append(result)
# except ignored_exceptions:
#     pass

for sublist in list_of_list_of_all_urls:
    for item in sublist:
        all_urls.append(item)

print(all_urls)
print(len(all_urls))

for url in all_urls:
    print(get_data_from_page(url))
    all_data.append(get_data_from_page(url))

print(all_data)

driver.close()