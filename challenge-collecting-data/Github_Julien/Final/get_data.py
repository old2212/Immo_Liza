from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re
import requests
import json
url = "https://www.immoweb.be/en/classified/apartment/for-sale/deinze/9800/10130388?searchId=63341f64bc8e6"


def get_data_from_site(url):
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    site_data_dic = {}
    for l in soup.html.find_all("tr"):
        if l.find("th"):
            a = str(l.find("th"))
            a = re.sub("<([^<]*)>", "", a)
            a = a.strip()
            a = a.replace("\n", "")
            a = a.replace("\t", "")
            if a is not None:
                th = a
            
            
        if l.find("td"):
            a = str(l.find("td"))
            a = re.sub("<([^<]*)>", "", a)
            a = a.strip()
            a = a.replace("\n", "")
            a = a.replace("\t", "")
            a = re.sub("\ {2,}",' ',a)
            td = a

        site_data_dic[th] = td
    return site_data_dic | get_data_from_url(url)

def get_data_from_url(url):
    url_content_dic = {}
    house_subtypes = ['house','villa', 'manor house','pavilion','other properties' 'mansion','castel','chalet','farmhouse','exceptional property','mixed-use building', 'town-house','apartment block','bungalow']
    apartment_subtypes =['apartment','ground floor', 'duplex','triplex', 'penthouse', 'kot', 'studio', 'loft', 'service flat']
    other_property_types =[]
    pattern = 'https://www.immoweb.be/en/classified/'
    url_data_content = re.sub(pattern,'',url).split('/')
    url_content_dic['subtype_of_property'] = url_data_content[0]
    if url_content_dic['subtype_of_property']  in apartment_subtypes:
        url_content_dic['type_of_property'] = 'apartment'
    elif url_content_dic['subtype_of_property']  in house_subtypes:
        url_content_dic['type_of_property'] = 'house'
    else:
        other_property_types.append(url_content_dic['subtype_of_property'])
        url_content_dic['type_of_property'] = 'other'
    url_content_dic['type_of_sale']= url_data_content[1]
    url_content_dic['locality']= url_data_content[2]
    url_content_dic['zip_code']= url_data_content[3]
    url_content_dic['url'] = str(url)
    return url_content_dic

def save(element, name):
    with open(f"{name}.json", "w") as write_file:
        json.dump(element, write_file)

# print(get_data_from_site(url))
# print(get_data_from_url(url))

############################################

all_data = []
f = open('all_urls.json')
all_urls_json = json.load(f)
f.close()
print(len(all_urls_json))
print(type(all_urls_json))

with ThreadPoolExecutor() as pool:
     all_data = list(pool.map(get_data_from_site, all_urls_json))

save(all_data, 'all_data')
print(all_urls_json[0])