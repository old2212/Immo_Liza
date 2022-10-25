from functools import lru_cache
from pkgutil import get_data
import time
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import itertools
import json
import re
import httpx
from bs4 import BeautifulSoup
import requests
import lxml.html
from requests_html import HTMLSession

def set_up_threads(all_search_pages):
    with Pool() as pool:
        return pool.map(get_urls, all_search_pages, timeout = 60)

@lru_cache
def get_data_from_page(url):
    print(url)
    page_content = {}
    session = HTMLSession()
    r = session.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    for table_row in soup.find_all("tr"):
        if table_row.find("th") and table_row.find("td"):
            key_text = table_row.find("th").string
            # key_text = re.sub("\\n",'', key_text)
            # key_text = re.sub("[^\w]","",key_text)
            value_text = table_row.find("td").string
            # value_text = re.sub("\\n",'', value_text)
            # value_text = re.sub("[^\w]","",value_text)
            page_content[key_text] = value_text
    return page_content

def save(element, name):
    with open(f"{name}.json", "w") as write_file:
        json.dump(element, write_file) 

#####################
page_content = {}
all_data = []
f = open('all_urls.json')
all_urls_json = json.load(f)
f.close()
#print(len(all_urls_json))
#print(type(all_urls_json))

with ThreadPoolExecutor() as pool:
     all_data = list(pool.map(get_data_from_page, all_urls_json))

save(all_data, 'all_data')