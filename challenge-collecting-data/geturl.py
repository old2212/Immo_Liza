from functools import lru_cache
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
from multiprocessing import Pool
import itertools
import json
import re
import httpx
from bs4 import BeautifulSoup
import requests

def set_up_threads(all_search_pages):
    with Pool() as pool:
        return pool.map(get_urls, all_search_pages, timeout = 60)

def get_urls(url, max):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(2)
    cookie_button = driver.find_element(By.XPATH, "//*[@id='uc-btn-accept-banner']")
    time.sleep(1)
    cookie_button.click()
    list_of_urls = []
    for i in range(max):
        try:
            paragraphs_with_link = driver.find_elements(By.XPATH, "//h2/a[@href]")
            for paragraph_with_link in paragraphs_with_link:
                    list_of_urls.append(paragraph_with_link.get_attribute('href'))
            #wait = WebDriverWait(driver, 10)
            #lol = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='pagination__link pagination__link--next button button--text button--size-small']")))
            driver.find_element(By.XPATH, "//*[@class='pagination__link pagination__link--next button button--text button--size-small']").click()
            #print(lol.get_attribute('href'))
        except StaleElementReferenceException:
            pass
        i+=1
    driver.close()
    return list_of_urls

def get_max_pages(url):
    driver = webdriver.Firefox()
    driver.get(url)
    last_page = driver.find_element(By.XPATH, "//a[@class='pagination__skip']/following::*").text
    last_page = re.sub("^Page.*\\n", "", last_page)
    driver.close()
    return int(last_page)

def save(element, name):
    with open(f"{name}.json", "w") as write_file:
        json.dump(element, write_file) 

#####################
list_of_list_of_all_urls = []
all_urls_to_cure = []
static_all_urls = []
all_data = []
url_house = 'https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance'
url_app = 'https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page=1&orderBy=relevance'
ignored_exceptions = (NoSuchElementException,StaleElementReferenceException)
#get_urls_parameters_for_pool = [(url_house,get_max_pages(url_house)),(url_app,get_max_pages(url_app))]
get_urls_parameters_for_pool = [(url_house,2),(url_app,2)]


with Pool() as pool:
    all_urls_to_cure = list(pool.starmap(get_urls, get_urls_parameters_for_pool))
all_urls_to_cure = list(itertools.chain.from_iterable(all_urls_to_cure)) # Flat la liste de liste en liste
print(len(all_urls_to_cure))
all_urls = list(dict.fromkeys(all_urls_to_cure)) #remove duplicates 
print(len(all_urls_to_cure))
all_urls = [item for item in all_urls_to_cure if "project" not in item]
print(len(all_urls))  
save(all_urls,'all_urls')

# for url in all_urls:
#     static_url = re.sub("\?.*",'',url)
#     static_all_urls.append(static_url)

# #print(static_all_urls)
# save(all_urls, 'all_urls')
# save(static_all_urls, 'static_all_urls')