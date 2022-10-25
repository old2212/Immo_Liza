import json
import pandas as pd

f = open('all_data.json')
all_data_json = json.load(f)
f.close()
print(len(all_data_json))
print(type(all_data_json))
print(all_data_json[3176])

df = pd.DataFrame(all_data_json)
df.to_csv(r'all_data_frame.csv', index = False, header=True, encoding='utf-8', escapechar='|')
