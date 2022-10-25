import re

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